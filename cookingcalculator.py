'''
COOKING CALCULATOR

This code develops a program, using If/Else + Range, that, based on the temperature of the steak (in Fahrenheit), returns the cooking point.

     -> the user must enter the temperature of the steak.

                Temperatures

                120°F  Rare
                130°F  Medium rare
                140°F  Medium
                150°F  Medium well
                160°F  Well done
'''

temp2 = int(input('What is the temperature of the steak:'))


if temp2 < 120:
    print('Your steak need to cook for a few more minutes')
elif temp2 in range(120, 129):
    print('Rare')
elif temp2 in range(130, 139): 
    print('Medium rare') 
elif temp2 in range(140, 159):
    print('Medium well')
elif temp2 >= 160:
    print('Well done')