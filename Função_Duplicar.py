# Problemas com a funcção def:


def duplicar(a, b):
    a = a*2
    b = b*2


a = 5
b = 5
duplicar(a, b)
print(f'O valor de a é {a} e de b é {b}')


# Para ficar mais claro, mude a função acima para a seguinte:


def duplicar(banana, maca):
    banana = banana*2
    maca = maca*2
    return banana, maca


a = 5
b = 5
a, b = duplicar(a,b)
print(f'O valor de a é {a} e de b é {b}')
