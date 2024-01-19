#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:
h = int(input('Ingrese la altura:\n'))

for i in range(h):
    for j in range(i+1):
        print('*', end='')
    print()