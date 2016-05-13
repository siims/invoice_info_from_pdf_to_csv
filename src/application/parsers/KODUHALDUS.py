#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
Created on May 13, 2016

'''

import application.models.CostModel as models

class KODUHALDUS():

    # keywords in same sequence as in CostModel
    COST_KEYWORDS = ["Teenus", "Summa", "Kogus", "Tariif"]

    COST_HEADERS = [
                    "Haldus",
                    "Majanduskulud",
                    "Remondifond",
                    "Tehnohooldus",
                    "Gaas",
                    "Küte",
                    "Prügivedu",
                    "Vee soojendamine",
                    "Vesi ja kanalisatsioon",
                    "Üldelekter",
                    "Üldvesi",
                    ]

    REMOVE_ROWS_STARTING_WITH = ["Mõõdetud teenused", "Püsiteenused", "Arve koostas:", "Viimati laekunud:"]

    START_ROW_MARKER_INCLUDING = "Teenus"
    END_ROW_MARKER_EXCLUDING = "Püsiteenused kokku:"

    def parse(self, text, toModel):
        rows = text.split("\n")
        rowsWithContent = filter(lambda x: x.strip() != "", rows)

        cleanedRows = []
        considerRow = False
        for row in rowsWithContent:
            if row.startswith(self.START_ROW_MARKER_INCLUDING):
                considerRow = True
            elif row.startswith(self.END_ROW_MARKER_EXCLUDING):
                considerRow = False

            if considerRow:
                addRow = True
                for remove_row_keyword in self.REMOVE_ROWS_STARTING_WITH:
                    if row.startswith(remove_row_keyword):
                        addRow = False

                if addRow:
                    cleanedRows.append(row)


        cleanedRows = filter(lambda x: x.strip() != "", cleanedRows)
        cleanedRows = map(lambda x: x.strip().lstrip(), cleanedRows)
        cleanedRows = map(lambda x: x.replace(",", "."), cleanedRows)
        toModel.title = cleanedRows[0]
        toModel.costs = self._parseCosts(cleanedRows)


    def _parseCosts(self, cleanedRows):
        numEntries = self._calcNumEntries(cleanedRows)

        costs = []
        for i in range(len(self.COST_HEADERS)):
            costs.append([self.COST_HEADERS[i]])

        for costKeyword in self.COST_KEYWORDS:
            if costKeyword is "Teenus":
                continue

            index = cleanedRows.index(costKeyword)
            if costKeyword is "Summa":  # remove sum subtotal
                cleanedRows.pop(index + 5)

            if numEntries == 9:
                cleanedRows.insert(index + 8, "")
                cleanedRows.insert(index + 8, "")


            for i in range(index + 1, index + len(self.COST_HEADERS) + 1):
                if costKeyword is "Tariif":
                    pair = cleanedRows[i].split()
                    if len(pair) == 0:
                        costs[i - index - 1].append("")
                        costs[i - index - 1].append(0)
                    else:
                        costs[i - index - 1].append(pair[1])
                        costs[i - index - 1].append(pair[0])
                elif costKeyword is "Kogus":
                    pair = cleanedRows[i].split()
                    if len(pair) == 0:
                        costs[i - index - 1].append(0)
                    else:
                        costs[i - index - 1].append(pair[0])
                else:
                    if cleanedRows[i] == "":
                        costs[i - index - 1].append(0)
                    else:
                        costs[i - index - 1].append(cleanedRows[i])

        costModels = []
        for i in range(len(self.COST_HEADERS)):
            costModels.append(models.CostModel(costs[i]))

        return costModels

    def _calcNumEntries(self, cleanedRows):
        for costHeader in self.COST_HEADERS:
            if costHeader not in cleanedRows:
                return 9  # water heating and sewage is left out
        return 11
