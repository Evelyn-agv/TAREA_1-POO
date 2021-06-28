class EstructuraSelectivas:     #ESTRUCTURAS SELECCIÓN
    def __init__(self):
        pass

    def estSel3(self):                           #EJERCICIO 6
        SueldI= float(input("Ingrese el sueldo que poseía: "))
        if SueldI <= 600:
            NuevoS= SueldI+(SueldI*0.1)
            print("Su nuevo sueldo es {}" .format(NuevoS))
        else:
            NuevoS= SueldI
            print("Su sueldo sigue siendo {}" .format(NuevoS))

clase1= EstructuraSelectivas()
clase1.estSel3()
