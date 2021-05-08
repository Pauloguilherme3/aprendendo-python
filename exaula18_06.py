n = []
while True:
    n.append(int(input('Digite um valor: ')))
    controle = str(input('Quer continuar? [S/N]')).upper().strip()
    if controle == 'N':
        break
print('-='*30)
print(f'Foram digitados {len(n)} numeros.')
print(f'A lista descrescente : {sorted(n, reverse=True)}')
print(f'O valor 5 {"faz parte da lista!"if 5 in n else "Não faz parte da lista!"}')
