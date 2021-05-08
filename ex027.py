c =  int(input("Primeiro numero! "))
b =  int(input("Secundo numero! "))
a =  int(input("Terceiro numero! "))
menor = a
maior = b
if c<b and c<a:
    menor = c
if b<c and b<a:
    menor = b
if a>c and a>b:
    maior = a
if c>b and c>a:
    maior = c
print("O {} é maior é {} é menor".format(maior,menor))

