'''
Created on May 11, 2016

'''

class InvoiceModel():

    TYPES = {"UNKNOWN":0, "ABHALDUS":1, "KODUHALDUS":2} # TODO: read type keywords from application.parsers package

    class InvoiceUnknownException(Exception):
        pass

    def __init__(self):

        self.type = self.TYPES["UNKNOWN"]

        self.title = ""
        self.year = ""
        self.month = ""
        self.costs = {}

