from random import randint, choice

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
#RESOLUCAO DO PROFESSOR GUSTAVO GUANABARA

sorteios = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice (sorteios)
print('O Aluno escolhido e: {}'. format(escolhido))

#MINHA RESOLUCAO 

sorteio = randint(aluno1, aluno2, aluno3, aluno4)
print('O aluno escolhido foi: {}'.format(sorteio))

