# Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário, exiba 'Definitivamente não é um ano bissexto.'

ano = int(input('Insira um ano: '))

if ano % 4 == 0:
    print(ano, 'pode ser um ano bissexto')
else:
    print(ano, 'definitivamente não é um ano bissexto')
