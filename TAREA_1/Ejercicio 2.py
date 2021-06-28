class EstructuraSecuenciales:      #ESTRUCTURAS SECUENCIALES
    def __init__(self):
        pass
    
    def estSec1(self):                   #EJERCICIO 2
        TotC= float(input("Ingrese el total de la compra: "))
        Descuento= TotC*0.15
        ValorP= TotC-Descuento
        print("El total de la compra es {}, su valor a pagar es {}" .format(TotC,ValorP))

clase1= EstructuraSecuenciales()
clase1.estSec1()
