def fibonacci(limite):

    # retorna o menor número de Ficonacci maior que limite
    anterior = 1  # primeiro número de Fibonacci
    atual = 1  # segundo número de Fibonacci
    while atual <= limite:

        # atual torna-se anterior, e novo atual é calculado
        anterior, atual = atual, anterior + atual
    return atual
