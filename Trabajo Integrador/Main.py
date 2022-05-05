from ManejadorMedicamento import ManejaMedicamento
from ManejadorCamas import  ManejadorCamas
if __name__ == '__main__':
    manejamedicamentos = ManejaMedicamento()
    manejamedicamentos.Cargar()
    manejacamas = ManejadorCamas()
    manejacamas.Cargar()
    nombrepaciente = input('Ingrese el nombre de algun paciente para dar el alta:')
    manejacamas.DarAlta(nombrepaciente,manejamedicamentos)
    diagnostico = input('Ingrese un diagnostico para listar pacientes: ')
    print('----------- LISTA DE PACIENTES CON ESE DIAGNOSTICO ----------')
    manejacamas.mostrarDatos(diagnostico)