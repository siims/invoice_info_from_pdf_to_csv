'''
Created on May 12, 2016

'''

import application.parsers as parsers

class ABHALDUS(parsers.BaseParser):

    def parse(self, text, toModel):
        rows = text.split("\n")
        rowsWithContent = filter(lambda x: x.strip() != "", rows)
        cleanedRows = map(lambda x: x.strip().lstrip(), rowsWithContent)
        toModel.title = cleanedRows[0]
