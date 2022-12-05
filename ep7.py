Height = int(input('Your Weight : '))
Weight = int(input('Your Height : '))
formula = (Weight/((Height/100)*2))
if formula <= 18.50:
    print('Underweight')
elif formula > 18.50:
    print('Normal')
elif formula > 23:
    print('Overweight Level 1')
elif formula > 25:
    print('Overweight Level 2')
else : print('Overweight Level 3')
