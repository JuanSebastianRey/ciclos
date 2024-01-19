#Escriba un programa que muestre una tabla de multiplicar con los numeros alineados a la derecha
for i in range(1,11):
    for j in range (1,11):
        producto = str(i*j)
        if j==10:
            out=producto.rjust(3)
        else:
            out=producto.rjust(2)
        print(out, end=' ')
    print()