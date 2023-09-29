# Sajjad Abdirahim Gedow    Reg No: SCT211-0065/2022

# Assignment 2 PART A Data Type Recap - Age Calculator

import datetime

def calculate_age(birth_year):
    today = datetime.date.today()
    age = today.year - birth_year

    if today.month < (birth_year + age) % 12 + 1:
        age -= 1

    months = today.month - ((birth_year + age) % 12 + 1)
    if months < 0:
        months += 12

    days = today.day - datetime.date(today.year - age, today.month - months, 1).day
    if days < 0:
        days += datetime.date(today.year - age, today.month - months, 1).day

    return age, months, days

birth_year = int(input("Enter your year of birth: "))
age, months, days = calculate_age(birth_year)

print(f"Your age is {age} years, {months} months, and {days} days.")