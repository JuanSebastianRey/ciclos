#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:
h = int(input('Ingrese la altura:\n'))
w = int(input('Ingrese el ancho:\n '))

for i in range(h):
    for j in range(w):
        print('*', end='')
    print()