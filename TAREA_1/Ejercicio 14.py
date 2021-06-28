class EstructuraCiclicas:     
    def __init__(self):
        pass

    def estCic4(self):    #BUCLE CONTROLADO POR CONDICIÓN         #EJERCICIO 14
        sum=0
        prod=1
        num= int(input("Ingrese un número: "))
        while num!=-1:
            sum= sum+num
            prod= prod*num
            print("El total de la suma es: {}" .format(sum))
            print("El total del producto es: {}" .format(prod))
            num= int(input("Ingrese un número: "))

clase1= EstructuraCiclicas()
clase1.estCic4()
