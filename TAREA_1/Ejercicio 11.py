class EstructuraCiclicas:     
    def __init__(self):
        pass
    
    """Estructuras FOR"""
    def estCic1(self):                        #EJERCICIO 11
        i=1
        suma=0
        for i in range(100):
            suma= suma+i*i
            i+=1
        print("La suma de los 100 números es: {}" .format(suma))

clase1= EstructuraCiclicas()
clase1.estCic1()