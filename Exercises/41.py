from datetime import date
date = date.today().year

birthday = int(input('When is you birthday? '))
age = date - int(birthday)
if age <=9:
    print('You are Mirim ')
elif age > 9 and age <=14:
    print('You are Infantil ')
elif age >14 and age <= 19:
    print('You are Junior ')
elif age >19 and age <=25:
    print('You are Senior ')
else:
    print('You are Master')