class Registro:
    __dia = ''
    __hora = ''
    __temperatura = ''
    __humedad = ''
    __presion = ''
    
    def __init__(self,dia , hora,temperatura, humedad, presion):
        self.__dia = dia
        self.__hora = hora
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion
    def getTemperatura(self):
        return self.__temperatura
    def getDia(self):
        return self.__dia
    def getHora(self):
        return self.__hora
    def getHumedad(self):
        return  self.__humedad
    def getPresion(self):
        return  self.__presion
    def mostrar(self):
        print (str(self.__dia)+','+str(self.__temperatura)+','+str(self.__humedad)+','+str(self.__presion))

   

