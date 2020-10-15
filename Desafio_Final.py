# Escreva um algoritmo que obedeça aos seguintes passos (um único algoritmo deve executar todos os passos a seguir):
# Peça ao usuário que digite um número entre 100 e 100 + X + Y, sendo X e Y seu dia e mês de nascimento,
# respectivamente. Por exemplo, se eu nasci no dia 09/10, pedirei ao usuário para que digite um número entre 100 e 119.
# Se o número digitado não estiver entre esse limite, você deverá pedir novamente por um número válido, repetidamente,
# até que ele o informe.
# Após receber um número válido, mostre na tela todos os números inteiros entre 1 e o número digitado pelo usuário.
# Se o número for múltiplo de 3, mostre na tela seu nome, em vez do número.
# Se o número for múltiplo de 5, mostre na tela seu sobrenome, em vez do número.
# Se o número for múltiplo de 3 e de 5, mostre na tela seu ano de nascimento, em vez do número.

try:
    # Pedido do mês de nascimento:
    mes = int(input('Digite o número do seu mês de nascimento: '))

    if mes < 1 or mes > 12:
        i = 0
        while mes < 1 or mes > 12:
            mes = int(input('Digite novamente o seu mês de nascimento entre 1 e 12: '))
            i = i + 1
    elif 1 <= mes <= 12:
        print('Muito bem!')

    # Pedido do ano de nascimento:
    ano = int(input('Digite os últimos 2 dígitos do seu ano de nascimento: '))
    if ano < 0 or ano > 99:
        j = 0
        while ano < 0 or ano > 99:
            ano = int(input('Digite novamente os últimos 2 dígitos do seu ano de nascimento: '))
            j = j + 1
    elif 0 <= ano <= 99:
        print('Muito bem!')

    # Pedido da soma do mês e do ano de nascimento \
    # O resultado não pode ser maior a menor a 1 nem maior a 111
    # Porque 12 meses (limite) + 99 (limite dos últimos 2 dígitos de qualquer ano) = 111:
    soma_mes_ano = int(input('Digite a soma dos números anteriores: '))
    if soma_mes_ano < 0 or soma_mes_ano > 111:
        k = 0
        while soma_mes_ano < 0 or soma_mes_ano > 111:
            soma_mes_ano = int(input('Digite novamente a soma entre seu mês e seu ano de nascimento: '))
            k = k + 1

    # Pedido da soma do resultado anterior + 100\
    # O resultado não pode ser menor a 100 nem maior a 211 \
    # Porque 12 meses (limite) + 99 (limite dos últimos 2 dígitos de qualquer ano) + 100 = 211:
    soma_mes_ano_100 = int(input('Some 100 ao resultado anterior: '))

    if soma_mes_ano_100 < 100 or soma_mes_ano_100 > 211:
        m = 0
        while soma_mes_ano_100 < 100 or soma_mes_ano_100 > 211:
            soma_mes_ano_100 = int(input('Some novamente 100 + mês de nascimento \
+ últimos 2 dígitos do seu ano de nascimento: '))
            m = m + 1

    # Escolher um número entre 100 e o resultado anterior.
    # O número escolhido NÃO pode ser menor ou igual que 100 NEM maior que o resultado anterior:
    elif 100 <= soma_mes_ano_100 <= 211:
        print('Muito bem!')

    numero_escolhido = int(input('Agora, escolha e digite um número entre 100 e o seu último resultado: '))
    if numero_escolhido <= 100 or numero_escolhido > soma_mes_ano_100:
        n = 0
        while numero_escolhido <= 100 or numero_escolhido > soma_mes_ano_100:
            numero_escolhido = int(input('Digite novamente um número entre 100 e o valor do seu último resultado: '))
            n = n + 1
    elif numero_escolhido > 100 or numero_escolhido < soma_mes_ano_100:
        print('Muito bem!')

    # Mostrar na tela todos os números inteiros entre 1 e o número digitado pelo usuário.
    # Se o número for múltiplo de 3, mostre na tela seu nome, em vez do número.
    # Se o número for múltiplo de 5, mostre na tela seu sobrenome, em vez do número.
    # Se o número for múltiplo de 3 e de 5, mostre na tela seu ano de nascimento, em vez do número.
    nome = str(input('Agora digite seu nome: '))
    sobrenome = str(input('Agora seu sobrenome: '))
    ano_nascimento = int(input('E finalmente, digite seu ano de nascimento por extenso: '))
    print('A continuação aparecerá seu nome (quando o número for múltiplo de 3), \
seu sobrenome (quando for múltiplo de 5) ou o seu ano do nascimento (quando for múltiplo de 3 e de 5): ')
    for p in range(1, numero_escolhido + 1):
        if p % 3 == 0 and p % 5 == 0:
            print(ano_nascimento)
        elif p % 3 == 0:
            print(nome)
        elif p % 5 == 0:
            print(sobrenome)
        else:
            print(p)

except ValueError as error:
    print('Erro de digitação. Reinicie o programa.')
    print('Tipo de erro:', error)
