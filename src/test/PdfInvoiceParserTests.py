'''
Created on May 12, 2016

'''
import unittest

from test.resources import TEST_PDF_DATE_CREATED, TEST_PDF_FILENAME, TEST_PDF_TITLE, TEST_PDF_TYPE
from test.resources import TEST_PDF_COSTS
from test.resources import TEST_UNKNOWN_PDF_FILENAME, TEST_UNKNOWN_PDF_TYPE
from test.resources import TEST_FILENAME_FOR_TEST_PARSER_NOT_IMPLEMENTED, \
                           TEST_RELATIVE_FILENAME_FOR_TEST_PARSER_NOT_IMPLEMENTED, \
                           TEST_KEYWORD_FOR_TEST_PARSER_NOT_IMPLEMENTED
from application import openPdf, getPdfPages, models
import application.parsers as parser
import os

class PdfInvoiceParserTests(unittest.TestCase):

    def setUp(self):
        self.PDF_FILE = open(TEST_PDF_FILENAME, "r")
        self.PDF_FILE_UNKNOWN = open(TEST_UNKNOWN_PDF_FILENAME, "r")

    def tearDown(self):
        self.PDF_FILE.close()
        self.PDF_FILE_UNKNOWN.close()

    def testGetPdfAsModel(self):
        invoice = self._parsePdfInvoice(self.PDF_FILE)

        self.assertTrue(isinstance(invoice, models.InvoiceModel.InvoiceModel))

    def testGetPdfTitle(self):
        invoice = self._parsePdfInvoice(self.PDF_FILE)

        self.assertEqual(TEST_PDF_TITLE, invoice.title)

    def testDetectInvoiceType(self):
        invoice = self._parsePdfInvoice(self.PDF_FILE)

        self.assertEqual(TEST_PDF_TYPE, invoice.type)

    def testDetectInvoiceUnknownType(self):
        with self.assertRaises(models.InvoiceModel.InvoiceModel.InvoiceUnknownException):
            self._parsePdfInvoice(self.PDF_FILE_UNKNOWN)

    def testDetectInvoiceDateCreated(self):
        invoice = self._parsePdfInvoice(self.PDF_FILE)

        self.assertEqual(TEST_PDF_DATE_CREATED.month, invoice.month)
        self.assertEqual(TEST_PDF_DATE_CREATED.year, invoice.year)

    def testInvoiceParserNotImplemented(self):
        invoiceDetectionKeyword = TEST_KEYWORD_FOR_TEST_PARSER_NOT_IMPLEMENTED
        pdfPath = TEST_RELATIVE_FILENAME_FOR_TEST_PARSER_NOT_IMPLEMENTED

        try:
            self._createNewInvoiceParser(invoiceDetectionKeyword)

            pdfFile = open(pdfPath, "r")

            with self.assertRaises(parser.ParserNotImplemented):
                self._parsePdfInvoice(pdfFile)

        finally:
            pdfFile.close()
            self._deleteNewInvoiceParser(invoiceDetectionKeyword)

    def testParsingCosts(self):
        invoice = self._parsePdfInvoice(self.PDF_FILE)

        self.assertSetEqual(TEST_PDF_COSTS, invoice.costs)

    def _parsePdfInvoice(self, fileDescriptor):
        pdfPages = getPdfPages(fileDescriptor=fileDescriptor)
        pdfDoc = openPdf(fileDescriptor)

        invoiceParser = parser.PdfInvoiceParser(pdfPage=pdfPages[0], pdfDoc=pdfDoc)
        invoice = invoiceParser.parse()

        return invoice

    def _createNewInvoiceParser(self, invoiceDetectionKeyword):
        try:
            newInvoiceParser = open('./application/parsers/%s.py' % invoiceDetectionKeyword, "w+")

            newInvoiceParser.write("""
import application.parsers as parsers

class %(invoiceDetectionKeyword)s(parsers.BaseParser):
    pass
""" % {"invoiceDetectionKeyword": invoiceDetectionKeyword})

        finally:
            newInvoiceParser.close()

    def _deleteNewInvoiceParser(self, invoiceDetectionKeyword):
        os.remove('./application/parsers/%s.py' % invoiceDetectionKeyword)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
