#

weight = float(input('Whats your weight? (kg)'))
height = float(input('How tall are you? (m)'))
imc = float(weight / (height ** 2 ))

print('The Imc is: {:.1f}'.format(imc))
if imc <= 18.5:
    print('You are underweight ')
elif imc > 18.5 and imc <= 25:
    print('Nice weight ')
elif imc > 25 and imc <= 30:
    print('You are above weight')
elif 30 < imc <= 40:
    print('Obesity')
else:
    print('Stop eating or you will die !')