# in this file we will exploe the reusability of our custom functions
from exercises.bmi_function import bmi_calculator


input_weight =float(input("Enter your weight in kilograms: "))
input_height = float(input("Enter your height in meters: "))

Oliver_bmi = bmi_calculator(input_weight, input_height)

print(Oliver_bmi)