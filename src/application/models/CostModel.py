#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on May 12, 2016

'''

class CostModel():

    def __init__(self, name="", total=0., amount=0., units="", unitCost=0.):
        if isinstance(name, list):
            inputLst = name
            if len(inputLst) > 0: self.name = inputLst[0]
            if len(inputLst) > 1: self.total = float(inputLst[1])
            if len(inputLst) > 2: self.amount = float(inputLst[2])
            if len(inputLst) > 3: self.units = inputLst[3]
            if len(inputLst) > 4: self.unitCost = float(inputLst[4])
        else:
            self.name = name
            self.amount = float(amount)
            self.units = units
            self.unitCost = float(unitCost)
            self.total = float(total)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.name == other.name)

    @staticmethod
    def getHeader():
        return "Type,Amount,Units,Unit Cost,Total"

    def __repr__(self):
        return "%s,%.2f,%s,%.3f,%.2f" % (self.name, self.amount, self.units, self.unitCost, self.total)
