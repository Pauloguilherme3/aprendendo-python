from time import sleep
print("Programa de funções!!")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
opçao = 0
laranja = "\033[33m"
azul = "\033[34m"
while opçao != 5:
    opçao = int(input("""    {0}[1] {1}Somar
    {0}[2] {1}multiplicar
    {0}[3] {1}maior
    {0}[4] {1}novos numeros
    {0}[5] {1}sair do programa
>>>>> Qual sua escolha: \033[m""".format(laranja,azul)))
    if opçao == 1:
        soma = n1 + n2
        print("soma: {} + {} = {}".format(n1,n2,soma))
        print(("=-=")*10)
    elif opçao == 2:
        multiplicar = n1 * n2
        print("multiplicação: {} x {} = {}".format(n1,n2,multiplicar))
        print(("=-=") * 10)
    elif opçao == 3:
        if n1 > n2:
            print("Maior: {} que {}".format(n1,n2))
            print(("=-=") * 10)
        else:
            print("Maior: {} que {}".format(n2,n1))
            print(("=-=") * 10)
    elif opçao == 4:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))
    elif opçao == 5:
        print("Fechando programa",end="")
        sleep(0.5)
        print(".",end="")
        sleep(0.5)
        print(".",end="")
        sleep(0.5)
        print(".")
        print(("=-=") * 10)
        continue
    else:
        print("Digite um valor valido!")
sleep(0.6)
print("Fim do programa , Volte sempre!!")