import csv
from Registro import Registro
class ManejadorRegistro:
    __listaObjeto = []



    def __init__(self):
        self.inicializarLista()

    def inicializarLista(self):
        for i in range(30):
            self.__listaObjeto.append([0] * 24)
        archivo = open('mes.csv')
        reader = csv.reader(archivo, delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                dia = int(fila[0])
                hora = int(fila[1])
                temperatura = float(fila[2])
                humedad = fila[3]
                presion = fila[4]
                UnRegistro = Registro(dia, hora, temperatura, humedad, presion)
                self.__listaObjeto[dia - 1][hora - 1] = UnRegistro

    def mostrar(self):
        print(self.__listaObjeto[0][0].mostrar())

    def MaximoTemperatura(self):
        maximo = -9999
        dia = None
        hora = None
        for i in range(len(self.__listaObjeto)):
            for j in range(len(self.__listaObjeto[i])):
                if type(self.__listaObjeto[i][j]) == Registro:
                    if self.__listaObjeto[i][j].getTemperatura() > maximo:
                        maximo = self.__listaObjeto[i][j].getTemperatura()
                        dia = self.__listaObjeto[i][j].getDia()
                        hora = self.__listaObjeto[i][j].getHora()
        return 'Temperatura maxima registrada: {} en el dia {} hora {}'. format(maximo, dia, hora)

    def MinimoTemperatura(self):
        minimo = 9999
        dia = None
        hora = None
        for i in range(len(self.__listaObjeto)):
            for j in range(len(self.__listaObjeto[i])):
                if type(self.__listaObjeto[i][j]) == Registro:
                    if self.__listaObjeto[i][j].getTemperatura() < minimo:
                        minimo = self.__listaObjeto[i][j].getTemperatura()
                        dia = self.__listaObjeto[i][j].getDia()
                        hora = self.__listaObjeto[i][j].getHora()
        return 'Temperatura minima registrada: {} en el dia {} hora {}'. format(minimo, dia, hora)


    def MaximoPresion(self):
        maximo = -9999
        dia = None
        hora = None
        for i in range(len(self.__listaObjeto)):
            for j in range(len(self.__listaObjeto[i])):
                if type(self.__listaObjeto[i][j]) == Registro:
                    if int(self.__listaObjeto[i][j].getPresion()) > int(maximo):
                        maximo = self.__listaObjeto[i][j].getPresion()
                        dia = self.__listaObjeto[i][j].getDia()
                        hora = self.__listaObjeto[i][j].getHora()
        return 'Maxima presion atmosferica  registrada: {} en el dia {} hora {}'. format(maximo, dia, hora)

    def MinimoPresion(self):
        minimo = 9999
        dia = None
        hora = None
        for i in range(len(self.__listaObjeto)):
            for j in range(len(self.__listaObjeto[i])):
                if type(self.__listaObjeto[i][j]) == Registro:
                    if int(self.__listaObjeto[i][j].getPresion()) < int(minimo):
                        minimo = self.__listaObjeto[i][j].getPresion()
                        dia = self.__listaObjeto[i][j].getDia()
                        hora = self.__listaObjeto[i][j].getHora()
        return 'Minima presion atmosferica  registrada: {} en el dia {} hora {}'. format(minimo, dia, hora)

    def MaximaHumedad(self):
        maximo = -9999
        dia = None
        hora = None
        for i in range(len(self.__listaObjeto)):
            for j in range(len(self.__listaObjeto[i])):
                if type(self.__listaObjeto[i][j]) == Registro:
                    if int(self.__listaObjeto[i][j].getHumedad()) > int(maximo):
                        maximo = self.__listaObjeto[i][j].getHumedad()
                        dia = self.__listaObjeto[i][j].getDia()
                        hora = self.__listaObjeto[i][j].getHora()
        return 'Maxima humedad  registrada: {} en el dia {} hora {}'. format(maximo, dia, hora)

    def MinimaHumedad(self):
        minimo = 9999
        dia = None
        hora = None
        for i in range(len(self.__listaObjeto)):
            for j in range(len(self.__listaObjeto[i])):
                if type(self.__listaObjeto[i][j]) == Registro:
                    if int(self.__listaObjeto[i][j].getHumedad()) < int(minimo):
                        minimo = self.__listaObjeto[i][j].getHumedad()
                        dia = self.__listaObjeto[i][j].getDia()
                        hora = self.__listaObjeto[i][j].getHora()
        return 'Minima humedad  registrada: {} en el dia {} hora {}'. format(minimo, dia, hora)


    def PromediosHoras(self):
        hora = 1
        while hora <= 24:
            print('Promedio mensual de la hora {}: {} °C' .format(hora,self.PromedioMensual(hora)))
            hora+=1
    def PromedioMensual(self, hora):
        total = 0
        count = 0
        for i in range(len(self.__listaObjeto)):
            for j in range(len(self.__listaObjeto[i])):
                if type(self.__listaObjeto[i][j]) == Registro:
                    if self.__listaObjeto[i][j].getHora() == hora:
                        count= count + 1
                        total = total + self.__listaObjeto[i][j].getTemperatura()
        total =total/count
        return float(total)               

           
    def __str__(self):
        s=''
        for i in range(len(self.__listaObjeto)):
            for j in range(len(self.__listaObjeto[i])):
                if type(self.__listaObjeto[i][j]) == Registro:
                    s+= str(self.__listaObjeto[i][j]) + '\n'
        return s      

    def mostrarDatos(self, dia):
        hora = 0
        if int(dia) <= 30:
            print('Hora\t\tTemperatura\t\tHumedad\t\tPresion')
            while hora <= 23:
                print((self.__listaObjeto[int(dia)-1][int(hora)].getHora()),'            ',(self.__listaObjeto[int(dia)-1][int(hora)].getTemperatura()), '         ', (self.__listaObjeto[int(dia)-1][int(hora)].getHumedad()),'          ', (self.__listaObjeto[int(dia)-1][int(hora)].getPresion()))
                hora+=1
        else:
            print('Dia ingresado invalido')    
  


            




   
