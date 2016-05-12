import datetime
import application.models.InvoiceModel as models

# first test pdf from abhaldus
TEST_PDF_FILENAME = "test/resources/abhaldus_test_invoice.pdf"
TEST_PDF_DATE_CREATED_STRING = "2016-04-08"
TEST_PDF_DATE_CREATED = datetime.datetime.strptime(TEST_PDF_DATE_CREATED_STRING, "%Y-%m-%d").date()
TEST_PDF_TITLE = "A R V E  Nr. 4.16/R12-12"
TEST_PDF_TYPE = "ABHALDUS"
TEST_PDF_NUM_PAGES = 1

# second pdf which is not an invoice
TEST_UNKNOWN_PDF_FILENAME = "test/resources/unknown_test_invoice.pdf"
TEST_UNKNOWN_PDF_TYPE = "UNKNOWN"
