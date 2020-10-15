# Crie um algoritmo que solicite o peso e a altura de uma pessoa (usando a função "input"). Em base desses dois valores,
# calcule o IMC (índice de massa corporal) dessa pessoa.
# O IMC é calculado da seguinte forma: IMC = peso/(altura²).
# Mostre na tela o IMC. Em seguida, mostre qual é a categoria na qual a pessoa se enquadra da seguinte forma:
# Se o IMC for menor do que 18,5: mostre "Abaixo do peso";
# Se for igual ou maior do que 18,5 e menor do que 25: "Peso normal";
# Se for igual ou maior do que 25 e menor do que 30: "Sobrepeso";
# Se for igual ou maior do que 30 e abaixo de 35: "Obesidade I";
# Se for igual ou maior do que 35 e abaixo de 40: "Obesidade II";
# Se for acima de 40: "Obesidade III".

peso = float(input('Digite o valor do peso em kg: '))
altura = float(input('Digite o valor da altura em metros: '))
IMC = peso / (altura**2)

if IMC < 18.5:
    print('Abaixo de peso')
elif 18.5 <= IMC < 25:
    print('Peso normal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 35:
    print('Obesidade do tipo I')
elif 35 <= IMC < 40:
    print('Obesidade do tipo II')
