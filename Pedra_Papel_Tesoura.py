# Escreva um algoritmo que obedeça aos seguintes passos:
# Peça ao usuário digitar uma opção: 1 equivale a pedra, 2 equivale à papel e 3 equivale à tesoura.
# Se ele digitar qualquer valor que não seja um desses valores, sairá do jogo.
# Assim que ele digitar uma jogada, gere um número aleatório entre 1 e 3. Dica: pesquise pela função randint.
# Com base na opção gerada pelo computador e na opção informada pelo usuário, mostre na tela se houve um empate,
# se o usuário ganhou ou se o computador ganhou.
# Depois de mostrar o resultado, peça por uma nova opção (item 1).
# Quando o usuário escolher sair do jogo (isto é, quando ele digitar qualquer opção que não seja 1, 2 ou 3),
# mostre na tela quantas vezes jogou contra o computador.

print("Vamos jogar 'Pedra, Papel ou Tesoura'!!!")
num = int(input("Digite 1 (número correspondente a pedra), 2 (número correspondente a papel) \
ou 3 (número correspondete a tesoura): "))
matriz = []

while num == 1 or num == 2 or num == 3:
    import random
    r1 = random.randint(1, 3)
    for i in range(0, 3):
        linha = []
        if (num == 1 and r1 == 1) or (num == 2 and r1 == 2) or (num == 3 and r1 == 3):
            print("Houve um EMPATE!!!")
            num = int(input("Se quiser seguir jogando, digite 1, 2 ou 3; senão, digite qualquer outro número: "))
            linha.append(1)
        elif num == 1 and r1 == 2:  # Usuário = pedra e computador = papel
            print("Você PERDEU!!!")
            num = int(input("Se quiser seguir jogando, digite 1, 2 ou 3; senão, digite qualquer outro número: "))
            linha.append(1)
        elif num == 1 and r1 == 3:  # Usuário = pedra e computador = tesoura
            print("Você GANHOU!!!")
            num = int(input("Se quiser seguir jogando, digite 1, 2 ou 3; senão, digite qualquer outro número: "))
            linha.append(1)
        elif num == 2 and r1 == 1:  # Usuário = papel e computador = pedra
            print("Você GANHOU!!!")
            num = int(input("Se quiser seguir jogando, digite 1, 2 ou 3; senão, digite qualquer outro número: "))
            linha.append(1)
        elif num == 2 and r1 == 3:  # Usuário = papel e computador = tesoura
            print("Você PERDEU!!!")
            num = int(input("Se quiser seguir jogando, digite 1, 2 ou 3; senão, digite qualquer outro número: "))
            linha.append(1)
        elif num == 3 and r1 == 1:  # Usuário = tesoura e computador = pedra
            print("Você PERDEU!!!")
            num = int(input("Se quiser seguir jogando, digite 1, 2 ou 3; senão, digite qualquer outro número: "))
            linha.append(1)
        elif num == 3 and r1 == 2:  # Usuário = tesoura e computador = papel
            print("Você GANHOU!!!")
            num = int(input("Se quiser seguir jogando, digite 1, 2 ou 3; senão, digite qualquer outro número: "))
            linha.append(1)
        matriz.append(linha)
else:
    contador = len(matriz)
    print("Você jogou", contador, "partidas")

