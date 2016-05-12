'''
Created on May 11, 2016

'''

import application
import application.models.InvoiceModel as models
import glob

class PdfInvoiceParser(object):

    def __init__(self, pdfPage, pdfDoc):
        self._rawText = application.getPdfAsText(pdfPages=[pdfPage])
        self._pdfDoc = pdfDoc

        self.readInInvoiceTypes()


    def parse(self):
        model = models.InvoiceModel()

        self._parseMetadata(model)
        self._parseModelByType(model)

        return model

    def readInInvoiceTypes(self, path_to_parser_modules="./application/parsers/"):
        models.resetTypes()

        for file in glob.glob(path_to_parser_modules + "[a-z|A-Z|0-9]*.py"):
            moduleName = file.strip(path_to_parser_modules).strip(".py")
            models.InvoiceModel.TYPES.append(moduleName)

    def _parseModelByType(self, model):
        if model.type == "ABHALDUS":
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
        for pdfType in models.InvoiceModel.TYPES:
            if pdfType.lower() in self._rawText or pdfType.upper() in self._rawText:
                return pdfType
        return models.InvoiceModel.TYPE_UNKNOWN

