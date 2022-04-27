from Registro import Registro
from  ManejadorRegistro import  ManejadorRegistro
import csv
from claseMenu import menu
if __name__ == '__main__':
   manejador = ManejadorRegistro()
   men = menu()
   men.opcion(manejador)