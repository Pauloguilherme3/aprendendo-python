teste = []
#paulo
while True:
    teste.append(str(input("Digite uma espressão: ")))
    if (teste[0].count("(")+teste[0].count(")")) % 2 == 0:
        print("Esta espressão e valida!!")
        break
    else:
        print("Espressão invalida!!")
        teste.clear()
