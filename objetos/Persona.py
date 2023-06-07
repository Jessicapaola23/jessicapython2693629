#Escriba una clase de Empleado que tenga como propiedades
#nombre, cargo, salario
#escribas metodos constructores, setters y getters
#escriba un metodo que permita calcular cuanto gana el empleado en una hora
#un método para saber cuánto recibe de incremento si el salario sube con el IPC. Si gana el minimo se le aumenta el ipc + 3%
#Un método que recibe una cantidad de horas extras y calcula el salario incrementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. valido
#Anexar variable de clase que cuente cantidad de objetos creados de esa clase


class Persona:
    
    def __init__(self,nombre,documento):
        #print('Se instancio un objeto')
        self.__nombre=nombre
        self.__documento=documento
        #self.__telefono
        #self.__cursos=[]

    def setNombre(self,nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setDocumento(self,documento):
        self.__documento=documento

    def getDocumento(self):
        return self.__documento












    
    
    