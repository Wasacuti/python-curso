# Ingresar la edad de una persona y determinar si es mayor o menor de edad
# "if": una estructura de control que ejecuta un bloque de código 
# solo cuando una condición (verdadera/falsa) se cumple.

# edad=int(input("Ingrese su edad:"))

# if edad >18 : 
#     print("Usted es mayor de edad ")

# else :
#     print("usted es menor de edad")



# clave_bd="123456"

# clave_user=input("ingrese la clave:")

# if clave_bd==clave_user: 
#     print("Login exitoso")
# else: 
#     print("no autorizado")


edad=int(input("Ingrese su edad:"))

if edad <12 : 
    print("Usted es un niño (a) ")

elif edad<18:
    print("Usted es adolecente ")

elif edad<25:
    print("Usted es joven ")

elif edad<60:
    print("Usted es adulto ")   

elif edad<100:
    print("Usted es adulto mayor ")   

else:
    print("ingrese un dato entre 1 y 100")



