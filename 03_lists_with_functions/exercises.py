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
    
## 