dist= float(input("Digite a distancia da viajem em KM: "))
if dist<=200:
    print("Custara R${}".format(dist*0.5))
else:
    print("Custara R${}".format(dist*0.45))