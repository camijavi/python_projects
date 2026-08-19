print("Ingrese los datos solicitados a continuacion")
a = int(input("1er número: "))
b = int(input("2do número: "))

suma = a + b 
resta = a - b
multi = a * b
potecia = a ** b 
division = a / b 
division2 = a // b # division entenra 
modulo = a % b #residuo 


print ("\nResultados de cada operación de: " + str(a) + " y " + str(b))

# Camila recuerda pasar de int a str
print("\n Suma: " + str(suma))
print(" Resta: " + str(resta))
print(" Multiplicación: " + str(multi))
print(" Potencia: " + str(potecia))
print(" División: " + str(division))
print(" División entera: " + str(division2))
print(" Residuo: " + str(modulo))
