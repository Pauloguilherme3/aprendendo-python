a = int(input("Digite um numero: "))
b = 0
for c in range(1,a+1):
    if a % c == 0:
        b+=1
        print("\033[33m[{}]".format(c),end = " ")
    else:
        print("\033[31m{}".format(c),end= " ")
if 2 > b or b > 2:
    print("\n\033[mO numero {} é divisivel por {} numeros,\npor isso não e um numero  primo!!".format(b,a))
else:
    print("\n\033[mO numero {} é divisivel por {} vezes, \npor isso um numero primo!!".format(b,a))
