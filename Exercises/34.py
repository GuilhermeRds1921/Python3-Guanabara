sal= float(input("Digite o seu Salario: "))
if sal>=1250:
    sal=sal+(sal*0.1)
else:
    sal=sal+(sal*0.15)
print("Seu novo salario e de {}".format(sal))