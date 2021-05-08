lista, peso, listamaisleves, listamaispesadas, pessoa = list(), list(), list(), list(), list()
while True:
    pessoa.append(str(input("Digite o nome:")))
    pessoa.append(int(input("Digite o peso:")))
    lista.append(pessoa[:])
    pessoa.clear()
    controle = str(input("Quer continuar [S/N] ")).upper().strip()
    if controle[0] in "N":
        break
for c, nome in enumerate(lista):
    peso.append(lista[c][1])
for f, pesos in enumerate(peso):
    if max(peso) == pesos:
        listamaispesadas.append(lista[f][0])
    elif min(peso) == pesos:
        listamaisleves.append(lista[f][0])

print(f'Ao todo foram cadastrados {len(lista)} pessoas')
print(f"O maior peso foi {max(peso)}kg e o nome são : {listamaispesadas}")
print(f"O menor peso foi {min(peso)}kg e o nome são : {listamaisleves}")
