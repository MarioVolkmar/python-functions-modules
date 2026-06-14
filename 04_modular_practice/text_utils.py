def normalizar_texto(texto):
    texto = texto.strip().lower().split()
    texto = " ".join(texto)
    return texto

def normalizar_nombre(nombre):
    nombre = nombre.strip().title().split()
    nombre = " ".join(nombre)
    return nombre

def contar_vocales(texto):
    vocales = "aeiou"
    res = 0
    for t in texto:
        if t.lower() in vocales:
            res += 1
    return res

def contar_consonantes(texto):
    vocales = "aeiou"
    letras = "qwertyuiopasdfghjklñzxcvbnm"
    res = 0
    for t in texto:
        if t.lower() in letras and t.lower() not in vocales:
            res += 1
    return res

def crear_slug(texto):
    texto = texto.strip().lower().split()
    texto = "-".join(texto)
    return texto