class Cama:
 __idCama = None
 __Habitacion = None
 __Estado = bool
 __NombreyApellido = None
 __Diagnostico = None
 __FechaDeInternacion = None
 __FechaDeAlta = None

 def __init__(self,idcama,habitacion,estado,nombre,diagnostico,fechainterancion,fechaalta):
  if int(idcama) < 30 and int(idcama) > 0:
   if not estado:
    self.__idCama = idcama
    self.__Habitacion = habitacion
    self.__Estado = estado
    self.__NombreyApellido = None
    self.__Diagnostico = diagnostico
    self.__FechaDeInternacion = fechainterancion
    self.__FechaDeAlta = fechaalta
   else:
    self.__idCama = idcama
    self.__Habitacion = habitacion
    self.__Estado = estado
    self.__NombreyApellido = nombre
    self.__Diagnostico = diagnostico
    self.__FechaDeInternacion = fechainterancion
    self.__FechaDeAlta = fechaalta
  else:
   print('Error')
 def getid(self):
   return self.__idCama
 def getNombre(self):
  return self.__NombreyApellido
 def getHabitacion(self):
  return self.__Habitacion
 def getEstado(self):
  return self.__Estado
 def getDiagnostico(self):
  return self.__Diagnostico
 def getFechainternacion(self):
  return self.__FechaDeInternacion
 def getFechaalta(self):
  return self.__FechaDeAlta
 def ingresarFechaalta(self,fecha):
   self.__FechaDeAlta = fecha
 def ingresarEstado(self,false):
  self.__Estado = false
 def ingresarnombre(self,none):
  self.__NombreyApellido = none

 def __str__(self):
  return 'Nombre: {nombre}      Cama:{cama}        Habitación:{habitacion}       Fecha internacion:{fecha}'.format(nombre=self.__NombreyApellido,cama=self.__idCama,habitacion=self.__Habitacion,fecha=self.__FechaDeInternacion)

