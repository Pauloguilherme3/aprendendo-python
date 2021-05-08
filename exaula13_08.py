frase = str(input("Digite uma frase: ")).replace(" ","").upper()
if frase == frase[::-1]:
    print('A frase digitada não e um palidrome {} {}'.format(frase,frase[::-1]))
else:
    print("A frase digitada não e um palidrome {} {}".format(frase,frase[::-1]))
