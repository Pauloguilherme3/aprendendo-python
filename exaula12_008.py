altura = float(input("Qual sua altura? (m) "))
peso = float(input("Qual seu peso? (kg) "))
imc = peso/altura**2
if imc < 18.5:
    print("abaixo do peso .{:.1f}".format(imc))
elif 18 <= imc < 25:
    print("Peso ideal {:.1f}".format(imc))
elif 25 <= imc < 30:
    print("sobrepeso {:.1f}".format(imc))
elif 30 <= imc < 40:
    print("Obesidade {:.1f}".format(imc))
else:
    print("Obesidade Morbida {:.1f}".format(imc))

