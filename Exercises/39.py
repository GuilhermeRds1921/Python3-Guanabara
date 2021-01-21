year = int(input('Whats year were you born? '))
age = 2020 - int(year)
if age > 18:
    print('You already spent {} year of enlistment year '.format(age-18))
elif age == 18:
    print('This is the enlistment year ')
else:
    print('You still have {} years to the enlistment year '.format(18-age))