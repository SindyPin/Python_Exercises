# 1. Peça ao usuário para que ele digite um número de jogos de computador (ou
# console) dos quais gosta. Se você não quiser usar como exemplo jogos, pode
# usar filmes ou bandas de música. Após receber o dado, peça para que digite o
# nome desses jogos (bandas ou filmes), na quantidade indicada. Por exemplo, se
# ele digitou "5", você deve pedir cinco vezes para que ele digite o nome de um
# jogo/banda/filme. Você deve armazenar em um vetor cada um desses itens.
# 2. Caso ele tenha digitado um nome que já está armazenado no vetor, você deve
# pedir para que informe outro que seja válido.
# 3. Após ele ter digitado todos os nomes, peça para que digite a nota que dá para
# cada um dos itens. A nota deve ser entre 0 e 10. Se for abaixo ou acima disso,
# você deve pedir por uma nova nota. Armazene as notas (válidas) em uma matriz.
# A primeira coluna da matriz deverá ser o nome do item e a segunda, a nota.
# 4. Mostre a média das notas armazenadas na matriz.


numero = int(input("Digite o número de jogos de console que você gosta mais gosta: "))
jogos = []
jogos_notas = []

i = 1
while i <= numero:
    jogo = input("Digite o nome do {0}º jogo: ".format(i))
    try:
        indice = jogos.index(jogo)
    except:
        jogos.append(jogo)
        i = i + 1
print(jogos)

i = 0
while i < numero:
    nota = float(input("Digite a nota que daria ao jogo {0}: ".format(jogos[i])))
    if nota < 0 or nota > 10:
        print("Digite novamente uma nota entre 0 e 10.")
    else:
        jogo_nota = []
        jogo_nota.append(jogos[i])
        jogo_nota.append(nota)
        jogos_notas.append(jogo_nota)
        i = i + 1
print(jogos_notas)

soma = 0
for i in jogos_notas:
    soma = soma + i[1]
print('A média das notas fornecidas é: ', soma/len(jogos_notas))
