cost = float(input('Whats the house cost? '))
salary = float(input('How many is your salary? '))
year = float(input('For how many years do you will pay the house? '))
print('\n')

installment = float(cost/(year*12))

if installment>=(salary*0.3):
    print('You cant buy this house')
else:
    print('Congratilations! Thats your house now!')
    print('But you will pay R${:.2f} for month during {} years'.format(installment, year))