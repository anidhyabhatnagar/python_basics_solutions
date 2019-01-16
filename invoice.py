# -*- coding: utf-8 -*-
"""
@author: Anidhya Bhatnagar
@description: This is the Invoice class created as per the question for the
              Classes Exercise Question.
@question: Create a class called Invoice that a hardware store might use to
           represent an invoice for an item sold at the store.

           An Invoice should include four pieces of information as instance
           variables—a partNumber, a partDescription, a quantity of the item
           being purchased and a price per item.

           Your class should have a constructor that initializes the four
           instance variables. Provide set and get methods for each instance
           variable.

           In addition, provide a method named getInvoiceAmount that calculates
           the invoice amount (i.e., multiplies the quantity by the price per
           item), then returns the amount as a float value.
             > If the quantity is not positive, it should be set to 0.
             > If the price per item is not positive, it should be set to 0.
           Write a test app named InvoiceTest that demonstrates class Invoice’s
           capabilities.
"""

class Invoice:
    def __init__(self):
        self.partNumber = ""
        self.partDescription = ""
        self.quantity = ""
        self.price = ""

    def setPartNumber(self, partNumber):
        self.partNumber = partNumber

    def setPartDescription(self, partDescription):
        self.partDescription = partDescription

    def setQuantity(self, quantity):
        if quantity < 0:
            self.quantity = 0
        else:
            self.quantity = quantity

    def setPrice(self, price):
        if price < 0:
            self.price = 0
        else:
            self.price = price

    def getPartNumber(self):
        return self.partNumber

    def getPartDescription(self):
        return self.partDescription

    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price

    def getInvoiceAmount(self):
        return self.quantity * self.price


