n, par, impar = [], [], []
while True:
    n.append(int(input('Digite um valor:')))
    controle = str(input('Quer continuar ? [S/N] ')).upper().strip()
    if controle == 'N':
        break
for i in n:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f"A lista completa è {n}.")
print(f'A lista de pares é {par}.')
print(f"A lista de impares é {impar}")
