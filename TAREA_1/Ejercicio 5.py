class EstructuraSelectivas:     #ESTRUCTURAS SELECCIÓN
    def __init__(self):
        pass

    """Estructuras selectivas dobles"""           
    def estSel2(self):                            #EJERCICIO 5
        cali= float(input("Ingrese la calificación del examen que obtuvo el estudiante: "))
        if cali >=7:
            print("La nota es {}, APROBADO" .format(cali))
        else:
            print("La nota es {}, REPROBADO" .format(cali))

clase1= EstructuraSelectivas()
clase1.estSel2()
