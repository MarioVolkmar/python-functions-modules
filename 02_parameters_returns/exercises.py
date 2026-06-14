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

##