tamanho = int(input('Informe o tamanho de linhas e colunas de uma matriz identidade: '))
matriz = []
for i in range(0, tamanho):
    linha = []
    for j in range(0, tamanho):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for num_linha in range(0, len(matriz)):
    print(matriz[num_linha])
