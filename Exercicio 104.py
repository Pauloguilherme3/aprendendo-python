def leiaint(text=""):
    while True:
        try:
            b = int(input(text))
            break
        except ValueError:
            print("\033[1;31mERROR digite um valor inteiro ", "\033[0;0m")
    return b


n = leiaint("Digite um Numero: ")
print(f"Voce acabou de digitar o numero {n}")
