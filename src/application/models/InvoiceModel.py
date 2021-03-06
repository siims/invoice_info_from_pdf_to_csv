#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on May 11, 2016

'''

import glob
from application.models import CostModel

class InvoiceModel():

    TYPE_UNKNOWN = "UNKNOWN"
    TYPES = [TYPE_UNKNOWN]

    class InvoiceUnknownException(Exception):
        pass

    def __init__(self):

        self.type = self.TYPE_UNKNOWN

        self.title = ""
        self.year = ""
        self.month = ""
        self.costs = []

    def __repr__(self):
        return "%s %d/%d" % (self.title, self.month, self.year) + "\n" + \
            CostModel.CostModel.getHeader() + "\n" + \
            "\n".join(["%s" % cost for cost in self.costs])

def resetTypes():
    InvoiceModel.TYPES = [InvoiceModel.TYPE_UNKNOWN]
    path_to_parser_modules = "./application/parsers/"

    for invoiceParserDefinition in glob.glob(path_to_parser_modules + "[a-z|A-Z|0-9]*.py"):
        moduleName = invoiceParserDefinition.replace(path_to_parser_modules, "").replace(".py", "")
        InvoiceModel.TYPES.append(moduleName)
