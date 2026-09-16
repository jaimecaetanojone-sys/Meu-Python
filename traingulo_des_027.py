#MINHA RESOLUCAO

lado1 = int(input('Digite o lado 1: '))
lado2 = int(input('Digite o lado 2: '))
lado3 = int(input('Digite o lado 3: '))

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado2 + lado1):
    print('E um triangulo')
else:
    print('Nao e um triangulo')