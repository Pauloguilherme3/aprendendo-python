produto = float(input('Qual valor do produto? R$'))
forma = ["Dinheiro/Cheque","cartão"]
pag = int(input("""Formas de Pagamento:
Digite [1] para pagamento em Dinheiro ou Cheque:10% de desconto 
Digite [2] para pagamento a vista no cartão 5% de desconto
Digite [3] para pagamento no cartao 2x preço normal
Digite [4] para pagamento no cartao 3x ou mais no cartao 20% juros 
Qual opção? """))
if 1 <= pag <=4:
  if pag == 1:
     resultado ="{:.2f} com desconto de 10%".format(produto*0.90)
     forpag =0
  elif pag == 2:
     resultado ="{:.2f} com desconto de 5%".format(produto*0.95)
     forpag =1
  elif pag == 3:
     resultado ="{:.2f} parcelado em 2x de R${:.2f} por mês".format(produto,produto/2)
     forpag =1
  elif pag == 4:
     parcelas = int(input("Quantas parcelas: "))
     forpag =1
     juros = produto *1.2
     resultado ="{:.2f} parcelado em {}x de R${:.2f} por mês".format(juros,parcelas,juros/parcelas)
  print("O Produto no Valor R${:.2f} no {} ficara R${}".format(produto, forma[forpag], resultado))
else:
    print("Opção invalida")


