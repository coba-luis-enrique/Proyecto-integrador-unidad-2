
"""se define la clase"""

class leernombres:  #operaciones (identacion)

    def __init__(self,Lista_A, verificar):
        self.Lista_A=Lista_A
        self.verificar=verificar

    def ordenamiento(self):
        self.Lista_A.sort()
        print(self.Lista_A)
        if len(self.Lista_A)<= 0:
            return 0
        else:
            return print(''.join(self.Lista_A[0:]))

    def busqueda(self):
        palabra = input("escriba un nombre: ")
        linea= (''.join(self.Lista_A[0:]))

        if len(self.Lista_A) <= 0:
            return 0
        else:
                if palabra in linea:
                    print(palabra, "se encuentra en la lista")
                else:
                    print(palabra, "no se encuentra en la lista")
