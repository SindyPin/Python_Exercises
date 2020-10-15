i = int(input('Digite o primeiro número inteiro da sua série: '))
f = int(input('Digite o último número da sua série: '))
p = int(input('Digite o intervalo de sequência: '))

for i in range(i, f+1, p):
    print(i)

for j in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

s = 0
for k in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n  # também pode ser escrito como s += n e serve para somar todos os números digitados pelo usuário
print('O somatório de todos os valor digitados foi {}'.format(s))
