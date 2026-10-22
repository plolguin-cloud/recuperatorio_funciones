from utils import calcular_subtotal, aplicar_descuento

totales = []

for i in range(1, 4):
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))

    subtotall = calcular_subtotal(precio, cantidad)
    total = aplicar_descuento(subtotall)
    totales.append(total)

print("Importes finales: $", totales)