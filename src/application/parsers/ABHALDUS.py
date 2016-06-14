#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on May 12, 2016
'''

import application.parsers as parsers
import application.models.CostModel as models
import re

class ABHALDUS(parsers.BaseParser):

    def parse(self, text, toModel):
        rows = text.split("\n")
        rowsWithContent = filter(lambda x: x.strip() != "", rows)
        cleanedRows = map(lambda x: x.strip().lstrip(), rowsWithContent)
        toModel.title = cleanedRows[0]
        toModel.costs = self._parseCosts(cleanedRows)

    def _parseCosts(self, rows):

        startMarkerInclusive = "-vee soojendus"
        includeRowsPattern = "\w|-"
        endMarkerInclusive = "Remondireserv"

        prog = re.compile(includeRowsPattern, re.UNICODE)
        started = False

        costs = []

        for row in rows:
            row = row.replace(":", "")
            if row.startswith(startMarkerInclusive):
                started = True

            if started and prog.match(row):
                elements = row.split()
                if len(elements) == 1:  # TODO remove this when re is filtering single bars "|"
                    continue
                if len(elements) == 6:  # two word name
                    elements[0] += " " + elements[1]
                    elements.pop(1)

                elements.insert(1, elements.pop())
                if len(elements) == 3:  # might be a case when amount and unitcost is missing
                    elements.insert(2, 0.0)
                newCost = models.CostModel(elements)

                costs.append(newCost)

            if row.startswith(endMarkerInclusive):
                break
        return costs
