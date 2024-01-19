# Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:
nr = int(input('Ingrese un numero: \n'))
for i in range(10):
    print(f'{nr} x {i+1} = {nr*(i+1)}')