##  Obtener primer elemento

def obtener_primero(lista):
    if len(lista) == 0:
        return None
    else:
        return lista[0]

## obtener_primero(lista)

def obtener_ultimo(lista):
    if len(lista) == 0:
        return None
    else:
        return lista[-1]
    
## Agregar elemento a lista

def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

## Eliminar último elemento

def eliminar_ultimo(lista):
    if len(lista) == 0:
        return lista
    else:
        lista.pop()
        return lista
    
## Buscar elemento

def buscar_elemento(lista, elemento):
    return elemento in lista

## Contar elementos manualmente

def contar_elementos(lista):
    res = 0
    for i in lista:
        res += 1
    return res

## Sumar números de una lista

def sumar_lista(numeros):
    if len(numeros) == 0:
        return 0
    else: 
        return sum(numeros)

## Calcular promedio

def calcular_promedio(numeros):
    if len(numeros) == 0:
        return None
    else:
        prom = sum(numeros) / len(numeros)
        return prom
    
## Obtener mayor número

def obtener_mayor(numeros):
    if len(numeros) == 0:
        return None
    else: 
        return max(numeros)

## Obtener menor número

def obtener_menor(numeros):
    if len(numeros) == 0:
        return None
    else: 
        menor = numeros[0]
        for n in numeros:
            if n < menor:
                menor = n
        return menor
    
## Filtrar números pares

def filtrar_pares(numeros):
    res = []
    for n in numeros:
        if n % 2 == 0:
            res.append(n)
    return res

## Separar pares e impares

def separar_pares_impares(numeros):
    pares = []
    impares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return {
        "pares" : pares,
        "impares" : impares
    }

## Eliminar duplicados manteniendo orden

def eliminar_duplicados(lista):
    res = []
    for e in lista:
        if e not in res:
            res.append(e)
    return res

## Contar apariciones

def contar_apariciones(lista, elemento):
    res = 0
    for e in lista:
        if e == elemento:
            res += 1
    return res

## Filtrar palabras largas

def filtrar_palabras_largas(palabras, longitud_minima=5):
    res = []
    for p in palabras:
        if len(p) >= longitud_minima:
            res.append(p)
    return res

## Normalizar lista de nombres

def normalizar_nombres(nombres):
    res = []
    for n in nombres:
        n = n.strip().title().split()
        n = " ".join(n)
        res.append(n)
    return res

## Buscar producto por nombre

productos = [
    {"nombre": "Laptop", "precio": 2500000, "stock": 3},
    {"nombre": "Mouse", "precio": 80000, "stock": 10},
    {"nombre": "Teclado", "precio": 120000, "stock": 0}
]

def buscar_producto(productos, nombre_buscado):
    for p in productos:
        if p["nombre"].lower() == nombre_buscado.lower():
            return p
    else:
        return None
    
## Filtrar productos disponibles

def filtrar_disponibles(productos):
    res = []
    for p in productos:
        if p["stock"] > 0:
            res.append(p)
    return res

## Calcular valor total del inventario

def calcular_valor_inventario(productos):
    total = 0
    for p in productos:
        total += p["precio"] * p["stock"]
    return total

## Actualizar stock de producto

def actualizar_stock(productos, nombre_producto, nuevo_stock):
    if nuevo_stock < 0:
        return False
    for p in productos:
        if p["nombre"].lower() == nombre_producto.lower():
            p["stock"] = nuevo_stock
            return True
    else:
        return False
    