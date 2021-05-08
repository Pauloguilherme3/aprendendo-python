lista = (int(input('Digite um valor :')),
         int(input('Digite outro valor :')),
         int(input('Digite mais um valor :')),
         int(input('Digite mais outro valor :'))
         )
listapar = [x for x in lista if x % 2 == 0]
print(f"Apareceu {lista.count(9)} vezes o valor 9")
print(f"Foi digitado o 3 na posição {lista.index(3)+1}"
      if 3 in lista else "Não foi digitado nenhum numero 3")
print(f"Os numeros pares sao {listapar}")
