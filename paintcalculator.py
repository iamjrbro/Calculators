'''
PAINT CALCULATOR

This code develops a calculator, using Functions, that calculates the amount of paint needed to paint a wall.

        -> the user must enter the paint's yield and the wall's informations (height and width).
'''


y = int(input('What is the yield of your paint can? :'))
height = int(input('What is the height of your wall? :'))
width = int(input('What is the width of your wall? :'))

def paint():
    area = height * width
    total = area / y
    print(f'You will need {total} cans of wall paint')

paint()