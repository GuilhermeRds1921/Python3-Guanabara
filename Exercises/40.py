num1 = float(input('Write the First Grade: '))
num2 = float(input('Write the Second Grade: '))
average = float(num1+num2)/2
if average < 5:
    print('You Fail ')
elif average > 5 and average < 7:
    print('You are in Recovery')
else:
    print('Congratulations! You Passed')