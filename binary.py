
#La conversión de decimal a binario y viceversa
# se realiza con las funciones bin() y int() 
#bin(): convierte un número decimal en binario 
#int(xx, 2): convierte un número binario en decimal

num=int(input("Enter a decimal number: "))
num=bin(num)  # convierte a binario 0b...   
print(num)  #0b1010  


num=input("Enter a binary number: ")
num=int(num,2)  # especificamos base 2 y lo convierte a decimal
print(num) 