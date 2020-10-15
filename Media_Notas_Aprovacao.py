nota1 = float(input('Escreva a nota do primeiro bimestre: '))
nota2 = float(input('Escreva a nota do segundo bimestre: '))
nota3 = float(input('Escreva a nota do terceiro bimestre: '))
nota4 = float(input('Escreva a nota do quarto bimestre: '))
media_notas = (nota1 + nota2 + nota3 + nota4) / 4
print('A média anual das suas notas é ', round(media_notas, 2))

if media_notas >= 7.0:
    print('Por ter superado a média anual de 7, você está "APROVADO", parabéns!')
else:
    print('Por não ter alcançado a média anual de 7, você está "DESAPROVADO", estude mais!')
