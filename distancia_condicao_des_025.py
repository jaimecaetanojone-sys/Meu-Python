distancia = float(input('Informe a distancia: '))

valor = distancia*0.50
cambio = valor*11.40
especial = valor*0.45
cambioespecial = especial*11.40

if distancia <= 200:
    print('O valor a pagar em ate 200km de viagem e de: R${:.2f}'. format(valor))
    print('O valor a pagar em Mocambique sera: {:.2f}MZN'. format(cambio))
else:
    print('O Valor a pagar em mais de 200km e de: R${:.2f}'. format(especial))
    print('O valor a pagar em Mocambique e de: {:.2f}MZN'. format(cambioespecial))