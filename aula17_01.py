valore = []
for i in range(0, 5):
    valore.append(int(input(f"Adicione um valor na posição {i}:")))

print(f"O maior valor é {max(valore)} esta na posição ", end='')
for i, v in enumerate(valore):
    if v == max(valore):
        print(i, end='...')
print()
print(f"O menor valor é {min(valore)} é esta na posição ", end='')
for i, v in enumerate(valore):
    if v == min(valore):
        print(i, end='...')
