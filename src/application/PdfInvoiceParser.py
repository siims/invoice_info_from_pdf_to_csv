'''
Created on May 11, 2016

'''

import application
import application.models.InvoiceModel as models


class PdfInvoiceParser(object):

    def __init__(self, pdfPage, pdfDoc):
        self._rawText = application.getPdfAsText(pdfPages=[pdfPage])
        self._pdfDoc = pdfDoc

    def parse(self):
        model = models.InvoiceModel()

        self._parseMetadata(model)
        self._parseModelByType(model)

        return model

    def _parseModelByType(self, model):
        if model.type == models.InvoiceModel.TYPES["ABHALDUS"]:
            rows = self._rawText.split("\n")
            rowsWithContent = filter(lambda x: x.strip() != "", rows)
            cleanedRows = map(lambda x: x.strip().lstrip(), rowsWithContent)
            model.title = cleanedRows[0]
        else:
            raise models.InvoiceModel.InvoiceUnknownException()

    def _parseMetadata(self, model):
        model.type = self._detectType()
        createdDate = application.getPdfDateCreated(pdfDoc=self._pdfDoc)
        model.year = createdDate.year
        model.month = createdDate.month

    def _detectType(self):
        for key, value in models.InvoiceModel.TYPES.iteritems():
            if key.lower() in self._rawText:
                return value
        return models.InvoiceModel.TYPES["UNKNOWN"]

