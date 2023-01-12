'''
BMI'S CALCULATOR (Body Mass Index)

This code develops a BMI'S Calculator using the If/Else Condition.

    -> the user must enter the following informations: 
        1. Height (in centimeters)
        2. Weight

The calculation is performed as follows:    

    BMI = WEIGHT / (HEIGHT*HEIGHT)

    less than 18,5         =   underweight
    between 18,5 and 24,9  =   normal
    between 25,0 and 29,9  =   overweight
    between 30,0 and 39,9  =   obesity
    more than 40,0         =   severe obesity
'''

height = float(input('What is your height (in cm?):'))
weight = float(input('What is your weight?:'))

imc = weight / (height/100)**2

if imc < 18.5:
    print('undernourishment')
elif imc >= 18.5 and imc < 24.9:
    print('normal')
elif imc >= 25.0 and imc < 29.9:
    print('overweight')
elif imc >= 30.0 and imc < 39.9:
    print('obesity')
elif imc >= 40.0:
    print('severe obesity')  