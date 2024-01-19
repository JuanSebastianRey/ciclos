#Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:
s=int(input('Lado: '))
f = s + 2*(s-1)
for i in range(s):
    fi=''
    for j in range(s+2*i):
        fi+='*'
    print(fi.center(f))
for x in range(1,s):
    fi=''
    for j in range(2,s+2*(s-x),1):
        fi+='*'
    print(fi.center(f))
