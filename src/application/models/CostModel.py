'''
Created on May 12, 2016

'''

class CostModel():

    def __init__(self, name, total, amount=0, units="", unitCost=0):
        self.name = name
        self.amount = amount
        self.units = units
        self.unitCost = unitCost
        self.total = total

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.name == other.name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "%s,%.2f,%s,%.3f,%.2f" % (self.name, self.amount, self.units, self.unitCost, self.total)

    def __hash__(self):
        return hash(self.__repr__())
