# Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto'.

golpes = int(input('Escreva o número de golpes recebidos: '))
defesa = int(input('Escreva o número de defesas realizadas: '))

if golpes > 10 and defesa == 0:
    print('Você está morto...')
else:
    print('Você continua vivo...')
