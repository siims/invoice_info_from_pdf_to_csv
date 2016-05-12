'''
Created on May 11, 2016

'''

import unittest

from test.resources import TEST_PDF_DATE_CREATED, TEST_PDF_FILENAME, TEST_PDF_NUM_PAGES
from test.resources import TEST_UNKNOWN_PDF_FILENAME
from application import openPdf, getPdfDateCreated, getPdfAsText, getPdfPages

class ApplicationTests(unittest.TestCase):

    def setUp(self):
        self.PDF_FILE = open(TEST_PDF_FILENAME, "r")
        self.PDF_FILE_UNKNOWN = open(TEST_UNKNOWN_PDF_FILENAME, "r")

    def tearDown(self):
        self.PDF_FILE.close()
        self.PDF_FILE_UNKNOWN.close()

    def testOpeningExistingPdf(self):
        pdf = openPdf(self.PDF_FILE)

        self.assertNotEqual(pdf, None)

    def testGetDateCreatedViaFilename(self):
        expectedDate = TEST_PDF_DATE_CREATED

        resultDate = getPdfDateCreated(fileDescriptor=self.PDF_FILE)

        self.assertEqual(expectedDate, resultDate)

    # TODO: this is almost identical to previous, can code duplication be eliminated?
    def testGetDateCreatedViaPdfDoc(self):
        expectedDate = TEST_PDF_DATE_CREATED

        resultDate = getPdfDateCreated(pdfDoc=openPdf(self.PDF_FILE))

        self.assertEqual(expectedDate, resultDate)

    def testGetPdfAsText(self):
        resultText = getPdfAsText(fileDescriptor=self.PDF_FILE)

        self.assertTrue(resultText is not None)
        self.assertTrue(isinstance(resultText, str), "Output must be text")

    def testGetPdfPages(self):
        pages = getPdfPages(self.PDF_FILE)

        self.assertEqual(TEST_PDF_NUM_PAGES, len(pages))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
