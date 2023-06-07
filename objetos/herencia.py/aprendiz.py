from persona import *   #importa los metodos de persona y curso 
from curso import *

class Aprendiz(Persona):
    def __init__(self,nombre,documento,formacion,ficha):
        Persona.__init__(self,nombre,documento)
        self.__formacion=formacion
        self.__ficha=ficha
        self.__cursos=[]   #este es el contructor 

    def agregarCurso(self,curso):  #este metodo sirve para agregar los cursos realizados 
        self.__cursos.append(curso)

    def componerCurso(self):
        nombreCurso=input('Ingrese nombre del curso')
        tipoCurso=input('Ingrese tipo del curso')
        objcurso=Curso(nombreCurso,tipoCurso)
        self.__cursos.append(objcurso)          #de la linea 14 a la 18 se crea el metodo y nos indica agregar un nombre del curso y un tipo, asi se agrega a la lista de cursos 

    def verCursos(self):
        return self.__cursos    #sirve para que podamos ver los cursos ingresados anteriormente 