distancia = int(input("Digite a distancia da viagem! "))
valorapagar = float
if(distancia <= 200):
    valorapagar = distancia*0.5
else:
    valorapagar = distancia*0.45
print("O valor da viagem fica {} reais".format(valorapagar))