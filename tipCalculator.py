# Sajjad Abdirahim Gedow    Reg No: SCT211-0065/2022

# Assignment 2 PART A Data Type Recap - Tip Calculator

# Get user inputs
total_bill = float(input("Enter the total bill amount: "))
tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
num_people = int(input("Enter the number of people splitting the bill: "))

# Calculate the tip amount
tip_amount = total_bill * (tip_percentage / 100)

# Calculate the total amount per person
total_per_person = (total_bill + tip_amount) / num_people

# Return the total amount per person rounded to two decimal points
total = round(total_per_person, 2)

# Calculate and display the result
print(f"Each person should pay: Ksh. {total}")
