# Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
# Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
# El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
tt = int(input('Duracción tramo: '))
tm=0
while tt!=0:
    tm+=tt
    tt = int(input('Duracción tramo: '))
print(f'Tiempo total de viaje: {tm//60}:{str(tm%60).zfill(2)} horas')
