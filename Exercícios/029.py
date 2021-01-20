vel= int(input("Digite a velocidade do carro: "))
if vel<=80:
    print("Voce esta dentro do limite ")
else:
    print("Voce esta acima do limite ")
    vel=vel-80
    print("Tera que pagar R${} de multa ".format(vel*7))
