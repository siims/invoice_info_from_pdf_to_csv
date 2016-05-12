'''
Created on May 11, 2016

'''

import application
import application.models.InvoiceModel as models
import importlib

class ParserNotImplemented(NotImplementedError):
    pass

class BaseParser(object):
    def parse(self, text, toModel):
        raise ParserNotImplemented()

class PdfInvoiceParser():

    def __init__(self, pdfPage, pdfDoc):
        self._rawText = application.getPdfAsText(pdfPages=[pdfPage])
        self._pdfDoc = pdfDoc

        self.readInInvoiceTypes()


    def parse(self):
        model = models.InvoiceModel()

        self._parseMetadata(model)
        self._parseModelByType(model)

        return model

    def readInInvoiceTypes(self):
        models.resetTypes()

    def _parseModelByType(self, model):
        if model.type == models.InvoiceModel.TYPE_UNKNOWN:
            raise models.InvoiceModel.InvoiceUnknownException()

        module = importlib.import_module("." + model.type, package="application.parsers")
        pdfParserClass = getattr(module, model.type)
        pdfParser = pdfParserClass()
        pdfParser.parse(self._rawText, model)

    def _parseMetadata(self, model):
        model.type = self._detectType()
        createdDate = application.getPdfDateCreated(pdfDoc=self._pdfDoc)
        model.year = createdDate.year
        model.month = createdDate.month

    def _detectType(self):
        for pdfType in models.InvoiceModel.TYPES:
            if pdfType.lower() in self._rawText or pdfType.upper() in self._rawText:
                return pdfType
        return models.InvoiceModel.TYPE_UNKNOWN
