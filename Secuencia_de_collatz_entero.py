#Desarrolle un programa que entregue la secuencia de Collatz de un número entero
n = int(input('n: '))
while n!=1:
    print(int(n), end=' ')
    if n%2==0:
        n /= 2
    else:
        n = n*3+1
print(1)