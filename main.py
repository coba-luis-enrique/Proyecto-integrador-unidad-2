from operaciones import *

archivo = open('lista.txt', 'r')
leer_fila = archivo.readlines()
archivo.close()

b=False
prototipo=leernombres(leer_fila,b)

print("\n1.- ordenamiento de nombres: ")
print ("2.-Busqueda de nombres")
opcion=int(input("seleccione una opcion: "))

if opcion==1:
    prototipo.ordenamiento()
elif opcion==2:
    prototipo.busqueda()
else:
    print("Opcion incorrecta...")
