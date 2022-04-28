class PlanAhorro:
    __codigoplan = None
    __modelo = None
    __version = None
    __valor = None
    __cantidadcuotas = None
    __cantidadcuotaslicitar = None

    def __init__(self,codigo,modelo,version,valor,cantidadcuotas,cantidadcuotasli):
        self.__codigoplan = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
        self.__cantidadcuotas = cantidadcuotas
        self.__cantidadcuotaslicitar = cantidadcuotasli

    def getCodigo(self):
        return self.__codigoplan
    def getModelo(self):
        return  self.__modelo
    def getVersion(self):
        return self.__version
    def getValor(self):
        return  self.__valor
    def getCantidadcuotas(self):
        return self.__cantidadcuotas
    def getCantidadlicitar(self):
        return self.__cantidadcuotaslicitar
    def actualizarvalor(self,val):
        self.__valor = val

    def actualizarcuotas(self,valor):
        self.__cantidadcuotaslicitar = valor

