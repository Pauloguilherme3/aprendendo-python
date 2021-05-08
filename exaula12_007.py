n = int(input("primeira reta: "))
n2 = int(input("Segunda reta: "))
n3 = int(input("Terceira reta: "))
test1= n  + n2 >n3
test2= n  + n3 >n2
test3= n2 + n3 >n
if test1 and test2 and test3:
    print("E possivel fazer um triangulo ",end ='')
    if  n != n2 != n3:
        print("triangulo Esacaleno")
    elif n == n2 == n3:
        print("triangulo Equilátero")
    else:
        print("Triangulo Isosceles")
else:
    print("Não e possivel fazer um triangulo")