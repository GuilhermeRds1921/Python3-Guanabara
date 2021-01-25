sex = 's'
while sex != 'M' and sex != 'F':
    sex = str(input('Whats your gender? (f or m')).upper()
    if sex != 'M' and sex != 'F':
        print('This isnt a valid answer. ')

if sex =='M':
    print('Your Gender is Male')
else:
    print('Your Gender is Female')