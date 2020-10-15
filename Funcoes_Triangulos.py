# Uma das fontes de sátiras e memes da internet orbita pelo seguinte tema:
# quando olhamos um código que já desenvolvemos há certo tempo, ou encontramos nele vários defeitos,
# ou ele está tão complexo que não entendemos mais o que havíamos feito.
#
# A atividade da semana pede que você faça as seguintes instruções:
# 1. Escolha um código em Python que você tenha desenvolvido.
# Escolha o código que considera mais complexo e/ou aquele que necessita mais de reorganização e refatoração,
# 2. Tente, a partir desse código, encontrar pontos em que esteja duplicado ou até triplicado no que tange à lógica
# (ou seja, código em que a lógica é a mesma, com somente pequenas alterações nas variáveis e afins).
# 3. Busque criar uma função com a finalidade de eliminar essa lógica duplicada/triplicada.
# 4. Crie mais funções a partir do seu código para agrupar as operações feitas.
# Como sugestão, se seu bloco de código possui cinco ou mais linhas que executam em conjunto a mesma operação lógica,
# você provavelmente conseguirá transformar isso em uma função.
# 5. Busque deixar o código mais organizado, inserindo comentários, quando possível.


def dado_a():
    a = float(input('Digite o valor do primeiro lado do triângulo: '))
    return a


def dado_b():
    b = float(input('Digite o valor do segundo lado do triângulo: '))
    return b


def dado_c():
    c = float(input('Digite o valor do terceiro lado do triângulo: '))
    return c


def triangulo(a, b, c):
    if (a < b + c and b < a + c and c < a + b) and (a == b == c):
        print('A figura é um triângulo equilâtero (todos os lados são iguais).')
    elif (a < b + c and b < a + c and c < a + b) and (a != b != c):
        print('A figura é um triângulo escaleno (todos os lados são diferentes).')
    elif (a < b + c and b < a + c and c < a + b) and (a == b) or (a == c) or (b == c):
        print('A figura é um triângulo isósceles (somente 2 lados são iguais).')
    else:
        print('A figura não é um triângulo.')
    return triangulo


triangulo(dado_a(), dado_b(), dado_c())
