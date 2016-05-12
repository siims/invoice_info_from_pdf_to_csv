'''
Created on May 11, 2016

'''

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
        self.costs = {}

def resetTypes():
    InvoiceModel.TYPES = [InvoiceModel.TYPE_UNKNOWN]
