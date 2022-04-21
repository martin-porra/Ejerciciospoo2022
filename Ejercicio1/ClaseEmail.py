class emai:
  __idcuenta = ''
  __dominio = ''
  __tipodominio = ''
  __contraseña = ''

  def __init__(self, idcuenta = 'a', dominio = '', tipodominio= '', contra = 'a'):
   self.__idcuenta = idcuenta
   self.__dominio = dominio
   self.__tipodominio = tipodominio
   self.__contraseña = contra
  def retorna(self):
   return self.__idcuenta + '@' + self.__dominio +'.' + self.__tipodominio
  def getDominio(self):
   return self.__dominio
  def crearcuenta (self, cade):
   particion = cade.partition("@")
   parti = particion[2].split(".")
   self.__idcuenta = particion[0]
   self.__dominio = parti[0]
   self.__tipodominio = parti[1]
  def getcontra(self):
   return self.__contraseña
  def setcontra(self, actual):
   if self.__contraseña == actual:
    print ('ingrese nueva contraseña')
    nueva = input()
    self.__contraseña = nueva
    print('contraseña actualizada ' + nueva)
   else:
       print('contraseña diferentes')

if __name__ == '__main__':
    print ('ingresar nombre')