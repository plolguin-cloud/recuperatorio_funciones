def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(subtotal):
    if subtotal >= 20000:
        return subtotal * 0.90
    return subtotal