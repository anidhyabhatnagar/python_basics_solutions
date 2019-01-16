# -*- coding: utf-8 -*-
"""
@author: Anidhya Bhatnagar
@description: This is the employee class created as per the question for the
              Classes Exercise Question.
@question: Create a class called Employee that includes three instance
           variables — a firstname (type String), a lastname (type String) and
           a monthly salary (float). Provide a constructor that initializes
           the three instance variables. Provide set and get methods for
           each instance variable. If the monthly salary is not positive, do
           not set its value. Create a method raiseSalary which raises the
           salary of the employee by 10%. Also create a method getAnnualSalary
           which returns the employee's annual salary.

           Write a test app named EmployeeTest that demonstrates class
           Employee’s capabilities.

           Create two Employee objects and display each object’s yearly salary.
           Then give each Employee a 10% raise and display each Employee’s
           yearly salary again.
"""

class Employee:
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.salary = ""

    def setFirstName(self, firstname):
        self.firstname = firstname

    def setLastName(self, lastname):
        self.lastname = lastname

    def setSalary(self, salary):
        try:
            if int(salary) < 0:
                print("Could not set due to Negative Salary.")
                return False
            else:
                self.salary = int(salary)
                return True
        except ValueError as ve:
            self.salary = 0
            print("Error: ", ve)
            return False

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname

    def getSalary(self):
        return self.salary

    def getAnnualSalary(self):
        return self.salary * 12

    def raiseSalary(self):
        self.salary += (self.salary * 10)/100
