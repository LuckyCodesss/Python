import random
y = random.randrange(12)
x = int(input('Your Answer : '))
if int(x) > y:
    print('wrong, your answer is more than')
elif int(x) < y:
    print('wrong, your answer is less than')
else : print('Your answer is correct')
