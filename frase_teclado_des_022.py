frase = str(input('Digite uma frase: ')).upper().strip()

#vezes que a letra A repete numa frase

letras = frase.count('A')
print('O numero de vezes que a letra (a) aparece no seu enunciado: ')
print(letras)

#Posicao que a letra (A) aparece no enunciado

repeticao = frase.find('A')+1
print(repeticao)

#ultima posicao que a letra (A) aparece no enunciado
print('A ultima letra A apareceu na posicao {}'. format (frase.rfind('A')+1))


