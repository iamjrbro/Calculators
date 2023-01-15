'''
ECOMMERCE CALCULATOR

This code develops a program, using the While Loop Condition, that is able to calculate the commission that an ecommerce website charges to sell another person's product.

    -> in this example, the hypothetical ecommerce has a 10% commission on top of the price of the product, if it has a value above $20.
'''

value = int(input('Please, type your product value:'))

while value > 20:
    value = (value * 0.10 + value)
    print(f'Your products final price will be ${value}')
    break
