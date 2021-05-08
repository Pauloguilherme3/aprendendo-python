numeros = []
while True:
    numeros.append(int(input('Digite um numero:')))
    while True:
        controle = str(input('Quer digitar mais um valor ? [S/N]')).upper().strip()
        if controle[0] in 'SN':
            break
        else:
            print('Valor invalido')
    if controle == 'N':
        break
print(f'Foram digitados {len(numeros)} numeros!!')
print(f'A lista {(sorted(numeros, reverse=True))}')
print(f'A lista {sorted(numeros)[::-1]}')
sefoidigitado5 = "foi adicionado"if 5 in numeros else "Não foi adicionado"
print(f'O valor 5 {sefoidigitado5} na lista.')
