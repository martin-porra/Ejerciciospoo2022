class viajero:
    __numeroviajero = 0
    __dni = 0
    __nombre = ''
    __apellido = ''
    __millasacum  = 0

    def __init__(self, numerov,dni,nombre,apellido,millas):
        self.__numeroviajero = numerov
        self.__nombre = nombre
        self.__dni = dni
        self.__apellido = apellido
        self.__millasacum = millas

    def getmillas(self):
     return  self.__millasacum
    def getnombre(self):
        return  self.__nombre
    def getapellido(self):
        return  self.__apellido
    def getdni(self):
        return  self.__dni
    def getnum(self):
        return self.__numeroviajero
   # def acumular(self, millas):
    #    self.__millasacum = self.__millasacum + millas
    def canjearmillas(self,millas):
        if int(self.__millasacum) >= int(millas):
            print('Se puede realizar el canje')
        else:
         print('Error de operacion')

    def __gt__(self, other):
        if int(self.__millasacum) > int(other.getmillas()):
          return  True
        else:
            return False

    def __add__(self, other):
        if other != type(self):
           return viajero(self.__numeroviajero,self.__dni,self.__nombre,self.__apellido,int(self.__millasacum)+int(other))

    def __sub__(self, other):
      if other != type(self):
          if int(other) <= int(self.__millasacum):
           return viajero(self.__numeroviajero,self.__dni,self.__nombre,self.__apellido,int(self.__millasacum)-int(other))
          else:
              print('no se puede canjear')
              return viajero(self.__numeroviajero, self.__dni, self.__nombre, self.__apellido,
                             int(self.__millasacum))
    def __rsub__(self, other):
        if other != type(self):
            if int(other) <= int(self.__millasacum):
                return viajero(self.__numeroviajero, self.__dni, self.__nombre, self.__apellido,
                               int(self.__millasacum) - int(other))
            else:
                print('no se puede canjear')
                return viajero(self.__numeroviajero, self.__dni, self.__nombre, self.__apellido,
                               int(self.__millasacum))
