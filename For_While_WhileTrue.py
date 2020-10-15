inte = int(input('Digite um número inteiro.'))

# if, elif e else.
# Note que podemos ter estruturas com if, elif e else; if e else ou if e elif sem problema algum.
if inte > 0 and inte < 10:
    print(f'{inte} é positivo, mas menor do que 10.')
elif inte < 0:
    print(f'{inte} é negativo.')
elif inte >= 10:
    print(f'{inte} é positivo e maior do que 10.')
else:
    print(f'{inte} é igual a zero.')

# while (enquanto).
# nesta estrutura, precisamos informar na mesma linha do "while" qual é o critério
# de comparação da repetição (linha 20). Precisaremos também informar OBRIGATORIAMENTE
# algo que faça com que o critério de comparação seja em algum momento extrapolado (linha 24)
soma_par = 0
soma = 0
while num <= 1000:
    soma = soma + num
    if num % 2 == 0:
        soma_par = soma_par + num
    num = num + 1
print(f'O valor da soma é {soma} e do soma_par é {soma_par}.')

# do while (ou while True -> faça enquanto).
# nesta estrutura, precisamos informar dentro do "while" qual é o critério
# de parada junto do comando de parada (linhas 37 e 38). Precisaremos também
# fazer algo que cause o eventual atendimento deste critério de parada (linha 36).
soma_par = 0
soma = 0
while True:
    if num % 2 == 0:
        soma_par = soma_par + num
    num = num + 1
    if num > 1000:
        break
print(f'O valor da soma é {soma} e do soma_par é {soma_par}.')

# for (para todo)
# aqui, informamos de antemão todos os valores que devem ser percorridos pela repetição
# (linha 46). Não há a necessidade de se preocupar com os critérios de parada além disto.
soma_par = 0
soma = 0
for num in range(1, 1001):
    soma = soma + num
    if num % 2 == 0:
        soma_par = soma_par + num
print(f'O valor da soma é {soma} e do soma_par é {soma_par}.')
