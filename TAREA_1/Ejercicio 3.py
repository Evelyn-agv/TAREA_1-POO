class EstructuraSecuenciales:      #ESTRUCTURAS SECUENCIALES
    def __init__(self):
        pass

    def estSec2(self):                   #EJERCICIO 3
        SueldoB= float(input("Ingrese su sueldo base: "))
        venta1= float(input("Ingrese el valor de su primera venta: "))
        venta2= float(input("Ingrese el valor de su segunda venta: "))
        venta3= float(input("Ingrese el valor de su tercera venta: "))
        TotV= venta1+venta2+venta3
        Comision= TotV*0.1
        TotR= SueldoB+Comision
        print("Su sueldo base es {}, mas las ventas realizadas {}, usted recibirá un total {}" .format(SueldoB,TotV,TotR))

clase1= EstructuraSecuenciales()
clase1.estSec2()