#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import application.models.CostModel as models

# first test pdf from abhaldus
TEST_PDF_FILENAME = "test/resources/abhaldus_test_invoice.pdf"
TEST_PDF_DATE_CREATED_STRING = "2016-04-08"
TEST_PDF_DATE_CREATED = datetime.datetime.strptime(TEST_PDF_DATE_CREATED_STRING, "%Y-%m-%d").date()
TEST_PDF_TITLE = "A R V E  Nr. 4.16/R12-12"
TEST_PDF_TYPE = "ABHALDUS"
TEST_PDF_NUM_PAGES = 1
TEST_PDF_COSTS = set([models.CostModel("Soojusenergia", 81.70, 0, "/MWh", 59.42),
                    models.CostModel("Majandamiskulud", 54.99, 0, "", 0),
                    models.CostModel("-vee soojendus", 21.04, 3, "m3", 7.013),
                    models.CostModel("Prügivedu", 3.65, 60.90, "m2", 0.06),
                    models.CostModel("-küte", 60.66, 60.90, "m2", 0.996),
                    models.CostModel("Avariivalve", 1.95, 60.90, "m2", 0.032),
                    models.CostModel("Vesi, kan.", 12.48, 6, "m3", 2.08),
                    models.CostModel("Haldus", 8.89, 60.90, "m2", 0.146),
                    models.CostModel("Üldelekter", 1.74, 14.28, "/kWh", 0.122),
                    models.CostModel("Hooldus", 14.01, 60.90, "m2", 0.23),
                    models.CostModel("Üldtarbevesi", 0.91, 60.90, "m2", 0.015),
                    models.CostModel("Koristus", 7, 60.90, "m2", 0.115),
                    models.CostModel("Remondireserv", 19.49, 60.90, "m2", 0.32)
                    ])

# second pdf which is not an invoice
TEST_UNKNOWN_PDF_FILENAME = "test/resources/unknown_test_invoice.pdf"
TEST_UNKNOWN_PDF_TYPE = "UNKNOWN"

# TEST_PARSER_NOT_IMPLEMENTED
TEST_FILENAME_FOR_TEST_PARSER_NOT_IMPLEMENTED = "test_parser_not_implemented"
TEST_KEYWORD_FOR_TEST_PARSER_NOT_IMPLEMENTED = TEST_FILENAME_FOR_TEST_PARSER_NOT_IMPLEMENTED.replace("_", "")
TEST_RELATIVE_FILENAME_FOR_TEST_PARSER_NOT_IMPLEMENTED = "test/resources/%s.pdf" % TEST_FILENAME_FOR_TEST_PARSER_NOT_IMPLEMENTED
