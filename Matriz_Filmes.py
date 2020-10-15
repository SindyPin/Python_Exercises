# Escreva um algoritmo que obedeça aos seguintes passos:
# 1. Peça ao usuário para que digite um número de filmes dos quais gosta.
# 2. Após receber o dado, peça que digite o nome desses filmes na quantidade indicada.
# Por exemplo, se ele digitou "5", você deve pedir cinco vezes para que ele digite o nome de um filme.
# Você deve armazenar em um vetor cada um desses itens.
# 3. Caso ele tenha digitado um nome que já está armazenado no vetor, você deve pedir para que informe outro.
# 4. Após ele ter digitado todos os nomes, peça para que digite a nota que dá para cada um dos itens.
# A nota deve ser entre 0 e 10. Se for abaixo ou acima disso, você deve pedir por uma nova nota.
# 5. Armazene as notas (válidas) em uma matriz. A primeira coluna da matriz deve ser o nome do item e a segunda, a nota
# 6. Mostre a média das notas armazenadas na matriz.

numero = int(input('Digite o número de filmes que você mais gosta: '))
matriz = []
lista_filmes = []

contagem = 0
while contagem < numero:
    if contagem < numero:
        filme = str(input('Digite o nome do filme ' + str(contagem + 1) + ': '))
        if filme not in lista_filmes:
            lista_filmes.append(filme)
            matriz.append(lista_filmes)
            contagem = contagem + 1
        elif filme in lista_filmes:
            print(filme, 'já foi digitado.')
            filme = str(input('Digite o nome de um filme não digitado anteriormente: '))
            lista_filmes.append(filme)
            matriz.append(lista_filmes)
            contagem = contagem + 1
    else:
        break

nota_filmes = []
for i in range(0, numero):
    nota = float(input(f'Digite uma nota entre 0 e 10 para o filme {lista_filmes[i]}: '))
    if 0 <= nota <= 10:
        nota_filmes.append(nota)
        matriz.append(nota_filmes)
        i = i + 1
    else:
        print(f'Nota inválida. Digite novamente uma nota entre 0 e 10 para o filme {lista_filmes[i]}: ')
        nota_filmes.append(nota)
        matriz.append(nota_filmes)
        i = i + 1
    matriz.append(nota_filmes)

media_notas = sum(nota_filmes)/numero
print('A média das notas dos filmes é: ', media_notas)
