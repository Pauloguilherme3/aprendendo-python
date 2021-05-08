salario = float(input("Digite valor do Salario! "))
if salario >= 1250:
    print("O salario de {} com 10% de aumento fica {}".format(salario,salario*1.10))
else:
    print("O salario de {} com 15% de aumento fica {}".format(salario,salario*1.15))