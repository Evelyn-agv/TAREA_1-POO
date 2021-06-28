class EstructuraSelectivas:     #ESTRUCTURAS SELECCIÓN
    def __init__(self):
        pass

    """Estructuras selectivas compuestas"""       
    def estSel4(self):                             #EJERCICIO 7
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

clase1= EstructuraSelectivas()
clase1.estSel4()
