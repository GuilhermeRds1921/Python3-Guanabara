from random import randint
b= randint(0,5)
a= int(input("Escreva um Numero de 0 a 5: "))
if a==b:
    print("Voce acertou ")
else:
    print("Voce errou ")
print("O numero era {}".format(b))