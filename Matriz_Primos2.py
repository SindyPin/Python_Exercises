# Peça para que o usuário digite um número inteiro maior do que 1.
# Se o número for maior do que 1, armazene esse valor em um vetor.
# Peça por um novo número e assim sucessivamente até que o usuário digite 0.
# Quando isso acontecer, pare de pedir por novos números.
# Mostre na tela quais dos números que ficaram salvos no vetor são primos.
# Para determiná-los, utilize uma função chamada determinar_primo


numero = int(input('Digite um número inteiro maior do que 1: '))
vetor = []
vetor_primos = []

for i in range(0, numero):
    if numero > 1:
        numero = int(input('Digite outro número inteiro maior do que 1: '))
        vetor.append(numero)
        i = i + 1
    else:
        break
vetor.append(numero)


def determinar_primo(vetor):
    for k in vetor:
        if k > 1:
            contador = 0
            for m in range(1, k+1):
                if k % m == 0:
                    contador = contador + 1
            if contador <= 2:
                vetor_primos.append(k)
    return vetor_primos


print('Os seguintes números são primos: ')
print(determinar_primo(vetor))
