# Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings)
# e depois exiba na tela, uma por linha, todas as strings de quatro letras nessa lista.

lista_palavras = str(input('Insira 5 palavras: '))

for word in lista_palavras.split():
    if len(word) == 4:
        print(word)

# split() = This is the opposite of concatenation which merges or combines strings into one.
# What it does is split or breakup a string and add the data to a string array using a defined separator.
# If no separator is defined when you call upon the function, whitespace will be used by default.
