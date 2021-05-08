print("="*30)
print("="*7, "SUPER BARATAO", "="*8)
print("="*30)
nomeprodutomaisbarato = ""
contaprecomaisde = precomaisbarato = contatotal = 0
while True:
    nome = str(input("Qual nome do produto: ")).strip()
    preco = float(input("Preço: R$"))
    if preco > 1000:
        contaprecomaisde += 1
    elif preco < precomaisbarato or precomaisbarato == 0:
        precomaisbarato = preco
        nomeprodutomaisbarato = nome
    contatotal += preco
    controle = " "
    while controle not in "SN":
        controle = str(input("Quer continuar [S/N]: ")).strip().upper()
    if controle == "N":
        break
print("-"*6, "Fim Do Programa", "-"*6)
print(f"O total da compra foi R${contatotal:.2f}")
print(f"Temos {contaprecomaisde} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi (o/a) {nomeprodutomaisbarato} que custa R${precomaisbarato:.2f}")
