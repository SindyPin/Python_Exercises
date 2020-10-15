# Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.

direcao_escape = str(input('Escreva a direção cardinal para onde quer escapar (em português): '))
direcoes_possiveis = ['norte', 'sul', 'leste', 'oeste']

if direcao_escape in direcoes_possiveis:
    print('Pode escapar!')
else:
    print('Não pode escapar. Busque outra direção...')
