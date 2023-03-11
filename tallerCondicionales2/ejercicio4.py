horas_normales = 0
horas_nocturnas = 0

valor_hora = float(input("Ingrese el valor de la hora de trabajo: "))
hora_inicio = int(input("Ingrese la hora de inicio (entre 6 y 15): "))
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas (máximo 8 horas): "))
dias_trabajados = int(input("Ingrese la cantidad de días trabajados: "))

if hora_inicio < 6 or hora_inicio > 15:
    print("Hora de inicio inválida")
elif horas_trabajadas > 8:
    print("Cantidad de horas trabajadas inválida")
else:
    if hora_inicio + horas_trabajadas > 18:
        horas_normales = horas_trabajadas - ((hora_inicio + horas_trabajadas) - 18)
        horas_nocturnas = horas_trabajadas - horas_normales
    else:
        horas_normales = horas_trabajadas
        
    total_horas_normales = horas_normales * valor_hora
    total_horas_nocturnas = horas_nocturnas * (valor_hora * 1.1)
    total_pago = total_horas_normales + total_horas_nocturnas

    print(f"Total a pagar por horas trabajadas antes de las 6pm: ${total_horas_normales}")
    print(f"Total a pagar por horas trabajadas después de las 6pm: ${total_horas_nocturnas}")
    print(f"Total a pagar por día: ${total_pago}")
    print(f"Total a pagar por los {dias_trabajados} días trabajados: ${total_pago * dias_trabajados}")
