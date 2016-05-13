#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on May 13, 2016

'''
import unittest
from application.models import InvoiceModel, CostModel

class ModelTests(unittest.TestCase):

    def setUp(self):
        self.invoice = InvoiceModel.InvoiceModel()
        self.invoice.title = "TestInvoice"
        self.invoice.year = 2000
        self.invoice.month = 2
        self.invoice.costs = [
                              CostModel.CostModel("A", 21),
                              CostModel.CostModel("Öžäõü utf8", 22),
                              CostModel.CostModel("Öžäõü utf8", 20, 123.1341, "\öäõü", 999),
                              ]

    def testCostsPrinting(self):
        expectedPrint = """TestInvoice 2/2000
A,0.00,,0.000,21.00
Öžäõü utf8,0.00,,0.000,22.00
Öžäõü utf8,123.13,\öäõü,999.000,20.00
"""
        result = self._obtainPrintedOutput(self.invoice)

        self.assertEqual(expectedPrint, result)

    def _obtainPrintedOutput(self, obj):
        import sys
        from StringIO import StringIO

        # setup the environment
        backup = sys.stdout

        sys.stdout = StringIO()  # capture output
        print self.invoice
        out = sys.stdout.getvalue()  # release output

        sys.stdout.close()  # close the stream
        sys.stdout = backup  # restore original stdout
        return out


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
