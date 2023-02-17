num = int(input("Digite un numero entero: \n"))

if num % 2 == 0:
    if num >= 0:
        print(f"El numero {num} es par y positivo")
    else:
        print(f"El numero {num} es par y negativo")
else:
    print(f"El numero {num} es impar y multiplicado por 3 es {num*3}")