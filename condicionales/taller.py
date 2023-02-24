#Solcucion punto 1:
def ecuacion(x, y):
    formula1 = x + 3 * y
    formula2 = 2 * x - 5 * y
    if formula1 == formula2:
        print("Es correcto los valores de X y Y")
    else:
        print("Es incorrecto")

#solucion punto 2:
def horasFormato12(h1, m1, mer1, h2, m2, mer2):
    if 0 < h1 <= 12 and 0 < h2 <= 12 and 0 <= m1 <= 59 and 0 <= m2 <= 59:
        if mer1.upper() == mer2.upper():
            if h1 == h2 and m1 == m2:
                print(f"la hora {h1}:{m1} {mer1} es igual a {h2}:{m2} {mer2}")
            elif h1 >= h2:
                print(f"la hora {h1}:{m1} {mer1} es mayor a {h2}:{m2} {mer2}")
            else:
                print(f"La hora {h1}:{m1} {mer1} es menor a {h2}:{m2} {mer2}")
        elif mer1 == "PM" and mer1 != mer2:
            print(f"la hora {h1}:{m1} {mer1} es mayor a {h2}:{m2} {mer2}")
        else:
            print(f"La hora {h1}:{m1} {mer1} es menor a {h2}:{m2} {mer2}")
    else:
        print("El formato no existe")

#solucion punto 3:
def formato24H(h1, m1, h2, m2):
    if 0 <= h1 <= 23 and 0 <= h2 <= 23 and 0 <= m1 <= 59 and 0 <= m2 <= 59:
        if h1 == h2 and m1 == m2:
            print(f"La hora {h1}:{m1} es igual a {h2}:{m2}")
        elif h1 >= h2:
            if m1 > m2:
                print(f"La hora 1 es mayor a la hora 2")
            else:
                print("la hora 1 es menor a la hora 2")
        else:
            print("la hora 1 es menor a la hora 2")
    else:
        print("Formato no valido")   



#Solucion punto 4:
def redondeo(num):
    result = int(num)
    if num > result + 0.5:
        print(result+1)
    else:
        print(result)
        


#Solucion punto 5:
def dibujar(dibujo):
    if dibujo == 1:
        print("""
        * * * * *
        *       *
        *       *
        * * * * *""")
    elif dibujo == 2:
        print("""
        * * * * * *
        *         *
        *         *
        * * * * * *""")
    elif dibujo == 3:
        print("""
                *
              *   *
            *       *
          *           *
        * * * * * * * * *""")
    elif dibujo == 4:
        print("* * * * * * * * *")

solucion = int( input("Elige la el numero de la solucion que desea probar del 1 al 5:\n") )
if solucion == 1:
    #Solcucion punto 1:
    valor1 = int( input("Digite el valor de x: ") )
    valor2 = int( input("Digite el valor de y: ") )
    #llamo a la funcion y le paso como parametro cada variable de entrada
    ecuacion(valor1, valor2)
elif solucion == 2:
    #solucion punto 2:
    hora1 = int( input("Digite la hora del primero 1 a 12:\n") )
    minutos1 = int( input("Digite los minutos\n") )
    meridiano1 = input("Diprint(result)gite si es AM o PM:\n")

    hora2 = int( input("Digite la hora del segundo 1 a 12:\n") )
    minutos2 = int( input("Digite los minutos del segundo:\n") )
    meridiano2 = input("Digite si es AM o PM:\n")
    #llamo a la funcion y le paso como parametro cada variable de entrada
    horasFormato12(hora1, minutos1, meridiano1, hora2, minutos2, meridiano2)
elif solucion == 3:
    #solucion punto 3:
    print("Ingrese las horas en formato militar:")
    hora1 = int( input("Ingrese la hora 1: ") )
    min1 = int( input("Ingrese el minuto 1: ") )
    hora2 = int( input("Ingrese la hora 2: ") )
    min2 = int( input("Ingrese el minuto 2: ") )
    #llamo a la funcion y le paso como parametro cada variable de entrada
    formato24H(hora1, min1, hora2, min2)
elif solucion == 4:
    #Solucion punto 4:
    numero = float( input("Digite un numero decimal: ") )
    #llamo a la funcion y le paso como parametro cada variable de entrada
    redondeo(numero)
elif solucion == 5:
    #Solucion punto 5:
    eleccion = int( input("""Elige el numero de la figura que desea dibujuar:
  1. Cuadrado
  2. Rectangulo
  3. Triangulo
  4. Linea\n""") )
    #llamo a la funcion y le paso como parametro cada variable de entrada
    dibujar(eleccion)
else:
    print(f"Solucion #{solucion} no existe")
