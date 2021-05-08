d =0
f =0
for c in range(0,6):
    s = int(input("Qual numero: "))
    if s % 2 == 0 :
        d+=s
        f+=1
print("Voce informou {} números pares e a soma foi{}".format(d,f))