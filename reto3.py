nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso en kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = peso / (estatura ** 2)

print("Nombre: ", nombre)
print("Peso: ", peso)
print("Estatura: ", estatura)
print("IMC:", round(imc, 2))
