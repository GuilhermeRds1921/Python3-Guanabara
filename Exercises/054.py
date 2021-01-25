from datetime import date
date = date.today().year
a = 0
b = 0
for i in range(0,7):
    age = int(input('What year were you born? '))
    p = date - age
    if p >= 21:
        a += 1
    else:
        b += 1
print('{} are of age. '.format(a))
print('{} arent of age. '.format(b))