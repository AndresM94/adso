nombreCliente = input("Cual es tu nombre?\n")
cantidadProductos = int(input("Cantidad de productos a registrar:\n"))

productos = []
preciosProductos = []
precioTotal = 0

for i in range(cantidadProductos):
    nombreProducto = input(f"Digite nombre del producto {i+1}:\n")
    precioProducto = float(input(f"Digite el precio de {nombreProducto}:\n"))
    productos.append(nombreProducto)
    preciosProductos.append(precioProducto)
    
print(f"Buenas Tardes, {nombreCliente} tus productos son:\n")

for l in range(cantidadProductos):
    print(f"Producto {l+1}: {productos[l]}, precio: ${preciosProductos[l]}")
    precioTotal = precioTotal + preciosProductos[l]
    
promedio = precioTotal/cantidadProductos

print(f"El promedio es: $", format(promedio, ","))