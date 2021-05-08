contador=0
proximo =0
anterior =0
n = int(input("Quantos numeros de fibonacci: "))
print("-*"*15)
while contador < n :
        print(proximo, end= " ↦ ")
        proximo = proximo + anterior
        anterior = proximo - anterior
        if proximo ==0:
            proximo += 1
        contador += 1

