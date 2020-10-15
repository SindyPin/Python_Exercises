# Crie um algoritmo usando "for" que determine se um número é ou não primo.
# Lembre-se que os números primos são os números naturais (inteiros e positivos)
# que somente podem ser divididos por 1 ou por ele mesmo.
# Lembrar que o 0 e o 1 não são números primos

try:
    n = int(input('Digite um número inteiro: '))
    if n < 0:
        print('Erro de digitação.', n, ' NÃO é um número inteiro. Digite novamente um número inteiro.')
    elif 0 <= n < 2:
        print('Embora', n, 'seja um número inteiro,', n, 'não é um número primo')
    else:
        for i in range(2, n+1):
            if n == 2:
                print(n, 'é um número primo')
            elif n % i == 0:
                print(n, 'NÃO é um número primo')
                break
            else:
                print(n, 'é um número primo')
                break

except ValueError as error:
    print('Erro de digitação. Digite novamente um número inteiro.')
    print('Tipo de erro:', error)
