# Crie um algoritmo usando "while" que determine se um número é ou não primo.
# Lembre-se que os números primos são os números naturais (inteiros e positivos)
# que somente podem ser divididos por 1 ou por ele mesmo.

try:
    n = int(input('Digite um número inteiro: '))
    if n < 0:
        print('Erro de digitação.', n, ' NÃO é um nuúmero inteiro. Digite novamente um número inteiro.')
    elif 0 <= n < 2:
        print('Embora', n, 'seja um nuúmero inteiro,', n, 'não é um número primo')
    else:
        i = 2
        while n >= i:
            if n % i == 0:
                print(n, 'NÃO é um número primo')
                i = i + 1
                break
            else:
                print(n, 'é um número primo')

except ValueError as error:
    print('Erro de digitação. Tente digitar novamente um número inteiro.')
    print('Tipo de erro:', error)
