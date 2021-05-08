fatorial = int(input("Digite um numero para fatorar: "))
contador = fatorial
print("Calculando {}! =".format(contador),end= "")
while contador != 1:
    contador -= 1
    fatorial *= contador
    print("{} ".format(contador),end="")
    print("x "if contador > 1 else "= ",end="")
print(fatorial)
