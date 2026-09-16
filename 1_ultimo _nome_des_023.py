nome = str(input ('Digite o seu nome: ')).strip()

primeiro = nome.split()

print('O primeiro nome: ', primeiro[0])
print('o ultimo nome: {}'. format(primeiro[len(primeiro)-1]))