from math import trunc

#Forma de resolucao da parte da demonstracao da parte inteira de um determinado numero real

numero = float(input('Digite um numero: '))
print('A parte inteira de {} e: {}'. format(numero, trunc(numero)))

#Forma do professor Gustavo Guanabara
print ('O Valor digitado foi {} e a sua porcao inteira e {}'. format(numero, int(numero)))