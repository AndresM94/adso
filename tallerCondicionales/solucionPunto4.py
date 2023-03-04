"""
Solucion punto 4:
"""

interesados = int( input("¿Cuantos personas estan interesadas en ADSI?\n") )
if interesados >= 0:
    if interesados >= 25:
        print("Se abre curso d ADSI")
    else:
        print(f"No se abre curso, por que faltaron {25-interesados} personas para poder abrir el curso")
else:
    print("Numero de personas invalido")