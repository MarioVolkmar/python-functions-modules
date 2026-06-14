def obtener_primero(lista):
    if len(lista) == 0:
        return None
    return lista[0]

def obtener_ultimo(lista):
    if len(lista) == 0:
        return None
    return lista[-1]

def eliminar_duplicados(lista):
    res = []
    for e in lista:
        if e not in res:
            res.append(e)
    return res

def filtrar_pares(numeros):
    res = []
    for n in numeros:
        if n % 2 == 0 :
            res.append(n)
    return res

def separar_pares_impares(numeros):
    pares = []
    impares = []
    for n in numeros:
        if n % 2 == 0 :
            pares.append(n)
        else:
            impares.append(n)
    return {
        "pares" : pares,
        "impares" : impares
    }
