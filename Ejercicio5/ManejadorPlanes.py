from ClasePlanAhorro import PlanAhorro
import csv

class ManejadorPlan:
    lista = []

    def __init__(self):
        self.llenarlista()

    def llenarlista(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            plan = PlanAhorro(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.lista.append(plan)
        archivo.close()
    def mostrar(self):
        print('ingresar valor')
        valor = int(input())
        for i in range(len(self.lista)):
         a = self.lista[i].getValor()
         b = self.lista[i].getCantidadcuotas()
         comp = self.valorcuota(a,b)
         if valor >= comp:
            print(self.lista[i].getCodigo(), '  ', self.lista[i].getModelo(), '  ', self.lista[i].getVersion())

    def actualizarvalor(self):
        print('Plan   Modelo     Version')
        for i in range(len(self.lista)):
            print(self.lista[i].getCodigo(),'  ', self.lista[i].getModelo(),'  ', self.lista[i].getVersion())
            print('ingresa valor actual del vehiculo')
            valor = input()
            self.lista[i].actualizarvalor(valor)

    def valorcuota(self,a,b):
        valor = (int(a)/int(b))+int(a)*0.10
        return valor
    def montolicitar(self):
        for i in range (len(self.lista)):
         monto = int(self.lista[i].getCantidadlicitar()) * int(self.valorcuota(self.lista[i].getValor(), self.lista[i].getCantidadcuotas()))
         print(' vehiculo: ', self.lista[i].getModelo(), 'monto:',   monto )

    def actualizarcuotalicitar(self):
        print('ingresar numero del plan')
        plan = int(input())
        for i in range(len(self.lista)):
         print(i)
         if plan == int(self.lista[i].getCodigo()):
          print('ingrese valor')
          val = int(input())
          self.lista[i].actualizarcuotas(val)
          break
        else:
            print('no se encontro el plan ingresado')

