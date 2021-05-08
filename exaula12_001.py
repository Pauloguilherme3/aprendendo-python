from time import sleep
valor_casa = float(input("\033[0:33:40m Digite o valor da casa: "))
Salario = float(input("\033[0:32:40m Digite o valor do seu salario: "))
anos = int(input("\033[0:34:40m Digite em quantos anos quer parcelar: "))
media = valor_casa/(anos*12)
print("\033[7:0:40m Processando...")
print("*-"*20)
sleep(2)
print("\033[7:0:40m O valor da parcela ficaria R${:.2fdd} reias por mes\033[0m".format(media))
sleep(2)
print("\033[7:0:40mAnalisando seu pedido de financiamento.")
print("*-"*20,"\033[0m")
if media > Salario*0.3:
    print("\033[30:41m Infelismente você nao pode comprar essa casa!!\033[0m")
else:
    print("\033[30:42m Parabéns seu financiamento foi aprovado\033[0m")