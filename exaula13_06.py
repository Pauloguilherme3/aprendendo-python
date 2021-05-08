t = int(input("Digite o termo: "))
r = int(input("Digite a Razão: "))
d = (t+(10 -1)*r)+r
for c in range(t,d,r):
    print(c, end = "-->")
print("ACABOU")
