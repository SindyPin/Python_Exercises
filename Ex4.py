# Crie uma lista e uma tupla. Tente modificar um dos elementos de cada uma.
# O que ocorre?

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
lista[0:9:1] = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]
print(lista)
lista[0:9:1] = [20, 30, 40]
print(lista)

tupla1 = 1, 2, 3
tupla2 = (1, 2, 3)
print(tupla1)
print(tupla2)
