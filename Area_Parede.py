# Faça um programa que peça ao usuário a largura e a altura de uma parede, em metros.
# Com base nesses dados, calcule a área da parede.
# Então, calcule a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 1,5 metro quadrado.
# Mostre ao usuário quanto ele deverá usar de tinta para executar a pintura.

largura_metros = float(input('Digite a largura da parede selecionada em metros: '))
altura_metros = float(input('Digite a altura da parede selecionada em metros: '))
area_metros_quadrados = largura_metros * altura_metros
print('A área da parede é de aproximadamente', round(area_metros_quadrados, 3), 'metros quadrados')

pintura_litros = area_metros_quadrados / 1.5
print('Deverá usar pelo menos ', int(pintura_litros), 'litros de pintura para pintar toda a parede selecionada')
