# This is a function to calculate the bmi

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    print(bmi)

    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return("It's not okay")
    
