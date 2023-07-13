import os
from TaskList import TaskList

isOpen = True

tasks = TaskList()

def showActions():
  print("\n\033[97m\033[42m===========================\033[0m")
  print("   Seleccione una opción")
  print("\033[97m\033[42m===========================\033[0m\n")
  print("1. Crear tarea")
  print("2. Ver tareas")
  print("0. Salir\n")

def cleanConsole():
  os.system("cls" if os.name == "nt" else "clear")

while (isOpen):
  cleanConsole()
  showActions()

  action = input("¿Qué deseas hacer? ")

  if action == "1":
    nameTask = input("Nombre de la tarea: ")
    tasks.createTask(nameTask)
  elif action == "2":
    tasks.showList()
  elif action == "0":
    isOpen = False
    break
  else:
    print("\nOpción no valida")

  input("\nPresiona ENTER para continuar")