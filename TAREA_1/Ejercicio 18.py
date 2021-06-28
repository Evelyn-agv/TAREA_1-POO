class Arreglos:    
    def __init__(self):
        pass

    def arr1(self):             #Arreglos en una dimensión        #EJERCICIO 18
        calificaciones = []
        for i in range(10):
            nuevoDato = int( input( "Dime el dato numero {}: ".format(i)))
            calificaciones.append(nuevoDato)
        print("Las calificaciones son: {}".format(calificaciones))

class1= Arreglos()
class1.arr1()
