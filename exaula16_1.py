estenso = ("zero", "um", "Dois", "Tres", "Quadro", "Cinco", "Seis", "Sete",
           "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze",
           "Dizesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
while True:
    c = int(input("Digite um numero entre 0 e 20: "))
    if 0 <= c <= 20:
        print(f"Você digitou o número {estenso[c]}")
        while True:
            n = str(input("Quer continuar [S/N]")).upper().strip()
            if n in "SN":
                break
            else:
                print("Digite condigo valido")
        if n == "N":
            break
    else:
        print("Tente novamente. ", end="")
