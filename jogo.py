# Com base no algoritmo desenvolvido na fase 1, inclua as seguintes funcionalidades:
# Para cada partida feita, armazene em um vetor os resultados.
# Precisamos armazenar no vetor quem foi o vencedor de cada partida (ou se houve um empate).
# Quando o usuário escolher terminar a partida,
# mostre a porcentagem de partidas em que ele venceu e a porcentagem de empates.
# Modifique seu código para que haja pelo menos uma função responsável por mostrar o menu
# (isto é, o item 1 da primeira fase do projeto final), uma função para determinar o resultado da partida
# (item 3 da primeira fase) e uma função para mostrar o resultado de todas as partidas (item 2 da segunda fase).

print("Vamos jogar 'Pedra, Papel ou Tesoura'!!!")
num = int(input("Digite 1 (número correspondente a pedra), 2 (número correspondente a papel) \
ou 3 (número correspondete a tesoura): "))
matriz = []  # Todas as jogadas
matriz2 = []  # Empates
matriz3 = []  # Jogos ganhos pelos usuário
while num == 1 or num == 2 or num == 3:
    import random
    r1 = random.randint(1, 3)
    for i in range(0, 3):
        linha = []
        linha2 = []
        linha3 = []
        if (num == 1 and r1 == 1) or (num == 2 and r1 == 2) or (num == 3 and r1 == 3):
            print("Houve um EMPATE!!!")
            num = int(input("Se quiser seguir jogando, digite 1, 2 ou 3; senão, digite qualquer outro número: "))
            linha.append(1)
            linha2.append(1)
        elif num == 1 and r1 == 2:  # Usuário = pedra e computador = papel
            print("Você PERDEU!!!")
            num = int(input("Se quiser seguir jogando, digite 1, 2 ou 3; senão, digite qualquer outro número: "))
            linha.append(1)
        elif num == 1 and r1 == 3:  # Usuário = pedra e computador = tesoura
            print("Você GANHOU!!!")
            num = int(input("Se quiser seguir jogando, digite 1, 2 ou 3; senão, digite qualquer outro número: "))
            linha.append(1)
            linha3.append(1)
        elif num == 2 and r1 == 1:  # Usuário = papel e computador = pedra
            print("Você GANHOU!!!")
            num = int(input("Se quiser seguir jogando, digite 1, 2 ou 3; senão, digite qualquer outro número: "))
            linha.append(1)
            linha3.append(1)
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
            linha3.append(1)
        matriz.append(linha)
        matriz2.append(linha2)
        matriz3.append(linha3)


def fim():
    if 1 > num > 3:
        contador = len(matriz)
        print("Você fez", contador, "jogadas")
    return fim


jogos = len(matriz)


def empates():
    emp = len(matriz2)
    emp_percentual = (emp * 100) / jogos
    print("O número de jogos empatados é:", emp, "que corresponde a", emp_percentual, "% de todas as partidas")
    return empates


def vencidos():
    ven = len(matriz3)
    ven_percentual = (ven * 100) / jogos
    print("O número de jogos que você venceu é:", ven, "que corresponde a", ven_percentual, "% de todas as partidas")
    return vencidos


empates()
vencidos()
fim()
