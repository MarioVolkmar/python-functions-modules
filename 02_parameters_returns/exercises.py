## Saludo con valor por defecto

def saludar(nombre = "Invitado"):
    return f"Hola {nombre}"

print(saludar("Mario"))
print(saludar())

## Saludo con valor por defecto

def calcular_iva(precio,iva = 19):
    return precio * (iva + 100) / 100

print(calcular_iva(100))

## Calcular precio con IVA

def aplicar_descuento(precio, descuento = 10):
    return precio * (100 - descuento) / 100

## Calcular subtotal

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

## Calcular total con descuento e IVA

def calcular_total(precio, cantidad, descuento = 0, iva = 19):
    return (precio * cantidad) * (100 + iva - descuento) / 100

## Validar edad

def validar_edad (edad, edad_min = 18):
    return edad > edad_min

##  Clasificar usuario por edad

def clasificar_edad (edad):
    if edad < 0:
        return "invalida"
    elif 0 <= edad <= 12:
        return "niño"
    elif 13 <= edad <= 17:
        return "adolecente"
    elif 18 <= edad <= 59:
        return "adulto"
    else:
        return "adulto mayor"
    
## Validar nota

def calificar_nota (nota, nota_min = 3):
    if nota < 0 or nota > 5:
        return "Invalida"
    elif nota >= 3:
        return "Aprobado"
    else:
        return "Reprobado"
    
## Normalizar texto

def normalizador (texto, formato = "lower"):
    texto = texto.strip().split()
    texto = " ".join(texto)
    if formato.lower() == "lower":
        texto = texto.lower()
    elif formato.lower() == "upper":
        texto = texto.upper()
    elif formato.lower() == "title":
        texto = texto.title()
    else:
        print("Error input")
        return
    return texto

print(normalizador("   mArIo vOLkMaR   ", "upper"))

## Crear mensaje de perfil

def crear_perfil (nombre, edad, lenguaje = "Python"):
    return f"Hola me llamo {nombre} y tengo {edad} años, y estoy aprendiendo {lenguaje}"

## Retornar múltiples valores

def analizar_numero (num):
    pos_neg_cero = [num > 0, num < 0 , num == 0]
    par = num % 2 == 0
    valor_absoluto = num if num >= 0 else -num
    res = ('Positivo' if pos_neg_cero.index(True) == 0 else 'Negativo' if pos_neg_cero.index(True) == 1 else 'Cero' , 'Par' if par else 'Impar' , valor_absoluto )
    return res

print(analizar_numero(8))

## Calcular estadísticas básicas

def calcular_estadisticas (numeros):
    if len(numeros) == 0:
        print("Error")
        return
    cantidad = len(numeros)
    suma = sum(numeros)
    promedio = suma / cantidad
    mayor = max(numeros)
    menor = min(numeros)
    return (cantidad, suma, promedio, mayor, menor)

## Filtrar números mayores a un límite

def filtrar_mayores (numeros, limite):
    res = []
    for n in numeros:
        if n > limite:
            res.append(n)
    return res

## Filtrar palabras por longitud

def filtrar_palabras_largas(palabras, longitud_minima=5):
    res = []
    for p in palabras:
        if len(p) >= longitud_minima:
            res.append(p)
    return res

## Buscar usuario

def buscar_usuario (usuarios, username):
    for u in usuarios:
        if u["username"].lower() == username.lower():
            return u
    else:
        return None
    
usuarios = [
    {"username": "mario", "activo": True},
    {"username": "ana", "activo": True},
    {"username": "luis", "activo": False}
]

print(buscar_usuario(usuarios , "maro"))


## Validar login

usuarios = [
    {"username": "mario", "password": "1234", "activo": True},
    {"username": "ana", "password": "abcd", "activo": True},
    {"username": "luis", "password": "pass", "activo": False}
]

def validar_login(usuarios, username, password):
    for u in usuarios:
        if u["username"].lower() == username:
            if u["password"] != password:
                return "Credenciales Invalidas"
            elif  u["activo"]:
                return "Acceso permitido"
            else:
                return "Usuario Inactivo"
    else:
        return "Usuario inexistente"
    
print(validar_login(usuarios, "lus", "pass"))

## Actualizar stock

productos = [
    {"nombre": "Laptop", "stock": 3},
    {"nombre": "Mouse", "stock": 10},
    {"nombre": "Teclado", "stock": 5}
]

def actualizar_stock(productos, nombre_producto, nuevo_stock):
    if nuevo_stock < 0:
                return False
    for p in productos:
        if p["nombre"].lower() == nombre_producto.lower():
            p["stock"] = nuevo_stock
            return True
    else:
        return False
    
print(actualizar_stock(productos ,"mouse" , 12))

##  Calcular total de inventario

productos = [
    {"nombre": "Laptop", "precio": 2500000, "stock": 3},
    {"nombre": "Mouse", "precio": 80000, "stock": 10},
    {"nombre": "Teclado", "precio": 120000, "stock": 5}
]

def calcular_total_inventario(productos):
    total = 0
    for p in productos:
        total += p["precio"] * p["stock"]
    return total

## Crear producto

def crear_producto(nombre, precio, stock=0):
    return {
        "nombre" : nombre,
        "precio" : float(precio),
        "stock" : stock
    }

## Registrar venta

productos = [
    {"nombre": "Laptop", "precio": 2500000, "stock": 3},
    {"nombre": "Mouse", "precio": 80000, "stock": 10},
    {"nombre": "Teclado", "precio": 120000, "stock": 5}
]

def registrar_venta(productos, nombre_producto, cantidad):
    if cantidad <= 0:
        return "Error cantidad"
    for p in productos: 
        if p["nombre"].lower() == nombre_producto.lower():
            if cantidad > p["stock"]:
                return "Stock insuficiente"
            else:
                p["stock"] -= cantidad
                return p["precio"] * cantidad
    else:
        return "Producto no encontrado"

print(registrar_venta(productos, "mouse", 0))
