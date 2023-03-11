mesNacimiento = int(input("Escribe tu mes de nacimiento:\n"))
diaNacimiento = int(input("Escribe tu dia de nacimiento:\n"))

if mesNacimiento >= 1 and mesNacimiento <= 12:
    if mesNacimiento == 1:
        if diaNacimiento < 20:
            print("Eres del signo Capricornio")
        elif diaNacimiento > 31:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Acuario")
    elif mesNacimiento == 2:
        if diaNacimiento < 19:
            print("Eres del signo Acuario")
        elif diaNacimiento > 29:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Piscis")
    elif  mesNacimiento == 3:
        if diaNacimiento < 21:
            print("Eres del signo Piscis")
        elif diaNacimiento > 31:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Aries")
    elif mesNacimiento == 4:
        if diaNacimiento < 20:
            print("Eres del signo Aries")
        elif diaNacimiento > 30:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Tauro")
    elif mesNacimiento == 5:
        if diaNacimiento < 21:
            print("Eres del signo Tauro")
        elif diaNacimiento > 31:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Géminis")
    elif mesNacimiento == 6:
        if diaNacimiento < 21:
            print("Eres del signo Géminis")
        elif diaNacimiento > 30:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Cancer")
    elif mesNacimiento == 7:
        if diaNacimiento < 23:
            print("Eres del signo Cancer")
        elif diaNacimiento > 31:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Leo")
    elif mesNacimiento == 8:
        if diaNacimiento < 23:
            print("Eres del signo Leo")
        elif diaNacimiento > 31:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Virgo")
    elif mesNacimiento == 9:
        if diaNacimiento < 23:
            print("Eres del signo Virgo")
        elif diaNacimiento > 30:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Libra")
    elif mesNacimiento == 10:
        if diaNacimiento < 23:
            print("Eres del signo Libra")
        elif diaNacimiento > 31:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Escorpio")
    elif mesNacimiento == 11:
        if diaNacimiento < 22:
            print("Eres del signo Escorpio")
        elif diaNacimiento > 30:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Sagitario")
    else:
        if diaNacimiento < 22:
            print("Eres del signo Sagitario")
        elif diaNacimiento > 31:
            print("Error ese dia no existe")
        else:
            print("Eres del signo Capricornio")
else:
    print("Numero de mes no existe")
