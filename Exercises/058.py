from random import randint
a = randint(0,10)
b = 11
count = 1
print('==== Guess the Number ====')
while b != a:
    b = int(input('Chose a Number: '))
    if b !=a:
        print('Wrong !')
        count += 1
print('You WIN !')
print('You had {} tries to win'.format(count))