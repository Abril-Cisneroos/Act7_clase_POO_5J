print("Programacion POO")
# definicion de clase 

class Perro:
    #Funciones dentro de la clase
    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self,nombre,edad):
        print(f"Nombre: {nombre} edad: {edad}")

#zona de creacion de objetos

pitbull=Perro()



# zona de uso de objetos

pitbull.Datos_perro("Boby",4)
pitbull.morder()