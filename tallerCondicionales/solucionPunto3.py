"""
Solucion punto 3:
"""

pregunta1 = input("¿Estudiaste para el examen?\n")

if pregunta1.lower() == "si":
    pregunta2 = input("¿Aprobó el examen?\n")
    if pregunta2.lower() == "si":
        pregunta3 = float( input("¿Cuanto fue tu nota entre 0 a 5?\n") )
        if pregunta3 >= 0 and pregunta3 <= 5:
            if pregunta3 >=3.5:
                pregunta4 = input("¿Ya terminó semestre?\n")
                if pregunta4.lower() == "si":
                    print("Felicitaciones!!!")
                else:
                    print("Continúa así...")
            else:
                if pregunta3 > 2.0:
                    print("Casi lo logras...")
                else:
                    print("Debes esforzarte mucho más...")
        else:
            print("Rango de nota invalido")
    else:
        print("Estudiar más...")