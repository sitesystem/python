# Comentario: imprimir cadenas de texto (strings)
print("Hola Mundo \"Eduardo\"")
print('Hola Mundo "Eduardo"')
print("""Hola Mundo""")
print('''Hola Mundo''')
print("Hola" + " " , "Mundo concatenado")

saludo = "Saludo"
print("Escribe tu nombre: ")
nombre = input()
edad = input("Escribe tu edad: ")
print(saludo + " " + nombre + " " + edad + " años") # str(edad)
print(f"{saludo} {nombre} {edad} años")

"""
Tipos de Datos
"""
saludo = "Hola"
print(type(saludo)) # string
saludo = 5
print(type(saludo)) # int

print(type(8)) # int
print(type(2.5)) # float
print(type(True)) # bool
print(type([1,2,3,4,5])) # list