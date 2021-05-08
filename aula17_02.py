valores = []
while True:
    n = int(input('Digite um valor:'))
    controle = ''
    if n in valores:
        print('Valor duplicado , nao vou adicionar!!')
    else:
        valores.append(n)
        print(f'Valor {n} salvo com sucesso.')

        while True:
            controle = str(input('Quer continuar? [S/N]')).upper().strip()
            if controle in 'SN':
                break
            else:
                print("Valor digitado invalido")
    if controle == 'N':
        break
print(f"Os numeros adicionados na lista foram {sorted(valores)}")
