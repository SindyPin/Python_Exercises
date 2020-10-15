lista = [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)

# Incluir o número 10 ao final da lista:
lista.append(10)
print(lista)

# Inserir outro 0 antes do número 1:
lista.insert(1, 0)
print(lista)

# Remover o último ítem da lista:
lista.pop()
print(lista)

# Remover a primeira ocorrência do número 1:
lista.remove(1)
print(lista)

# Invertir a ordem dos itens da lista:
lista.reverse()
print(lista)

# Ordenar a lista de maior a menor:
lista.sort()
print(lista)

# Mostrar o número de ocorrências do número 0:
print(lista.count(0))

# Mostrar o tamanho da lista:
print(len(lista))

# Mudar o quarto 0 por 1:
lista[3] = 1
print(lista)
