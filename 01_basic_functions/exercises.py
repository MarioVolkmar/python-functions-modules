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

## 