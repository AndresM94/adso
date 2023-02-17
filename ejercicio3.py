horaPrecio = 5000

nombreEmpleado = input("Digite su nombre: \n")
dias = int(input("Cuantos dias trabajo: \n"))
horas = int(input("Cuantas horas trabajo: \n"))

sueldoTotal = dias * (horas * horaPrecio)

print(f'El sueldo de {nombreEmpleado} es: ${sueldoTotal}')