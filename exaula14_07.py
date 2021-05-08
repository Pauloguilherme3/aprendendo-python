n = contador = soma = 0
while n != 999:
    n = int(input(f"Digite {contador+1}° valor: "))
    if n == 999:
        continue
    elif n != 999:
        contador += 1
        soma += n
print("foram {} numero e a soma deles foi {}".format(contador,soma))