velocidade = int(input("Digite a velocidade do carro!! "))
if (velocidade > 80):
    print("Você sera multado no valor de {} reais.".format((velocidade-80)*7))
else:
    print("Velocidade permitida")
