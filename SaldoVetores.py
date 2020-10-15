print('Vamos cadastrar os valores dos saldos das pessoas dentro de um vetor.')
saldo_pessoa = [1000.00, 500.40, 0.40, -1400.00, 500.55, 3.14, -100.00]

print('Vamos agora escrever o primeiro item da lista.')
print(f'O saldo na posição 0 do vetor é {saldo_pessoa[0]}')

print('Vamos modificar um dos valores e mostrar todos novamente.')
saldo_pessoa[2] = 3.14
for posicao in range(len(saldo_pessoa)):
    print(f'O saldo na posição {posicao} do vetor é {saldo_pessoa[posicao]}.')

print('Vamos agora remover o quarto valor da lista, mostrando todos depois.')
saldo_pessoa.pop(3)
for posicao in range(len(saldo_pessoa)):
    print(f'O saldo na posição {posicao} do vetor é {saldo_pessoa[posicao]}.')

print('Vamos remover o primeiro valor que seja igual a 3.14, mostrando todos depois.')
saldo_pessoa.remove(3.14)
for posicao in range(len(saldo_pessoa)):
    print(f'O saldo na posição {posicao} do vetor é {saldo_pessoa[posicao]}.')

print('Vamos adicionar um novo valor no fim da lista, mostrando todos novamente.')
saldo_pessoa.append(9900.99)
for posicao in range(len(saldo_pessoa)):
    print(f'O saldo na posição {posicao} do vetor é {saldo_pessoa[posicao]}.')

print('Vamos agora inserir um novo valor na 4a posição, mostrando todos depois.')
saldo_pessoa.insert(3, 9200.50)
for posicao in range(len(saldo_pessoa)):
    print(f'O saldo na posição {posicao} do vetor é {saldo_pessoa[posicao]}.')

print('Vamos inserir o conteúdo de uma outra lista, mostrando todos depois.')
novos_saldos = [400.50, 470.50, -235.70]
saldo_pessoa.extend(novos_saldos)
for posicao in range(len(saldo_pessoa)):
    print(f'O saldo na posição {posicao} do vetor é {saldo_pessoa[posicao]}.')
