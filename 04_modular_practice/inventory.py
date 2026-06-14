def buscar_producto(productos, nombre_buscado):
    for p in productos:
        if p["nombre"].lower() == nombre_buscado.strip().lower():
            return p
    else:
        return None
    
def filtrar_disponibles(productos):
    res = []
    for p in productos:
        if p["stock"] > 0:
            res.append(p)
    return res

def calcular_valor_inventario(productos):
    total = 0
    for p in productos:
        total += p["precio"] * p["stock"]
    return total

def actualizar_stock(productos, nombre_producto, nuevo_stock):
    if nuevo_stock < 0:
        return False
    for p in productos:
        if p["nombre"].lower() == nombre_producto.strip().lower():
            p["stock"] = nuevo_stock
            return True
    else:
        return False

def registrar_venta(productos, nombre_producto, cantidad):
    if cantidad < 0:
        return "Cantidad invalida"
    for p in productos:
        if p["nombre"].lower() == nombre_producto.strip().lower():
            if p["stock"] >= cantidad:
                p["stock"] -= cantidad
                return p["precio"] * cantidad
            else:
                return "Stock insuficiente"
    else:
        return "Producto no encontrado"