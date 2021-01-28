# Estructuras de Condición/Decisión/Selección
edad = int(input("¿Cuál es tu edad?: "))

if (edad >= 0 and edad <= 18):
  print("Menor de edad")
elif edad > 18 and edad <= 120:
  print("Mayor de edad")
else:
  print("Edad incorrecta")