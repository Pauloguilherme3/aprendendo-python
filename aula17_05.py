par = []
impar = []
numeros = []
while True:
    numeros.append(int(input("Digite um numero:")))
    controle = str(input('Quer continuar? [S/N] ')).upper().strip()
    if controle in "Nn":
        break
for v in numeros:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Os numeros digitados {numeros}')
print(f'Os numeros pares {par}')
print(f'Os numeros impares {impar}')
