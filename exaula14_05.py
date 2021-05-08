termo = int(input("Digite Começo ou termo: "))
razao = int(input("Digite a razão: " ))
condição = 99999
soma = 0
contador = 10
contaprint =0
while condição != 0:
    if condição == 99999:
        for c in range(contador-1):
            print(termo,end="-*")
            termo += razao
            contaprint += 1
        termo += razao
        contaprint += 1
        print(termo)
    elif condição == 1:
        contador = int(input("Quantos termos quer mostrar mais: "))
        for c in range(contador-1):
            print(termo,end="-*")
            termo += razao
            contaprint += 1
        termo += razao
        contaprint += 1
        print(termo)
    elif condição == 0:
        continue
    else:
        print("Opção invalida")
    condição = int(input("""    [1]mostra mais termos
    [0]sair do programa
                Qual a opção: """))
print("programa finalizado com {} termos imprimidos".format(contaprint))

