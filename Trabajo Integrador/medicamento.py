class Medicamento:
    __IdCama = None
    __IdMedicamento= None
    __NombreComercial = None
    __Monodroga = None
    __Presentacion = None
    __CantidadAplicada = None
    __PrecioTotal = None

    def __init__(self,idcama,idmecicamento,nombrecomercial,monodroga,presentacion,cantidadaplicada,preciototal):
        if int(idcama) < 30 and int(idcama) > 0:
            self.__idCama = idcama
        if int(idmecicamento) < 100 and int(idmecicamento) > 0:
            self.__IdMedicamento = idmecicamento
            self.__NombreComercial = nombrecomercial
            self.__Monodroga = monodroga
            self.__Presentacion = presentacion
            self.__CantidadAplicada = cantidadaplicada
            self.__PrecioTotal = preciototal
    def getIdcama(self):
        return self.__idCama
    def getIdmedicamento(self):
        return self.__IdMedicamento
    def getNombre(self):
        return self.__NombreComercial
    def getMonodroga(self):
        return self.__Monodroga
    def getPresentacion(self):
        return self.__Presentacion
    def getCantidadAplicada(self):
        return self.__CantidadAplicada
    def getPrecio(self):
       return  self.__PrecioTotal