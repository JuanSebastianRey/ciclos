#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:
n = int(input('Ingrese un numero: \n'))
for i in range(n+1):
    print(f'{2**(i)}', end=' ')