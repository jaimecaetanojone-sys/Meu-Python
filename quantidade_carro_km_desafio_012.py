km = float(input('Digite o espaco percorrido em (km): '))
dias = int(input('Digite o tempo de duracao em (dias): '))


#Formula para o calculo do preco a pagar em funcao do tempo por volta

print('\n Em {} Km percorridos em {} dias \n Preco a pagar em dias e de: R${:.2f} \n O preco a pagar por rodada e de: R${:.2f}'. format(km, dias, (60*dias), (0.15*km) ))