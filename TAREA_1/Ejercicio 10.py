class EstructuraSelectivas:     #ESTRUCTURAS SELECCIÓN
    def __init__(self):
        pass

    """Expresiones lógicas"""  #USO DE "AND" "OR"
    def estSel7(self):                                #EJERCICIO 10
        C1= int(input("Ingrese la primera calificación: "))
        C2= int(input("Ingrese la segunda calificación: "))
        if C1 >=80 and C2>=80:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(C1,C2))
        else:
            print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(C1,C2))
    

    def estSel8(self):
        C1= int(input("Ingrese la primera calificación: "))
        C2= int(input("Ingrese la segunda calificación: "))
        if C1 >=90 or C2>=90:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(C1,C2))
        else:
            print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(C1,C2))

clase1= EstructuraSelectivas()
clase1.estSel7()
clase1.estSel8()
    