class Usuario: #clase usuario
    def __init__(self,nombre,documento,departamento): #constructor de la clase 
        self.__nombre=nombre
        self.__documento=documento
        self.__departamento=departamento
        
    def setNombre(self,nombre): 
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
                                     #setters y getters

    def setDocumento(self,documento):
        self.__documento=documento

    def getDocumento(self):
        return self.__documento
    
    
    def setDepartamento(self,departamento): 
        self.__departamento=departamento

    def getDepartamento(self):
        return self.__departamento
    