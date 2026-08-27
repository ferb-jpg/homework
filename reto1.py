nombre = input("Ingrese su nombre: ")
horas = float(input("Ingrese su cantidad de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de cada hora: "))

salario = horas * valor_hora

print("Empleado: ", nombre)
print("Horas trabajadas: ", horas)
print("Valor por hora: $", valor_hora)
print("Salario: $", salario)
