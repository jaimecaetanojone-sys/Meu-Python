num = int(input('Digite um numero: '))

# RESOLUCAO DO PROFESSOR GUSTAVO GUANABARA
        #Parte 01

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o numero {}'. format(num))
print('Unidade: {}'. format(u))
print('Dezena: {}'. format(d))
print('Centena: {}'. format(c))
print('Milhar: {}'. format (m))



#Distribuicao do algarismos

#print('Unidade: ', distribuicao[3])
#print('Dezena: ', distribuicao[2])
#print('Centena: ', distribuicao[1])
#print('Milhar: ', distribuicao[0])

#rint(distribuicao)

