test = ("paulo", "maria", 'computador', 'casa', 'carro', 'paralelepipado')
for i in test:
    print(f'Na palavra {i} temos a vogal [ ', end='')
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra, end=' ')
    print("]", end="\n")
