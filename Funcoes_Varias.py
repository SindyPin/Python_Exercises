import math


def media(x, y):
    return (x + y) / 2


def perimetro(r):
    return 2 * math.pi * r


def is_par(x):
    return x % 2 == 0


print(is_par(5))  # mostra "False" na tela
print(is_par(6))  # mostra "True" na tela


def factorial_max(a, b, c, d):
    fat = 1
    maximo = max(a, b, c, d)
    if maximo <= 0:
        return fat
    while maximo >= 1:
        fat = fat * maximo
        maximo = maximo - 1
    return fat


print(factorial_max(1, 5, 3, -5))  # mostra "120" na tela
