# Sajjad Abdirahim Gedow    Reg No: SCT211-0065/2022

# Assignment 2 Part B Control Flow - BMI Calculator


height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))


bmi = weight / (height * height)


print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
else:
    print("You are overweight.")
