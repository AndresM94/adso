"""
Solucion punto 5:
"""

hora1 = int( input("Ingrese la hora del primero:\n") )
min1 = int( input("Ingrese los minutos del primero\n") )

hora2 = int( input("Ingrese la hora del primero\n") )
min2 = int( input("Ingrese los minutos del segundo\n") )

if hora1 <= 23 and hora1 >= 0 and hora2 <= 23 and hora2 >= 0 and min1 <= 59 and min1 >= 0 and min2 <= 59 and min2 >= 0:
    if hora1 == hora2:
        if min1 == min2:
            print(f"La primera hora {hora1}:{min1} es igual a la segunda hora {hora2}:{min2}")
        elif min1 > min2:
            print("La hora 1 es mayor a la hora 2")
        else:
            print("La hora 1 es menor a la hora 2")
    elif hora1 > hora2:
        print("la hora 1 es mayor a la hora 2")
    else:
        print("La hora 1 es menor que la hora 2")
else:
    print("La hora es invalida")