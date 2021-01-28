# def Saludar(nombre, edad):
#     return "Hola {} de {} años Bienvenido".format(nombre, edad)

# print("Escribe tu nombre: ")
# nombre = input()
# edad = input("Escribe tu edad: ")

# print(Saludar(nombre, edad))

def mayor_a_cinco(elemento):
  return elemento > 5

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
filtro = tuple(filter( mayor_a_cinco, tupla))
resultado = len(filtro)
print(filtro)
print(resultado)

def cuadrado(elemento=0):
  return elemento * elemento

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(map(cuadrado, lista))
print(resultado)