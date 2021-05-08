valores = [[], []]
for c in range(1, 8):
    n = int(input(f"Digite o {c}° valor:"))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print(f"Os valores pares digitados são {sorted(valores[0])}")
print(f"Os valores impares digitados são {sorted(valores[1])}")
