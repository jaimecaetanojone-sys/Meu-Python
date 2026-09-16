nome = input('Digite o nome do aluno: ')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#Formula de Media dos alunos

print('A media do aluno {} foi de {:.2f}, tendo em conta primeira nota {} e a segunda nota {} '. format(nome, (n1+n2)/2, n1, n2))