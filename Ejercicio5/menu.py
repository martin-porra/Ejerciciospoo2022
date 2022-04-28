import os
class menu:

    def __init__(self):
      os.system('cls')

    def Menu(self):
     print("Selecciona una opción")
     print("\t1 - primera opción")
     print("\t2 - segunda opción")
     print("\t3 - tercera opción")
     print("\t4 - cuarta opción")
     print("\t5 - salir")

    def opcion(self, manejador):
     while True:
      self.Menu()
      op = input("inserta un numero valor >> ")
      if op == "1":
       manejador.actualizarvalor()
      elif op == "2":
       manejador.mostrar()
      elif op == "3":
        manejador.montolicitar()
      elif op == "4":
          manejador.actualizarcuotalicitar()
      elif op == "5":
          break
      else:
       input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")