class EstructuraSelectivas:     #ESTRUCTURAS SELECCIÓN
    def __init__(self):
        pass

    """Estructuras selectivas múltiples"""
    def estSel6(self):                            #EJERCICIO 9
        v1= int(input("Ingrese un número: "))
        v2= int(input("Ingrese un valor: "))
        if v1== 1:
            Resp= 100*v2
        elif v1== 2:
            Resp= 100**v2
        elif v1== 3:
            Resp= 100/v2
        else:
            Resp= 0
        print("El resultado del número {} y el valor {} es de: {} ".format(v1,v2, Resp))

clase1= EstructuraSelectivas()
clase1.estSel6()
