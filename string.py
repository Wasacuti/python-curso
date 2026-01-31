# Cadenas de texto en Python - Guía Educativa

# 1. Conceptos básicos de cadenas
# son una secuencia de caracteres encerrados entre comillas simples (' ') o dobles (" "). 

# Comillas dobles 


# string  str


saludo = "Hola 'hola' "
nombre=input("¿Cual es tu nombre? ")

print(saludo, nombre)

# Comillas simples (igual que comillas dobles)
bienvenida = ' "Bienvenido"  '
print(bienvenida, nombre)

# Cadenas multi-línea (comillas triples)
multilínea = """ Esta es una
cadena de texto
multi-línea en Python se puede escribir así.  es util para textos largos
como parrafos. 
Hola
como estas?
Juan
"""

print(multilínea)







# Concatenación de cadenas
nombre = "Juan"
apellido = "Lopez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Salida: Juan Lopez

# f-strings (Python moderno 3.6+)
edad = 25
print(f"Mi nombre es {nombre}  {apellido} y tengo {edad} años")


#2 slicing

texto = "hola mundo"

print (texto[-1])  

















# 2. Funciones importantes de cadenas

# len() - Retorna la longitud de la cadena
print("la cantidad de caracteres es: ", len(texto))  # Salida: 10

# capitalize() - Capitaliza el primer carácter

print(texto.capitalize())  # Salida: Hola mundo







# upper() - Convierte todos los caracteres a mayúsculas
print(texto.upper())  # Salida: HOLA MUNDO

# lower() - Convierte todos los caracteres a minúsculas
texto2 = "HOLA MUNDO"
print(texto2.lower())  # Salida: hola mundo

# title() - Capitaliza la primera letra de cada palabra
print(texto.title())  # Salida: Hola Mundo

# strip() - Elimina espacios en blanco de ambos extremos
texto3 = "  hola  "
print(texto3.strip())  # Salida: hola

# replace() - Reemplaza subcadena por otra
print(texto.replace("mundo", "Python"))  # Salida: hola Python

# split() - Divide la cadena en una lista
palabras = texto.split()
print(palabras)  # Salida: ['hola', 'mundo']





