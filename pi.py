#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:
n = int(input('n:\n '))
su=0
for i in range(n):
    su+=(-1)**(i)*(1/(2*i+1))
pi = 4 * su
print(pi)