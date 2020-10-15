# Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 20 posições.
# Crie uma função que receba o vetor preenchido e substitua todas as ocorrências de valores negativos por 0,
# as de valores menores do que 10 por 1 e as demais por 2.

vetor = []

i = 0
for i in range(0, 5):
    numero = int(input('Digite um numero inteiro: '))
    vetor.append(numero)
    i += 1

print(vetor)

for j in range(len(vetor)):
    num = vetor[i]
    j += 1
    if num < 0:
        vetor[i] = 0
        j += 1
    elif 0 <= num <= 10:
        vetor[i] = 1
        j += 1
    else:
        vetor[i] = 2
        j += 1


print('O novo vetor é: ', vetor)
