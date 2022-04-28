from  ManejadorPlanes import ManejadorPlan
from menu import  menu
if __name__ == '__main__':
    manejador = ManejadorPlan()
    men = menu()
    men.opcion(manejador)