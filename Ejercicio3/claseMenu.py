import os
from  ManejadorRegistro import ManejadorRegistro
class menu:

    def __init__(self):
      os.system('cls')

    def Menu(self):
     print("Selecciona una opción")
     print("\t1 - primera opción")
     print("\t2 - segunda opción")
     print("\t3 - tercera opción")
     print("\t4 - salir")

    def opcion(self, manejador):
     while True:
      self.Menu()
      op = input("inserta un numero valor >> ")
      if op == "1":
       print('__________________Temperatura _______________ ')
       print(manejador.MaximoTemperatura())
       print(manejador.MinimoTemperatura())
       print('_____________________Humedad______________________')
       print(manejador.MaximaHumedad())
       print(manejador.MinimaHumedad())
       print('_______________________Presión____________________')
       print(manejador.MaximoPresion())
       print(manejador.MinimoPresion())
      elif op == "2":
        print('Temperatura promedio mensaul por hora:')
        manejador.PromediosHoras()
      elif op == "3":
         print('ingrese un dia para mostrar datos variables por hora')
         di = input()
         manejador.mostrarDatos(di)
      elif op == "4":
          break
      else:
       input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")