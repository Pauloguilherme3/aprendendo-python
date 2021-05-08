valores = []
for i in range(0, 5):
    n = int(input("Digite um numero:"))
    if i == 0 or n > valores[-1]:
        valores.append(n)
        print('O valor foi adicionado no final da lista')
    else:
        for pos in range(len(valores)):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'foi adicionado na posição {pos}')
                break
print('-='*30)
print(f"Os valores adicionados {valores}")
