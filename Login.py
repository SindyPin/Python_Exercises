# Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login (ou seja, uma string).
# O programa, então, verifica se a identificação informada pelo usuário está na lista de usuários válidos.
# Dependendo do resultado, uma mensagem apropriada deverá ser impressa.
# Não importando o resultado, sua função deverá exibir 'Fim.' antes de terminar.

login = str(input('Insira seu login: '))

if login in ['joe', 'sue', 'hani', 'sophie']:
    print(login, 'você entrou!')
else:
    print('Usuário desconhecido')
