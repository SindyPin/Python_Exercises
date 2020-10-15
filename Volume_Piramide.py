# Faça um programa que calcule o volume de uma pirâmide (com base retangular).
# Para tanto, você precisará solicitar ao usuário a altura, o comprimento da base e a largura da base.
# Com o comprimento e a largura da base, você conseguirá determinar sua área.
# Em seguida, você poderá determinar o volume da pirâmide,
# multiplicando a área da base pela altura e dividindo o resultado por 3.

largura_piramide = float(input('Digite a largura da base retangular da pirâmide em estudo em metros: '))
comprimento_piramide = float(input('Digite o comprimento da base retangular da pirâmide em estudo em metros: '))
altura_piramide = float(input('Digite a altura da pirâmide em estudo em metros: '))
volume_piramide = (largura_piramide * comprimento_piramide * altura_piramide) / 3
print('O volume da pirâmide de base retangular em estudo é de aproximadamente', round(volume_piramide, 3), 'metros cúbicos')