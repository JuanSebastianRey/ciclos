#Escriba un programa que entregue todos los divisores del número entero ingresado:
n = int(input('Ingrese nmero: \n'))
d = []
for i in range(1,int(n**0.5)):
    if n%i==0:
        d.append(i)
for d in reversed(d):
    d.append(n/d)
print(d)