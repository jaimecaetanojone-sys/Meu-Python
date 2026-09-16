#MINHA RESOLUCAO

import math

angulo = int(input('Angulo: '))

#Formula para o calculo do seno em funcao do angulo
seno = math.sin(angulo)
print ('O seno do angulo {} e de: {}'. format(angulo, math.ceil(seno)))

#Formula para o calculo do cosseno em funcao do angulo
cosseno = math.cos(angulo)
print('O cosseno do angulo {} e de: {}'. format(angulo, math.ceil(cosseno)))

#Formula para o calculo da tangente em funcao do angulo
tangente = math.tan(angulo)
print('A tangente do angulo {} e de: {}'. format(angulo, math.ceil(tangente)))

#RESOLUCAO DO PROFESSOR GUSTAVO GUANABARA

from math import radians, sin, cos, tan, ceil

angulos = float(input('Digite o angulo que voce deseja: '))
sen = sin(radians(angulos))
print("o seno do angulo e de: {}". format(ceil(sen)))

cos = cos(radians(angulos))
print('O cosseno do angulo e de: {}'. format(ceil(cos)))

tan = tan(radians(angulos))
print ('A tangente do angulo sera de: {}'. format(ceil(tan)))