r1 = int(input("digite valor primera reta! "))
r2 = int(input("digite valor segunda reta! "))
r3 = int(input("digite valor terceira reta! " ))
if r1+r2 > r3 and r1+r3 > r2 and r3+r2 > r1:
    print("E possivel fazer um triangulo!")
else:
    print("Não e possivel fazer um triangulo!")