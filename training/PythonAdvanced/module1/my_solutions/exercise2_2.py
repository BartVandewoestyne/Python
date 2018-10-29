# My solution for exercise 2.2

from collections import namedtuple
import csv
import sys

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

for emp in [EmployeeRecord(*columns) for columns in csv.reader(open("employees.csv", "rb"))]:
    print(emp.name, emp.title)