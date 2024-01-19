#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.
import math
de=2
di=1
eu = 2
previous = 1
fra = 1
while di>0.0001:
    previous = fra
    fra= 1/math.factorial(de)
    de += 1
    eu += fra
    di= previous-fra
print(eu)