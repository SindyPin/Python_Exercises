# Escreva um algoritmo que obedeça aos seguintes passos (um único algoritmo deve executar todos os passos a seguir):
# Peça ao usuário que digite um número entre 100 e 100 + X + Y, sendo X e Y seu dia e mês de nascimento,
# respectivamente. Por exemplo, se eu nasci no dia 09/10, pedirei ao usuário para que digite um número entre 100 e 119.
# Se o número digitado não estiver entre esse limite, você deverá pedir novamente por um número válido, repetidamente,
# até que ele o informe.
# Após receber um número válido, mostre na tela todos os números inteiros entre 1 e o número digitado pelo usuário.
# Se o número for múltiplo de 3, mostre na tela seu nome, em vez do número.
# Se o número for múltiplo de 5, mostre na tela seu sobrenome, em vez do número.
# Se o número for múltiplo de 3 e de 5, mostre na tela seu ano de nascimento, em vez do número.

# Pedido do mês de nascimento:

mes = int(input('Digite o número do seu mês de nascimento: '))

if mes < 1 or mes > 12:
    i = 0
    while mes < 1 or mes > 12:
        mes = int(input('Digite novamente o seu mês de nascimento entre 1 e 12: '))
        i = i + 1

elif 1 <= mes <= 12:
    print('Valor válido inserido referente a seu mês de nascimento!')

# Pedido do ano de nascimento:

ano = int(input('Digite os últimos 2 dígitos do seu ano de nascimento: '))

if ano < 0 or ano > 99:
    j = 0
    while ano < 0 or ano > 99:
        ano = int(input('Digite novamente os últimos 2 dígitos do seu ano de nascimento: '))
        j = j + 1

elif 0 <= ano <= 99:
    print('Valor válido inserido referente aos últimos 2 dígitos do seu ano de nascimento!')

# Pedido da soma do mês e do ano de nascimento \
# O resultado não pode ser maior a menor a 1 nem maior a 111
# Porque 12 meses (limite) + 99 (limite dos últimos 2 dígitos de qualquer ano) = 111:

soma_mes_ano = int(input('Digite a soma do seu mês e de seu ano de nascimento: '))

if soma_mes_ano < 0 or soma_mes_ano > 111:
    k = 0
    while soma_mes_ano < 0 or soma_mes_ano > 111:
        soma_mes_ano = int(input('Digite novamente a soma entre seu mês e seu ano de nascimento: '))
        k = k + 1

elif 1 <= soma_mes_ano >= 111:
    print('Resultado válido inserido referente à soma do seu mês e do seu ano de nascimento!')

# Pedido da soma do mês e do ano de nascimento \
# O resultado não pode ser menor a 100 nem maior a 211 \
# Porque 12 meses (limite) + 99 (limite dos últimos 2 dígitos de qualquer ano) + 100 = 211:

soma_mes_ano_100 = int(input('Some 100 ao resultado anterior e digite o novo resultado: '))

if soma_mes_ano_100 < 100 or soma_mes_ano_100 > 211:
    m = 0
    while soma_mes_ano_100 < 100 or soma_mes_ano_100 > 211:
        soma_mes_ano_100 = int(input('Some novamente 100 ao resultado anterior: '))
        m = m + 1

elif 100 <= soma_mes_ano_100 <= 211:
    print('Resultado válido inserido referente à soma de 100 + seu mês + os últimos 2 dígitos do seu ano de nascimento!')

# Escolher um número entre 100 e o resultado anterior.
# O número escolhido não pode ser menor ou igual que 100 nem maior que 211:

numero_escolhido = int(input('Agora, escolha e digite um número entre 100 e o valor do seu último resultado: '))

if numero_escolhido <= 100 or numero_escolhido > 211:
    n = 0
    while numero_escolhido <= 100 or numero_escolhido > 211:
        numero_escolhido = int(input('Digite novamente um número entre 100 e o valor do seu último resultado: '))
        n = n + 1

elif 100 < numero_escolhido <= 211:
    print('Número escolhido com sucesso!')

# Mostrar na tela todos os números inteiros entre 1 e o número digitado pelo usuário.

print('Todos os números entre 1 e o número escolhido são: ')
for p in range(1, numero_escolhido + 1):
    print(p)

# Se o número for múltiplo de 3, mostre na tela seu nome, em vez do número.
# Se o número for múltiplo de 5, mostre na tela seu sobrenome, em vez do número.
# Se o número for múltiplo de 3 e de 5, mostre na tela seu ano de nascimento, em vez do número.

nome = str(input('Agora digite seu nome: '))
sobrenome = str(input('Agora seu sobrenome: '))
ano_nascimento = int(input('E finalmente, digite seu ano de nascimento por extenso: '))

if numero_escolhido % 3 == 0:
    print('Como o número escolhido é múltiplo de 3, então a continuação aparecerá seu nome:', nome)
elif numero_escolhido % 5 == 0:
    print('Como o número escolhido é múltiplo de 5, então a continuação aparecerá seu sobrenome:', sobrenome)
elif numero_escolhido % 3 == 0 and numero_escolhido % 5 == 0:
    print('Como o número escolhido é múltiplo de 3 e de 5 ao mesmo tempo, \
então a continuação aparecerá seu ano de nascimento por extenso:', ano_nascimento)
else:
    q = 0
    while numero_escolhido % 3 != 0 and numero_escolhido % 5 != 0:
        numero_escolhido = int(input('Escolha algum outro número entre 100 e o seu último resultado \
(a soma de 100 + seu mês de nascimento + os últimos 2 dígitos do seu ano de nascimento) \
e que seja múltiplo de 3 e/ou de 5: '))
        q = q + 1
