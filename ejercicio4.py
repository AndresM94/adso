#Construir un algoritmo que convierta a positivo cualquier numero digitado por pantalla.
numero = int( input("Digite un numero negativo a convertir:\n") )
if numero < 0:
    print(f"El numero {numero} convertido a positivo es: {numero * -1}")
else:
    print(f"El {numero} ya es positivo")