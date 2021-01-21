ano= int(input("Digite o Ano: "))
if ano%4==0:
    ano=ano
    if ano%100!=0:
        print("{} é Bissexto ".format(ano))
    elif ano%400==0:
        print("{} é Bissexto ".format(ano))
    else:
        print("Nao e Bissexto ")
else:
    print("Nao e Bissexto ")