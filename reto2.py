nombre = input("Nombre del cliente: ")
comida = float(input("Digite el valor de la comida: "))
bebidas = float(input("Digite el valor de las bebidas: "))

subtotal = comida + bebidas
propina = subtotal * 0.10
total = subtotal + propina

print("----- FACTURA -----")
print("Cliente: ", nombre)
print("Subtotal: $", subtotal)
print("Propina (10%): $", propina)
print("Total a pagar: $", total)
