"""
Soucion punto 1:
"""

hora1Program = float( input("Cuantas horas tardo en terminar el primer programa:\n") )
lineas1Program = float( input("Cuantas cuantas lineas uso para terminar el primer programa:\n") )
costo1 = (lineas1Program / hora1Program) * 20000
precio1 = costo1 + (costo1 * 0.1)

hora2Program = float( input("Cuantas horas tardo en terminar el segundo programa programa:\n") )
lineas2Program = float( input("Cuantas cuantas lineas uso para terminar el segundo programa programa:\n") )
costo2 = (lineas2Program / hora2Program) * 20000
precio2 = costo2 + (costo2 * 0.1)

hora3Program = float( input("Cuantas horas tardo en terminar el tercer programa:\n") )
lineas3Program = float( input("Cuantas cuantas lineas uso para terminar el tercer programa:\n") )
costo3 = (lineas3Program / hora3Program) * 20000
precio3 = costo3 + (costo3 * 0.1)

print(f"El precio del primer programes es: ${precio1}\nEl precio del segundo programa es: ${precio2}\nEl precio del tercer programa es: ${precio3}")