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