# Faça um programa que leia algo pelo teclado e mostre na tela 
# seu tipo primitivo e todas as infomações possíveis sobre ele.

valor = input('Variavel: ')
print('O tipo da variavel e: ',type(valor))
print('E feito de espacos: ', valor.isspace())
print('E numerico: ', valor.isnumeric())
print('E alfabetico: ', valor.isalpha())
print('E tudo maiusculo: ', valor.isupper())
print('E tudo minusculo: ', valor.islower())
print('E capitalizada: ', valor.istitle())
