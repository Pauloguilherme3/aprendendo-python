sexo = str(input("Digite o Sexo[M/F]: ")).upper().strip()
while not sexo in "MF":
        sexo = str(input("Dados invalidos. Por favor , informe seu sexo: ")).strip().upper()
        if sexo =="MASCULINO":
                sexo = "M"
        elif sexo == "FEMININO":
                sexo = "F"
print("Sexo {} registrado com sucesso.!".format(sexo))
