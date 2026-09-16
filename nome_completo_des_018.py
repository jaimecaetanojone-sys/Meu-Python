nome = str(input ('Digite o seu nome completo: ')).strip()

#Letras maiusculas

maiusculas = nome.upper()
print (maiusculas)

#Letras minusculas

minusculas = nome.lower()
print(minusculas)

#Numero de letras
numero = len(nome) - nome.count(" ")
print (numero)

#primeiro nome e quantidade de letra

primeiro = nome.split()

print('Seu primeiro nome e: ', primeiro[0], ' e ele tem')

#RESOLUCAO DO PROFESSOR GUSATAVO GUANABARA

print('seu primeiro nome tem {} letras'. format(nome.find(' ')))

separa = nome.split()
print('seu primeiro nome e {} e ele tem {} letras'. format(separa[0], len(separa[0])))