class EstructuraCiclicas:     
    def __init__(self):
        pass

    """Bucles anidados"""
    def estCic7(self):                         #EJERCICIO 17
        num= int(input("Ingrese un número: "))
        fact=1
        for i in range(1, num+1):
            fact*=i
        print("El factorial del número {} es: {}" .format(num, fact))

clase1= EstructuraCiclicas()
clase1.estCic7()