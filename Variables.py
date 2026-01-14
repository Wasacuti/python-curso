# Variables.py
# 1) ¿Qué es una variable?
# Una variable es un nombre que referencia un valor en memoria.

""" no es necesario declarar el tipo de variable explícitamente.
El intérprete infiere el tipo automáticamente basado en el valor asignado.
"""

numero = 10           # entero
print("Numero es un entero=", numero, type(numero))

# 2) Tipado dinámico: la variable puede cambiar de tipo
numero = "Diez"       # ahora es string
print("Numero es ahora un string =", numero, "| tipo:", type(numero))

#3 Las variables también pueden venir del usuario
#usuario = input("¿Cómo te llamas? ")
#print("Bienvenido al curso", usuario)

# 4) Tipos básicos
entero = 42                 # int
flotante = 3.1415            # float
texto = "Hola, Python"      # str
booleano = False             # bool
nada = None                 # NoneType
print(f"Entero {entero}, Flotante:  {flotante}, texto: {texto}, Boolen {booleano}, None:  {nada}")

# 5) F-strings para mostrar variables 
nombre = "Ana"
edad = 25
print(f"{nombre} tiene {edad} años.")




# 6) Conversión de tipos (casting)
numero_str = "100"
numero = float(numero_str)    # convierte de str a int
print("100 (str) ->", numero, type(numero))



# 7) Asignación múltiple
a, b, c = 1, 2, 3
print("a,b,c =", a, b, c)

# 8) Intercambio de valores sin variable temporal
a, b = b, a
print("intercambio a,b =", a, b)

# 9) Constantes (convención)
PI = 3.14159    # por convención, variables en mayúsculas se tratan como constantes
print("PI =", PI)


# 10) Estructuras compuestas como variables

lista = [1, 2, 3]  
# Colección ordenada y modificable

tupla = (4, 5, 6, 7)  
# Colección ordenada y no modificable

diccionario = {"clave": "valor"}  
# Almacena datos en pares clave : valor
# No usa índices numéricos

print("Lista:", lista)
print("Tupla:", tupla)
print("Diccionario:", diccionario)

# 11) Nombres válidos y buenas prácticas
# - deben comenzar con letra o guion bajo, no con número
# - usar minúsculas y guion bajo para separar palabras (snake_case)

nombre_valido = "Fin del programa"
print(nombre_valido)

# Resumen de buenas prácticas:
# - Las variables guardan valores y Python infiere el tipo.
# - Usa nombres claros, sigue snake_case, evita empezar con números.
# - Convención: CONSTANTES en MAYÚSCULAS.
# Utilizar Nombres descriptivos
