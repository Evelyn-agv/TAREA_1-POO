class Arreglos:    
    def __init__(self):
        pass

    def arr3(self):            #Arreglos en dos dimensiones         #EJERCICIO 20
        notas_lista = []
        alumnos_lista = []
        ALUMNOS = 30
        CASILLAS_NOTAS = 6
        promedio_examenes = []
        
        for alumno in range(1, 31):
            """Lectura de los 30 alumnos."""
            alum_temporal = input('Nombre del alumno {}: '.format(alumno))
            alumnos_lista.append(alum_temporal)
            for nota in range(1, 7):
                print('Escriba la calificación del alumno "{}" en el exámen "{}"'.format(alum_temporal, nota))
                """Lectura de las 6 calificaciones de los 30 alumnos."""
                notas_temporal = round(float(input('Nota #{}: '.format(nota))), 2)
                if nota == 1:
                    notas_lista.append([notas_temporal])
                else:
                    notas_lista[alumno-1].append(notas_temporal)
            print('')
        
        """Calculo promedio de calificaciones de cada uno de los exámenes."""
        for numero_examen in range(6):
            suma_notas = 0
            for nota in notas_lista:
                suma_notas += nota[numero_examen]
            promedio = round((suma_notas/ALUMNOS), 2)
            print('Promedio de exámen {}: {}'.format(numero_examen+1, promedio))
        
        """Cálculo del promedio de cada alumno."""
        print('')
        for numero, alumno in enumerate(alumnos_lista):
            suma_notas = sum(notas_lista[numero])
            promedio = round((suma_notas/CASILLAS_NOTAS), 2)
            print('{} su promedio es: {}'.format(alumno, promedio))
            
        """Cálculo del tipo de exámen que tuvo mayor promedio de calificación."""
        prom_mayor = 0
        for numero_examen in range(6):
            suma_notas = 0
            for nota in notas_lista:
                suma_notas += nota[numero_examen]
            promedio = round((suma_notas/ALUMNOS), 2)
            if prom_mayor < promedio:
                prom_mayor = promedio
            promedio_examenes.append(promedio)
        print('')
        print('El exámen', promedio_examenes.index(prom_mayor)+1,'obtuvo el mayor promedio:', prom_mayor)

class1= Arreglos()
class1.arr3()