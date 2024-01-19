#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.
n1= int(input('Ingre num: '))
n2= int(input('Ingrese num: '))
suma=0
for i in range(n1+1,n2):
    suma += i
print(f'La suma es {suma}')