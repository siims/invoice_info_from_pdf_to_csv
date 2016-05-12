'''
Created on May 12, 2016

'''
import unittest

from test.resources import TEST_PDF_DATE_CREATED, TEST_PDF_FILENAME, TEST_PDF_TITLE, TEST_PDF_TYPE
from test.resources import TEST_UNKNOWN_PDF_FILENAME, TEST_UNKNOWN_PDF_TYPE
from application import openPdf, getPdfPages, models
import application.PdfInvoiceParser as parser

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

    def _parsePdfInvoice(self, fileDescriptor):
        pdfPages = getPdfPages(fileDescriptor=fileDescriptor)
        pdfDoc = openPdf(fileDescriptor)

        invoiceParser = parser.PdfInvoiceParser(pdfPage=pdfPages[0], pdfDoc=pdfDoc)
        invoice = invoiceParser.parse()

        return invoice

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()