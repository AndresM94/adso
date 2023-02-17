opcion = int( input("""¿Cual es tu deporte favorito?
Escoja una opcion:
    1. Futbol
    2. Voleybol
    3. Basquet 
    4. Sóftbol\n""") )

if opcion == 1:
    pregunta = int( input("¿Cuantos jugadores conforman el equipo de futbol? \n") )
    if pregunta == 11:
        print("La respuesta es correcta")
    else:
        print(f"La respuesta es incorrecta, la respuesta correcta es: 11")
elif opcion == 2:
    pregunta = int( input("¿Cuantos jugadores conforman el equipo de Volebol? \n") )
    if pregunta == 6:
        print("La respuesta es correcta")
    else:
        print("La respuesta es incorrecta, la respuesta correcta es: 6")
elif opcion == 3:
    pregunta = int( input("¿Cuantos jugadores conforman el equipo de Basquet? \n") )
    if pregunta == 5:
        print("La respuesta es correcta")
    else:
        print(f"La respuesta es incorrecta, la respuesta correcta es: 5")
elif opcion == 4:
    pregunta = int( input("¿Cuantos jugadores conforman el equipo de Sóftbol? \n") )
    if pregunta == 10:
        print("La respuesta es correcta")
    else:
        print("La respuesta es incorrecta, la respuesta correcta es: 10")
else:
    print("El numero esta fuera de la lista")