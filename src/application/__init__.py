
from pdfminer import pdfparser, pdfdocument
import datetime
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
import StringIO
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams

def openPdf(fileDescriptor):
    parser = pdfparser.PDFParser(fileDescriptor)
    return pdfdocument.PDFDocument(parser)

def getPdfPages(fileDescriptor):
    pages = []
    for page in PDFPage.get_pages(fileDescriptor, set()):
        pages.append(page)
    return pages

def getPdfAsText(pdfPages = None, fileDescriptor = None):
    if pdfPages is None and fileDescriptor is not None:
        pdfPages = getPdfPages(fileDescriptor)

    resourceManager = PDFResourceManager()
    laparams = LAParams()
    laparams.all_texts = True
    laparams.detect_vertical = True

    try:
        outputStream = StringIO.StringIO()
        device = TextConverter(resourceManager, outputStream, laparams=laparams)
        intrepreter = PDFPageInterpreter(resourceManager, device)
        for pdfPage in pdfPages:
            intrepreter.process_page(pdfPage)
        return outputStream.getvalue()
    finally:
        device.close()
        outputStream.close()

def getPdfDateCreated(pdfDoc = None, fileDescriptor = None):
    if fileDescriptor is not None and pdfDoc is None:
        pdfDoc = openPdf(fileDescriptor)

    datetimeString = pdfDoc.info[0]["CreationDate"]
    dateString = datetimeString[2:10]

    return datetime.datetime.strptime(dateString, "%Y%m%d").date()
