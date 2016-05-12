'''
Created on May 11, 2016

'''

import glob

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

def resetTypes():
    InvoiceModel.TYPES = [InvoiceModel.TYPE_UNKNOWN]
    path_to_parser_modules = "./application/parsers/"

    for invoiceParserDefinition in glob.glob(path_to_parser_modules + "[a-z|A-Z|0-9]*.py"):
        moduleName = invoiceParserDefinition.replace(path_to_parser_modules, "").replace(".py", "")
        InvoiceModel.TYPES.append(moduleName)
