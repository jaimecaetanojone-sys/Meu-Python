nome = str(input('Digite o seu nome: ')).strip()

santo = 'santo' in nome
print("O seu nome contem santo")
print(santo)

#RESOLUCAO DO PROFESSOR GUSTAVO GUANABARA

cid = str(input('Em que cidade voce nasceu? ')).strip()
print(cid[:5].upper() == 'Santo')