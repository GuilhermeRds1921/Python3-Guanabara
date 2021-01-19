# Fça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.

valor = float(input("Digite o Preco de algo: "))
desc = float(valor-(valor * 0.05))
print("O valor com 5% de desconto eh: {:.2f}".format(desc))