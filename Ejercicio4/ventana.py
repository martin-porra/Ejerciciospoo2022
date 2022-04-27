class Ventana:
    __titulo = None
    __sx = None
    __sy = None
    __ix = None
    __iy = None

    def __init__(self,titulo, sx=0, sy=0,ix=500, iy=500):
        self.__titulo = titulo
        if int(sx) < 0 or int(sy) < 0:
            print('error')
        else:
         self.__sx = sx
         self.__sy = sy
        if int(ix) > 500 or int(iy) > 500:
            print('error')
        else:
            self.__ix = ix
            self.__iy = iy

    def mostrar(self):
        print('vertices superior izquierdo', '(', int(self.__sx), ',', int(self.__sy),')',)
        print('vertice inferior derecho', '(', int(self.__ix), ',', int(self.__iy),')',)

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        alto= self.__iy - self.__sy
        return alto
    def ancho(self):
        ancho = self.__ix - self.__sx
        return ancho
    def moverDerecha(self,x=0):
        if self.__sx + x <= 500 and self.__ix + x <= 500:
            self.__sx += x
            self.__ix += x
        else:
            print('No se puede mover la ventana, Error')
    def moverIzquierda(self,x=0):
        if self.__sx - x >=0  and self.__ix - x >= 0:
            self.__sx -=x
            self.__ix -=x
        else:
            print('No se puede mover la ventana')

    def bajar(self,y=0):
        if self.__sy - y >= 0 and self.__iy - y >= 0:
            self.__sy -=y
            self.__iy -=y
        else:
            print('No se puede bajar la ventana')

    def subir(self,y=0):
        if self.__sy + y <= 500 and self.__iy + y <=500:
          self.__sy +=y
          self.__iy +=y
        else:
            print('No se puede subir la ventana')