mayor = -10000
menor = 10000
numero1 = int(input("digite un número:\n"))

if numero1 > mayor:
    mayor = numero1

if numero1 < menor:
    menor = numero1

numero2 = int(input("digite un número:\n"))
if numero2 > mayor:
    mayor = numero2

if numero2 < menor:
    menor = numero2
numero3 = int(input("digite un número:\n"))
if numero3 > mayor:
    mayor = numero3

if numero3 < menor:
    menor = numero3
numero4 = int(input("digite un número:\n"))
if numero4 > mayor:
    mayor = numero4

if numero4 < menor:
    menor = numero4
numero5 = int(input("digite un número:\n"))
if numero5 > mayor:
    mayor = numero5

if numero5 < menor:
    menor = numero5
numero6 = int(input("digite un número:\n"))

if numero6 > mayor:
    mayor = numero6

if numero6 < menor:
    menor = numero6

print(f"El numero menor es: {menor}, el numero mayor es: {mayor}")

# punto 2:
unidades = int(input("Digite la cantidad de discos comprados:\n"))
costoUnidad = 0
costoVendedor = 0.25

if unidades >= 1 and unidades <= 9:
    costoUnidad = 0.35

elif unidades>= 10 and unidades <= 99:
    costoUnidad = 0.34

elif unidades >= 100 and unidades <= 499:
    costoUnidad = 0.3

elif unidades >= 500:
    costoUnidad = 0.28

costoTotal = costoVendedor * unidades
precioCliente = costoUnidad * unidades
ganancia = precioCliente - costoTotal

print(f"El precio para el cliente es: ${precioCliente}, El costo total es: ${costoTotal} y la ganancia es: ${ganancia:.2f}")

