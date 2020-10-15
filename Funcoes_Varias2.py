import random


# Função que retorna uma variável:


def potencia(a, b):
    pot = a ** b
    return pot


x = potencia(2, 3)
print(x)


# Função que retorna uma expressão:


def soma(x1, x2, x3):
    sum1 = x1 + x2 + x3
    return sum1


print(soma(3, 4, 5))


# Função que retorna várias coisas:


def soma_multiplicacao(num1, num2):
    sum2 = num1 + num2
    return sum2, num1 * num2


print(soma_multiplicacao(4, 4))


# Função que retorna NADA:


def lanca_dado():
    a = random.randint(1, 7)
    print(a)


lanca_dado()


# Função que retorna lista:


def soma(num2, *lista):
    soma_num = 0
    print(lista)
    for num in lista:
        soma_num += num
    return soma_num


k = (1, 2, 3, 4)
print(soma(1, 2, 3, 4, 5))


# Função Média:


def soma(*nums):
    soma_num = 0
    for j in nums:
        soma_num += j
    return soma_num


def media(p1, p2, p3, peso1=1, peso2=2, peso3=3):
    return (p1*peso1 + p2*peso2 + p3*peso3) / soma(peso1, peso2, peso3)


print(media(6, 7, 8))
