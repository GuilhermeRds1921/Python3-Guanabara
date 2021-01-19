# Faça um programa que leia um ângulo qualquer e
# morte na tela o valor do seno, cosseno e
# tangente desse ângulo.

import math
angl = float(input("Informe o Angulo: "))
sen = math.sin(math.radians(angl))
cos = math.cos(math.radians(angl))
tan = math.tan(math.radians(angl))
print("O Seno desse angulo eh {:.2f}".format(sen))
print("O Cosseno desse angulo eh {:.2f}".format(cos))
print("A Tangente desse angulo eh {:.2f}".format(tan))

