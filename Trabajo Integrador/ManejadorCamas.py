import csv
import numpy as np
from camas import Cama
from datetime import datetime
from ManejadorMedicamento import ManejaMedicamento
class ManejadorCamas:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension=5, incremento=5):
            self.__camas = np.empty(dimension, dtype=Cama)
            self.__cantidad = 0
            self.__dimension = dimension

    def agregarCama(self, cama):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__camas.resize(self.__dimension)
            self.__camas[self.__cantidad] = cama
            self.__cantidad += 1

    def Cargar(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo,delimiter =';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
              cama = Cama(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5],linea[6])
              self.agregarCama(cama)

    def DarAlta(self,Nombre,Medicamentos):
        print('-------------------------------------------------------------------------------------------------------------')
        i = 0
        bandera = False
        band = False
        while i < (int(self.__cantidad)) and bandera == False:
         if self.__camas[i].getNombre().lower() == Nombre.lower():
            fecha = datetime.today().strftime('%d/%m/%Y')
            self.__camas[i].ingresarFechaalta(fecha)
            print('Paciente: {nombre}           Cama: {cama}           Habitación: {habitacion}'.format(nombre=self.__camas[i].getNombre(), cama=self.__camas[i].getid(),habitacion=self.__camas[i].getHabitacion() ))
            print('Diagnóstico: {diagnostico}                Fecha de internación: {fechain}'.format(diagnostico=self.__camas[i].getDiagnostico(), fechain=self.__camas[i].getFechainternacion()))
            print('Fecha de alta: {fechalta}'.format(fechalta=self.__camas[i].getFechaalta()))
            Medicamentos.MostrarAlta(i+1)
            band = True
            self.__camas[i].ingresarEstado(False)
            self.__camas[i].ingresarnombre(None)
            bandera= True
            i= i +1
         else:
            i = i + 1
            band = False
        if band == False:
         print('Paciente no encontrado')
    def mostrarDatos(self,diagnostico):
        for i in range(self.__cantidad):
         if diagnostico.lower() in self.__camas[i].getDiagnostico().lower():
             print(self.__camas[i])


