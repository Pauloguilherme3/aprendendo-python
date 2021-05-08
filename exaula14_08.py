condiçao = "S"
contador = 1
maior = 0
menor = 0
soma = 0

while condiçao == "S" or condiçao != "N":
    if condiçao == "S":
        n1 = int(input("Digite {}° numero: ".format(contador)))
        soma += n1
        if contador == 1:
            maior = n1
            menor = n1
        contador += 1
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    else:
        print("Digite um numero valido!!")
    condiçao = str(input("Quer continuar?[S/N]")).strip().upper()
media = soma / (contador-1)
print("A media = \033[32m{:.2f}\033[m".format(media))
print("O numero \033[32m[{}]\033[m maior é o menor \033[32m[{}]".format(maior, menor))
