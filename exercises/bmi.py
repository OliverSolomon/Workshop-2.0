# BMI calculator

height = input('\n\nEnter your height in meters: ')
weight = input('Enter your weight in kilograms: ')

converted_height = float(height) 
converted_weight = float(weight)

BMI = converted_weight / (converted_height * converted_height)

print('\n\n')

print('Your BMI is: ', BMI)

if BMI < 18.5:
    print('You are Underweight')
elif BMI >= 18.5 and BMI < 25:
    print('You are Normal')
elif BMI >= 25 and BMI < 30:
    print('You are Overweight')
elif BMI >= 30 and BMI < 35:
    print('You are Obese')