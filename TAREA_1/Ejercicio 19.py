class Arreglos:    
    def __init__(self):
        pass

    def arr2(self):             #Arreglos en una dimensión       #EJERCICIO 19
        nuevo = []
        B=[]
        A= []
        print(nuevo)
        for j in range(0,20):
            num = int(input("Ingrese un número: "))
            nuevo.append(num)
        for j in nuevo:
            if j >= 0:
                B.append(j)
            else:
                A.append(j)
        print("Los números positivos son: {}".format(B))
        print("Los números negativos son: {}".format(A))

class1= Arreglos()
class1.arr2()
