notas = [['José', 5.0, 6.5, 3.4], ['Carlos', 3.5, 6.7, 7.7], ['Rui', 4.4, 9.5, 9.5]]
print('Mostrando todos os valores:')
for linha in range(len(notas)):  # note a diferença deste "for" para o que vem na linha abaixo
    for coluna in range(len(notas[linha])):
        print(f'A linha {linha}, coluna {coluna} possui o valor {notas[linha][coluna]}.')

print('Mostrando todos os valores da primeira coluna:')
for linha in range(len(notas)):
    print(f'A linha {linha}, coluna 0 possui o valor {notas[linha][0]}.')

print('Mostrando o valor da segunda coluna e terceira linha:')
print(notas[2][1])

print('Inserindo um novo aluno ao final da lista:')
notas.append(['César', 5.0, 1.3, 4.5])
for linha in range(len(notas)):
    for coluna in range(len(notas[linha])):
        print(f'A linha {linha}, coluna {coluna} possui o valor {notas[linha][coluna]}.')

print('Inserindo um novo aluno na segunda posição da lista:')
notas.insert(1, ['Leonel', 9.0, 8.1, 0.3])
for linha in range(len(notas)):
    for coluna in range(len(notas[linha])):
        print(f'A linha {linha}, coluna {coluna} possui o valor {notas[linha][coluna]}.')

print('Concatenando os dados de uma outra matriz:')
novas_notas = [['Juliana', 5.5, 6.5, 7.0], ['Rebeca', 4.3, 1.9, 8.5]]
notas.extend(novas_notas)
for linha in range(len(notas)):
    for coluna in range(len(notas[linha])):
        print(f'A linha {linha}, coluna {coluna} possui o valor {notas[linha][coluna]}.')

print('Removendo a última linha da lista:')
notas.pop()
for linha in range(len(notas)):
    for coluna in range(len(notas[linha])):
        print(f'A linha {linha}, coluna {coluna} possui o valor {notas[linha][coluna]}.')

print('Removendo a linha referente ao Leonel:')
notas.remove(['Leonel', 9.0, 8.1, 0.3])
for linha in range(len(notas)):
    for coluna in range(len(notas[linha])):
        print(f'A linha {linha}, coluna {coluna} possui o valor {notas[linha][coluna]}.')

print('Corrigindo (modificando) a segunda nota do terceiro aluno:')
notas[2][2] = 10.0
for linha in range(len(notas)):
    for coluna in range(len(notas[linha])):
        print(f'A linha {linha}, coluna {coluna} possui o valor {notas[linha][coluna]}.')
