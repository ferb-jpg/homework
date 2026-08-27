# ¿Qué es una variable?
# Una variable es un espacio donde podemos guardar un valor.
# Ese valor puede cambiar y tomar diferentes valores según se necesite en el programa.

# Ejemplo:
nombre = "Juan"
edad = 25


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2

print("Suma:", suma)
print("Resta: ", resta)
print("Multiplicación: ", mult)
print("División: ", div)

#Actividad de análisis
#Observe el siguiente código:
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
nueva_edad = edad + 5
print(nombre)
print(nueva_edad)

#1. ¿Qué problema presenta el código?
#R// el código presenta un error en la línea de código numero 2, ya que “edad” se esta guardando como texto por que input() devuelve una cadena, entonces no se puede hacer “nueva_edad = edad + 5” porque se esta intentando sumar un numero con un texto

#2. ¿Qué tipo de dato devuelve input()?
#R// devuelve un dato tipo cadena de texto

#3. ¿Cómo se puede corregir?
#R// convirtiendo la edad en numero usando int()

#4. Escriba el código corregido
#R//

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nueva_edad = edad + 5
print(nombre)
print(nueva_edad)
