# Precedencia de Operadores en Python
# La precedencia define el orden en que Python evalúa operadores
#  en una expresión aritmética o lógica.
# Tabla de precedencia (de mayor a menor):
# 1. Paréntesis ()
# 2. Exponenciación **
# 3. Multiplicación *, División /, División entera //, Módulo %
# 4. Suma +, Resta -
# 5. Comparación ==, !=, <, >, <=, >=
# 6. Operadores lógicos and, or, not



# Ejemplo 1: Paréntesis cambian la precedencia
resultado = (2 + 3) * 4
print(f"(2 + 3) * 4 = {resultado}")  # Output: 20
# Explicación: Primero 2 + 3 = 5, luego 5 * 4 = 20

# Ejemplo 2: Exponenciación
resultado2 = 2 + 3 ** 2
print(f"2 + 3 ** 2 = {resultado2}") 


# Ejemplo 3: Multiplicación antes que suma
resultado3 = 2 + 3 * 4
print(f"2 + 3 * 4 = {resultado3}")  



# Ejemplo 4: Orden de precedencia (de mayor a menor)
resultado4 = 2 + 3 * 4 / 2 - 1
print(f"2 + 3 * 4 / 2 - 1 = {resultado4}")  



# Ejemplo 5: Orden de precedencia (de mayor a menor)
resultado5 = 2 + 3 **4 / 2 - 1
print(f"2 + 3 * 4 / 2 - 1 = {resultado5}") 


