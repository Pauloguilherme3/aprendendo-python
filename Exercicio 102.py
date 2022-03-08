def fatorial(x, show=False):
    """
    Colcule o Fatorial de um numero.
    :param x: O numero a ser calculado
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O valor do falotorial de um numero n
    """
    resultado = 1
    print(30*"=")
    for i in range(x, 0, -1):
        resultado *= i
        if show:
            if i > 1:
                print(f"{i} ", end="x ")
            else:
                print(f"{i} ", end="= ")
    return resultado


print(fatorial(5, True))
