velocidade = float(input('Digite a velocidade do carro: '))

#Formulas para o calculo da velocidade, multa e do cambio

multa = velocidade*7
cambio = 11.05*multa

if velocidade >= 80:
    print('Carro motorista, voce foi multado, por estar acima da velocidada, MAU NOTORISTA!')
    print('Sua multa e de: R${:.2f}'. format(multa))
    print('Em Mocambique a multa seria de {:.2f}MZN'. format(cambio))
else:
    print('Voce esta num bom ritmo de velocidade, BOM MOTORISTA!')