'''
AGE CALCULATOR WITH INPUT

This code develops a program that calculates the user's age when they enter their year of birth.

    obs: age is not exact, because the only information that it's provided is the year of birth.
    obs2: the year used in the calculation is 2023, needing to be changed if you want to use other year.
'''

birth_year = input('When were you born?: ')
age = 2023 - int(birth_year)
print(age)