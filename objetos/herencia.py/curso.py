class Curso:
    def __init__(self,nombre,tipo):   #nos pide el nombre y tipo de los cursos realizados 
        self.__nombre=nombre
        self.__tipo=tipo

    def getNombre(self):
        return self.__nombre