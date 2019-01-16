# -*- coding: utf-8 -*-
"""
@author: Anidhya Bhatnagar
@description: This is a test program which tests for the functionality of
              employee class.
"""

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee()
        self.employee.setFirstName("Vivek")
        self.employee.setLastName("Chouhan")
        self.employee.setSalary(50000)

    def test_setFirstName(self):
        self.assertEqual(self.employee.firstname, "Vivek",
                         "Could not set First Name.")

    def test_setLastName(self):
        self.assertEqual(self.employee.lastname, "Chouhan",
                         "Could not set Last Name.")

    def test_setSalary(self):
        self.assertEqual(self.employee.salary, 50000,
                         "Could not set Salary.")
        self.assertFalse(self.employee.setSalary(-25000),
                         "Negative Salary Error, should return False")

    def test_getFirstName(self):
        self.assertEqual(self.employee.getFirstName(), "Vivek",
                         "Error in getting First Name.")

    def test_getLastName(self):
        self.assertEqual(self.employee.getLastName(), "Chouhan",
                         "Error in getting Last Name.")

    def test_getSalary(self):
        self.assertEqual(self.employee.getSalary(), 50000,
                         "Error in getting Salary.")

    def test_raiseSalary(self):
        self.employee.raiseSalary()
        self.assertEqual(self.employee.getSalary(), 55000,
                         "Salary could not be raised correctly.")

    def test_showAnnualSalary(self):
        self.assertEqual(self.employee.getAnnualSalary(), 600000,
                         "Could not get correct Annual Salary.")


if __name__ == '__main__':
    unittest.main()
