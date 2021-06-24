class EstructuraSelectivas:     #ESTRUCTURAS SELECCIÓN
    def __init__(self):
        pass
    
    """Estructuras selectivas simples"""
    def estSel1(self):
        calif= float(input("Ingrese la calificación del examen que obtuvo el estudiante: "))
        if calif >=7:
            print("La nota es {}, APROBADO" .format(calif))
    
    
    """Estructuras selectivas dobles"""
    def estSel2(self):
        cali= float(input("Ingrese la calificación del examen que obtuvo el estudiante: "))
        if cali >=7:
            print("La nota es {}, APROBADO" .format(cali))
        else:
            print("La nota es {}, REPROBADO" .format(cali))
    

    def estSel3(self):
        SueldI= float(input("Ingrese el sueldo que poseía: "))
        if SueldI <= 600:
            NuevoS= SueldI+(SueldI*0.1)
            print("Su nuevo sueldo es {}" .format(NuevoS))
        else:
            NuevoS= SueldI
            print("Su sueldo sigue siendo {}" .format(NuevoS))
    

    """Estructuras selectivas compuestas"""
    def estSel4(self):
        hort= int(input("Ingrese las horas que trabajó: "))
        pagh= float(input("Ingrese el pago de la hora normal: "))
        if hort > 40:
            he= hort-40
            if he > 8:
                het= he-8
                paghe= (pagh*2*8) + (pagh*3*het)
            else:
                paghe= pagh*2*he
            pagt= pagh*40+paghe
        else:
            pagt= pagh*hort
        print("El pago total por las horas trabajadas es {}" .format(pagt))
    

    def estSel5(self):
        num1= int(input("Ingrese el primer número: "))
        num2= int(input("Ingrese el segundo número: "))
        num3= int(input("Ingrese el tercer número: "))
        if num1> num2 and num1> num3:
            print("El número mayor es {}" .format(num1))
        elif num2> num1 and num2> num3:
            print("El número mayor es {}" .format(num2))
        else:
            print("El número mayor es {}" .format(num3))
    
    
    """Estructuras selectivas múltiples"""
    def estSel6(self):
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
    
    
    """Expresiones lógicas"""  #USO DE "AND" "OR"
    def estSel7(self):
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
clase1.estSel1()
clase1.estSel2()
clase1.estSel3()
clase1.estSel4()
clase1.estSel5()
clase1.estSel6()
clase1.estSel7()
clase1.estSel8()
