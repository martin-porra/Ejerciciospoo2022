import csv
from medicamento import Medicamento
class ManejaMedicamento:
    __lista = []

    def __init__(self):
     self.__lista = []
      

    def Cargar(self):
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter =';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                medicamento = Medicamento(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5],linea[6])
                self.__lista.append(medicamento)

    def MostrarAlta(self,i):
            total = 0
            print('Medicamento/monodroga            Presentación              Cantidad               Precio')
            for o in range(len(self.__lista)):
                if int(i) == int(self.__lista[o].getIdcama()):
                 total +=    int(self.__lista[o].getPrecio())
                 print('{medicamento}/{monodroga}            {presentacion}                 {cantidad}                    {precio}    '.format(medicamento=self.__lista[o].getNombre(),monodroga=self.__lista[o].getMonodroga(),presentacion=self.__lista[o].getPresentacion(),cantidad=self.__lista[o].getCantidadAplicada(),precio=self.__lista[o].getPrecio()))
            print('Total Adeudado:                                                                     {total}'.format(total=total))
            print( '-------------------------------------------------------------------------------------------------------------')



