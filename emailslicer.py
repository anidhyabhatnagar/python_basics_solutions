# -*- coding: utf-8 -*-
"""
@author: Anidhya Bhatnagar
@description: This class provides the functionality required for the
              email slicer program.
"""
class EmailSlicer:
    def __init__(self, email=''):
        self.email = email

    def setEmail(self, email):
        if len(email.split('@')) < 2:
            return False
        else:
            self.email = email

    def getEmail(self):
        return self.email

    def getDomain(self):
        slices = self.email.split('@')
        return slices[1]

    def getUser(self):
        slices = self.email.split('@')
        return slices[0]
