import math
grau = float(input('digite um grau! '))
radi = math.radians(grau)
print("seno de {0} = {1:.2f}"
"\nconsceno de {0} = {2:.2f}"
"\ntangente de {0} = {3:.2f}".format(grau,(math.sin(radi)),(math.cos(radi)),(math.tan(radi))))