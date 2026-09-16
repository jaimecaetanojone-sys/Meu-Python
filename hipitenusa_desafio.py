# MINHA RESOLUCAO
import math

oposto = float(input('Cateto Oposto (Digite): '))
adjacente = float(input('Cateto adjacente (Digite): '))

#Formula para o calculo da Hipotenusa 
hipotenusa = math.sqrt((oposto)**2 + (adjacente)**2)


print('\n Com o cateto oposto dado de {} m \n Com o cateto adjacente dado de {} m \n A hipotenusa do triangulo retangulo sera de: {} m'. format (oposto, adjacente, math.ceil(hipotenusa)))

# RESOLUCAO 01 DO PROFESSOR GUSTAVO GUANABARA 

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

hi = (co**2 + ca**2)**(1/2)
print('\n A hipotenusa vai medir: {}'. format(math.ceil(hi)))

# RESOLUCAO 02 COM IMPORTACAO

co = float(input("\n Comprimento do cateto oposto: "))
ca = float(input("\n Comprimento do cateto adjacente: "))

hip = math.hypot(ca, co)
print('A hipotenusa vai medir: {}'. format(math.ceil(hip)))
