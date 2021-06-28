class EstructuraSelectivas:     #ESTRUCTURAS SELECCIÓN
    def __init__(self):
        pass

    """Estructuras selectivas simples"""         #EJERCICIO 4
    def estSel1(self): 
        calif= float(input("Ingrese la calificación del examen que obtuvo el estudiante: "))
        if calif >=7:
            print("La nota es {}, APROBADO" .format(calif))

clase1= EstructuraSelectivas()
clase1.estSel1()

