'''
This code develops a sale promotion for a product, using While Loop Condition, which will start with the sale price at $100 and will get $5 off every day. 

    -> the loop ends when the value reaches the $20 limit.
'''

value = 100
day = 0

while value > 20:
    day += 1
    print(f'At day {day} the product will be sold for ${value}')
    value -= 5