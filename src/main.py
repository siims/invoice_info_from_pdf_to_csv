#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on May 11, 2016

'''
from application import getPdfPages, openPdf, parsers

def parseInvoice(invoiceFileDescriptor):
    pdfPages = getPdfPages(fileDescriptor=invoiceFileDescriptor)
    pdfDoc = openPdf(invoiceFileDescriptor)

    invoiceParser = parsers.PdfInvoiceParser(pdfPage=pdfPages[0], pdfDoc=pdfDoc)
    invoice = invoiceParser.parse()

    return invoice

if __name__ == '__main__':
    try:
        pdf = open("/home/s/Downloads/R12-12.pdf", "r")
        invoice = parseInvoice(pdf)
        print invoice

    finally:
        pdf.close()
