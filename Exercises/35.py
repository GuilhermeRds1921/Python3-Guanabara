a= float(input("Digite a Primeira Reta: "))
b= float(input("Digite a Segunda Reta: "))
c= float(input("Digite a Terceira Reta: "))
if a < b:
    ax = a
    a = c
    c = ax
if b<c:
    ax = b
    b = c
    c =ax
if a < b:
    ax = a
    a = c
    c = ax
if a<b+c:
    print("Pode formar um Triangulo ")
else:
    print("Nao pode formar um Triangulo ")