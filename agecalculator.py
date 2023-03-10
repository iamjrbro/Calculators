'''
AGE CALCULATOR

This code develops a program that is able to calculate somebody's age by importing the Datetime Module and using Class.

    obs: age is not exact, because the only information that it's provided is the year of birth.
    obs2: the Datetime Module determines that the set up year used in the calculation is the year which we are in.
'''

from datetime import datetime

class Person:
   def __init__(self, name, last_name, birthdayear):
    self.name = name
    self.last_name = last_name
    self.birthdayear = birthdayear

    def personage(self):
        currentyear = datetime.now().year
        self.birthdayear = int(currentyear - self.birthdayear)
        return self.birthdayear


person1 = Person('Jesse', 'Rose', '1994')
person2 = Person('Cristal', 'MCallin', '1996')
person3 = Person('Abel', 'Machado', '2000')
person4 = Person('Sabrina', 'Delfante', '2002')

print(Person.personage(person1))
