import datetime
import application.models.CostModel as models

# first test pdf from abhaldus
TEST_PDF_FILENAME = "test/resources/abhaldus_test_invoice.pdf"
TEST_PDF_DATE_CREATED_STRING = "2016-04-08"
TEST_PDF_DATE_CREATED = datetime.datetime.strptime(TEST_PDF_DATE_CREATED_STRING, "%Y-%m-%d").date()
TEST_PDF_TITLE = "A R V E  Nr. 4.16/R12-12"
TEST_PDF_TYPE = "ABHALDUS"
TEST_PDF_NUM_PAGES = 1
TEST_PDF_COSTS = set(models.CostModel("Soojusenergia", 0, "/MWh", 59.42, 81.70),
                    models.CostModel("Majandamiskulud", 0, "", 0, 54.99),
                    models.CostModel("-vee soojendus", 3, "m3", 7.013, 21.04),
                    models.CostModel("Prügivedu", 60.90, "m2", 0.06, 3.65),
                    models.CostModel("-küte", 60.90, "m2", 0.996, 60.66),
                    models.CostModel("Avariivalve", 60.90, "m2", 0.032, 1.95),
                    models.CostModel("Vesi, kan.", 6, "m3", 2.08, 12.48),
                    models.CostModel("Haldus", 60.90, "m2", 0.146, 8.89),
                    models.CostModel("Üldelekter", 14.28, "/kWh", 0.122, 1.74),
                    models.CostModel("Hooldus", 60.90, "m2", 0.23, 14.01),
                    models.CostModel("Üldtarbevesi", 60.90, "m2", 0.015, 0.91),
                    models.CostModel("Koristus", 60.90, "m2", 0.115, 7),
                    models.CostModel("Remondireserv", 60.90, "m2", 0.32, 19.49),
                    )

# second pdf which is not an invoice
TEST_UNKNOWN_PDF_FILENAME = "test/resources/unknown_test_invoice.pdf"
TEST_UNKNOWN_PDF_TYPE = "UNKNOWN"

# TEST_PARSER_NOT_IMPLEMENTED
TEST_FILENAME_FOR_TEST_PARSER_NOT_IMPLEMENTED = "test_parser_not_implemented"
TEST_KEYWORD_FOR_TEST_PARSER_NOT_IMPLEMENTED = TEST_FILENAME_FOR_TEST_PARSER_NOT_IMPLEMENTED.replace("_", "")
TEST_RELATIVE_FILENAME_FOR_TEST_PARSER_NOT_IMPLEMENTED = "test/resources/%s.pdf" % TEST_FILENAME_FOR_TEST_PARSER_NOT_IMPLEMENTED
