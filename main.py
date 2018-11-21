#!/usr/bin/python3

from dayOfWeek import *

print("Enter future date in the following format: MM/DD/YYYY or MM/DD/YY: ")

enteredDate = input()
print(dayConverter(dayOfWeek(enteredDate)))
