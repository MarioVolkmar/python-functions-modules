## Saludar

def saludar():
    print("Hola")

saludar()

## Saludar nombre

def saludar_nombre(nombre):
    print(f"Hola {nombre.capitalize()}")

saludar_nombre("mario")

## Sumar dos números

def sumar (a , b):
    return a + b

print(sumar(5,3))

## Restar dos números

def restar (a , b):
    return a - b

print(restar(5,3))

## Multiplicar dos números

def multiplicar (a , b):
    return a * b

print(multiplicar(5,3))

## Dividir dos números

def dividir (a, b):
    if b != 0:
        return a / b
    else :
        return "Error"

print(dividir(5,0))

## Verificar si un número es par

def es_par(n):
    if n % 2 == 0:
        return "Par"
    else:
        return ("Impar")
    
print(es_par(5))

## Clasificar número

def clasificar(n):
    if n == 0:
        return "Cero"
    elif n > 0:
        return "Positivo"
    else:
        return "Negativo"
    
print(clasificar(5))

## Calcular edad en días

def edad_dias (edad):
    return edad*365

print(edad_dias(32))

## Calcular área de rectángulo

def area_rec(a,b):
    return a*b

print(area_rec(6,5))

## Calcular promedio de tres notas

def prom(n1,n2,n3):
    promedio = (n1 + n2 + n3)/3
    return promedio

print(prom(5,6,8))

## Determinar estado de una nota

def evaluador(nota):
    if nota >= 3:
        return True
    else:
        return False
    
print(evaluador(2.9))

## Normalizar nombre

def normalizador(nombre):
    nombre = nombre.strip().title().split()
    nombre = " ".join(nombre)
    return nombre

print(normalizador("   mArIo   vOLkMaR   "))

## Contar vocales

def c_vocales(texto):
    vocales = "aeiou"
    res = 0
    for l in texto:
        if l.lower() in vocales:
            res += 1
    return res

print(c_vocales("Contar vocales"))

## Contar consonantes

def c_consonantes(texto):
    vocales = "aeiou"
    letras = "qwertyuiopasdfghjklñzxcvbnm"
    res = 0
    for l in texto:
        if l.lower() in letras and l.lower() not in vocales:
            res += 1
    return res

print(c_consonantes("qwertyuiopasdfghjklñzxcvbnm"))

## Invertir texto

def invertir(texto):
    return texto[::-1]

print(invertir("Hola"))

## Validar email simple

def validar_email(e):
    e = e.strip()
    if e[0] == "@" or e[-1] == "@":
        return False
    elif "." not in e:
        return False
    elif "@" not in e:
        return False
    else:
        return True
    
print(validar_email("das@f.sco"))

## Crear slug

def slug (texto):
    texto = texto.strip().lower().split()
    texto = "-".join(texto)
    return texto

print(slug("Curso de Python Backend"))

## Calcular total de carrito

carrito = [
    {"producto": "Mouse", "precio": 80000, "cantidad": 2},
    {"producto": "Teclado", "precio": 120000, "cantidad": 1},
    {"producto": "Monitor", "precio": 900000, "cantidad": 1}
]

def c_total (lista):
    total = 0
    for p in lista:
        total += (p["precio"] * p["cantidad"])
    return total

print(c_total(carrito))

## Buscar producto por nombre

productos = [
    {"nombre": "Laptop", "precio": 2500000, "stock": 3},
    {"nombre": "Mouse", "precio": 80000, "stock": 10},
    {"nombre": "Teclado", "precio": 120000, "stock": 5}
]

def busqueda_prod (lista, nombre):
    for p in lista:
        if p["nombre"].lower() == nombre.lower():
            return p
    else:
        return "None"
    
print(busqueda_prod(productos, "mose"))