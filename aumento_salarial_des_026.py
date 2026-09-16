salario = float(input('Informe o salario atual: R$'))

aumento1 = salario +  (salario*10/100)
aumento2 = salario + (salario*15/100)

if salario > 1250:
    print("O seu aumento salarial sera de 10% \n Seu novo salario com aumeto e de: {:.2f}". format(aumento1))
else:
    print ('O seu aumento salarial sera de 15% \n seu novo salario com aumento e de: {:.2f}'. format(aumento2))
