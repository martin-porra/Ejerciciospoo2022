from ClaseEmail import emai
import csv

if __name__ == '__main__':
    print('ingresar nombre para crear cuenta')
    nom = input()
    print ('ingresar id cuenta (ej: martin), dominio (ej: gmail) , tipo dominio (ej: com)')
    id = input()
    dom = input()
    tipo = input()
    print('ingresar contraseña de la cuenta')
    contra = input()
    email = emai(id,dom,tipo,contra)
    cadena = email.retorna()
    print('Estimado '+ nom + ' te enviaremos tus mensajes a la dirección ' + cadena)
    print('')
    print('ingresar contraseña para cambiar contraseña actual por una nueva')
    actual = input()
    email.setcontra(actual)
    correo = emai()
    print('ingresar correo que desea para crear objeto clase de email, ejemplo: "juanLiendro1957@yahoo.com"')
    ejemplo = input()
    a = ejemplo.find('@')
    c = ejemplo.find('.')
    while a == -1 or c == -1:
      print ('el correo no es valido le falta "@" o "."')
      print('ingresar correo que desea para crear objeto clase de email, ejemplo: "juanLiendro1957@yahoo.com"')
      ejemplo = input()
      a = ejemplo.find('@')
      c = ejemplo.find('.')
    correo.crearcuenta(ejemplo)
    print(correo.retorna())
    print('lista')
    lista = []
    archivo = open('emails.txt')
    reader = csv.reader(archivo,delimiter=',')
    for fila in reader:
     co = emai()
     s = str(fila)
     co.crearcuenta(s)
     lista.append(co)
    archivo.close()
    print('buscar identificador que ingrese')
    domi = input()
    suma = 0
    for x in range(0, len(lista)):
     cant = lista[x].retorna().count(domi)
     suma = suma + cant
    if suma > 1:
        print ('El identificador se repite')
    else:
        print('El identificador no se repite')
