import math

altura = float(input('Escreva a altura do cilindro em metros: '))
raio = float(input('Escreva o raio da base do cilindro em metros: '))
area_total = 2 * math.pi * raio * (altura + raio)

# Cada lata contém 5 litros de tinta
# Cada litro de tinta pinta 3 metros quadrados
# Então, cada lata de tinta pinta 15 metros quadrados
# Criar algortimo para saber quantas latas são necessárias para pintar o cilindro acima

lata_litros = 5
litro_m2 = 3
lata_pinta_m2 = lata_litros * litro_m2
latas_necessarias = area_total / lata_pinta_m2
print('Serão necessários ao menos ', math.ceil(latas_necessarias), 'latas de tinta para pintar o cilindro')

lata_preco = 50
custo = latas_necessarias * lata_preco
print('O custo total para pintar o cilindro será de $', round(custo, 2))
