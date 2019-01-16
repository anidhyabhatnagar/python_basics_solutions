# -*- coding: utf-8 -*-
"""
@author: Anidhya Bhatnagar
@description: This is a test program which tests for the functionality of
              Invoice class.
"""

import unittest
from invoice import Invoice


class TestInvoice(unittest.TestCase):
    def setUp(self):
        self.invoice = Invoice()
        self.invoice.setPartNumber("WB452W")
        self.invoice.setPartDescription("Large White Wash Basin")
        self.invoice.setQuantity(2)
        self.invoice.setPrice(25.50)

    def test_setPartNumber(self):
        self.assertEqual(self.invoice.partNumber, "WB452W",
                         "Unable set Part Number.")

    def test_setPartDescription(self):
        self.assertEqual(self.invoice.partDescription,
                         "Large White Wash Basin",
                         "Unable to set Part Description.")

    def test_setQuantity(self):
        self.assertEqual(self.invoice.quantity, 2,
                         "Unable to set Quantity.")
        self.invoice.setQuantity(-2)
        self.assertEqual(self.invoice.quantity, 0,
                         "Negative Quantity Error, should be set to Zero.")

    def test_setPrice(self):
        self.assertEqual(self.invoice.price, 25.50,
                         "Unable to set Price.")
        self.invoice.setPrice(-5)
        self.assertEqual(self.invoice.price, 0,
                         "Negative Price Error, should be set to Zero.")

    def test_getPartNumber(self):
        self.assertEqual(self.invoice.getPartNumber(), "WB452W",
                         "Unable get correct Part Number.")

    def test_getPartDescription(self):
        self.assertEqual(self.invoice.getPartDescription(),
                         "Large White Wash Basin",
                         "Unable to get correct Part Description.")

    def test_getQuantity(self):
        self.assertEqual(self.invoice.getQuantity(), 2,
                         "Unable to get correct Quantity.")

    def test_getPrice(self):
        self.assertEqual(self.invoice.getPrice(), 25.50,
                         "Unable to get correct Price.")

    def test_getInvoiceAmount(self):
        self.assertEqual(self.invoice.getInvoiceAmount(), 51,
                         "Unable to get correct Invoice Amount.")


if __name__ == '__main__':
    unittest.main()
