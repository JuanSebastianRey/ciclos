#Desarrolle un programa que permita trabajar con las potencias fraccionales de dos
f=1
i = 1
sum=0
headers = ['Potencia', 'Fracción', 'Suma']
for header in headers:
    print(header, end=' ')
print()
while f>0.000001:
    f=1/(2**i)
    sum+=f
    print(str(i).ljust(8), end=' ')
    print(str(round(f,4)).ljust(8), end=' ')
    print(round(sum,4))
    i+=1

