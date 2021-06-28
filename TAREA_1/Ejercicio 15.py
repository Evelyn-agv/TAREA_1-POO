class EstructuraCiclicas:     
    def __init__(self):
        pass

    def estCic5(self):    #BUCLE CONTROLADO POR BANDERAS O INTERRUPTORES          #EJERCICIO 15
        primo= True
        divisor=2
        num= int(input("Ingrese un número: "))
        while divisor<num and primo==True:
            res= num%divisor
            if res==0:
                primo= False
            divisor+=1
        if primo== True:
            print("El número {} es primo" .format(num))
        else:
            print("El número {} no es primo" .format(num))

clase1= EstructuraCiclicas()
clase1.estCic5()
