# Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'],
# exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'.

jogadores_beisebol = str(input('Escreva o nome de um jogador de beisebol: '))
lista_jogadores = ['Musical', 'Aaron', 'Williams', 'Gehring', 'Ruth']

if jogadores_beisebol in lista_jogadores:
    print('Você escreveu o nome de um dos 5 maiores jogadores de beisebol de todos os tempos!')
else:
    print(jogadores_beisebol, 'não está dentro do ranking dos maiores jogadores de beisebol de todos os tempos')
