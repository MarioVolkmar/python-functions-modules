def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b == 0:
        return None
    return a/b

def calcular_promedio(numeros):
    if len(numeros) == 0:
        return None
    return sum(numeros) / len(numeros)

