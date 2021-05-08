matriz = [[[], [], []], [[], [], []], [[], [], []]]
soma = soma3 = 0
for c in range(3):
    for d in range(3):
        matriz[c][d].append(int(input(f'Digite um valor para [{c}, {d}]: ')))
        if matriz[c][d][0] % 2 == 0:
            soma += matriz[c][d][0]
        if d == 2:
            soma3 += matriz[c][d][0]
print('-='*30)
for a in range(3):
    for b in range(3):
        print(f'[  {matriz[a][b][0]:^5}  ]', end='')
    print()
print("-="*30)
print(f'A soma todos os valores = {soma}.')
print(f'A soma da 3° parte = {soma3}.')
print(f'O maior da segunda linha = {max(matriz[1])[0]}.')
