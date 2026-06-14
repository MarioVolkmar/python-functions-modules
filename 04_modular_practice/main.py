from calculator import sumar, dividir, promedio
from text_utils import normalizar_nombre, crear_slug
from list_utils import eliminar_duplicados, filtrar_pares
from inventory import buscar_producto, registrar_venta, calcular_valor_inventario



print(sumar(5, 3))
print(dividir(10, 2))
print(promedio([4, 5, 3]))

print(normalizar_nombre("   mArIo   vOLkMaR   "))
print(crear_slug("Curso de Python Backend"))

print(eliminar_duplicados([1, 2, 2, 3, 1, 4]))
print(filtrar_pares([1, 2, 3, 4, 5, 6]))

productos = [
    {"nombre": "Laptop", "precio": 2500000, "stock": 3},
    {"nombre": "Mouse", "precio": 80000, "stock": 10},
    {"nombre": "Teclado", "precio": 120000, "stock": 0}
]

print(buscar_producto(productos, "mouse"))
print(calcular_valor_inventario(productos))
print(registrar_venta(productos, "Mouse", 2))
print(productos)

