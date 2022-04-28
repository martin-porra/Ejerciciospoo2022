import csv
from ClaseViajero import viajero
import os

def menu():
 os.system('cls') # NOTA para windows tienes que cambiar clear por cls
 print ("Selecciona una opción")
 print ("\t1 - primera opción")
 print ("\t2 - segunda opción")
 print ("\t3 - tercera opción")

if __name__ == '__main__':
 lista = []
 archivo = open('viajero.txt')
 reader = csv.reader(archivo, delimiter=(','))
 for fila in reader:
  objeto = viajero(fila[0],fila[1],fila[2],fila[3],fila[4])
  lista.append(objeto)
 archivo.close()
 print('ingrese numero de viajero frecuente')
 b = int(input())
 a = True
 while a == True:
   menu()
   opcion = input()
   if opcion == '1':
    print('la cantidad de millas es:')
    print(lista[b-1].getmillas())
   elif opcion == '2':
    print('ingrese numero de millas a acumular')
    lol = int(input())
    lista[b-1] = lista[b-1]+lol
    print('la cantidad de millas  actual es:', lista[b - 1].getmillas())
   elif opcion == '3':
    print('ingresar millas que desea canjear')
    lel = int(input())
    lista[b-1] =lel - lista[b-1]
    print('la cantidad de millas  actual es:', lista[b - 1].getmillas())
   elif opcion == "4":
       mayor = lista[0]
       for i in range(len(lista) - 1):
           if mayor > lista[i+1]:
               mayor = mayor
           else:
               mayor = lista[i+1]
       print('el/los usuarios con mayor millas son:')
       for i in range(len(lista)):
        if lista[i].getmillas() == mayor.getmillas():
         print(lista[i].getnombre())

   else:
    a = False
    print('opcion incorrecta')
 print('programa terminado')