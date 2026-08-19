
print("Ingresa los datos solicitados para generar su factura: ")
producto = input("Nombre del producto: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad

print("\n --- FACTURA ---")
print("\n--- RESUMEN DE TU COMPRA ---")
print(f"Producto:  {producto}")
print(f"Precio:    ${precio:.2f}")
print(f"Cantidad:  {cantidad}")
print(f"----------------------------")
print(f"Subtotal:  ${subtotal:.2f}")
 