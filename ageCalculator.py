# Sajjad Abdirahim Gedow    Reg No: SCT211-0065/2022

# Assignment 2 PART A Data Type Recap - Age Calculator

import datetime

YearOfBirth = int(input("Enter the year of birth: "))
CurrentYear = datetime.datetime.now().year
ageInYears = CurrentYear - YearOfBirth

if ageInYears < 0:
    print("Invalid year of birth. Please enter a valid year.")
else:
    
    ageinMonths = ageInYears * 12

    daysinaMonth = 30.44 
    daysinYear = 365.24 
    ageInDays = ageInYears * daysinYear + ageinMonths * daysinaMonth
    
    print(f"Age in years: {ageInYears}")
    print(f"Age in months: {ageinMonths}")
    print(f"Age in days: {int(ageInDays)}")
