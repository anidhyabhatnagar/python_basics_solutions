# -*- coding: utf-8 -*-
"""
@author: Anidhya Bhatnagar
@description: This is a test program which tests for the functionality of
              email slicer program.
"""

import unittest
from emailslicer import EmailSlicer


class TestEmailSlicer(unittest.TestCase):
    def setUp(self):
        self.emailSlicer = EmailSlicer()
        self.emailSlicer.setEmail("anidhya@gmail.com")

    def test_setEmail(self):
        self.assertEqual(self.emailSlicer.email,
                         "anidhya@gmail.com", "Email not set Properly")
        self.assertEqual(self.emailSlicer.setEmail("anidhyagmail.com"),
                         False, "Invalid Email Not Checked.")

    def test_getEmail(self):
        self.assertEqual(self.emailSlicer.getEmail(), "anidhya@gmail.com",
                         "Could not get email.")

    def test_getDomain(self):
        self.assertEqual(self.emailSlicer.getDomain(), "gmail.com",
                         "Could not get Domain from email.")

    def test_getUser(self):
        self.assertEqual(self.emailSlicer.getDomain(), "gmail.com",
                         "Could not get Domain from email.")


if __name__ == '__main__':
    unittest.main()
