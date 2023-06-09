class Libro:
    def __init__(self,titulo,autor,fecha_publicacion):
        self.__titulo=titulo
        self.__autor=autor
        self.__fecha_publicacion=fecha_publicacion
        
    def setTitulo(self,titulo): 
        self.__titulo=titulo
    def getTitulo(self):
        return self.__titulo
    
    def setAutor(self,autor): 
        self.__autor=autor
    def getTitulo(self):
        return self.__autor
    
    def setFecha_publicacion(self,fecha_publicacion): 
        self.__fecha_publicacion=fecha_publicacion
    def getTitulo(self):
        return self.__fecha_publicacion
    
    
    
    
    
        
    #def informacionLibro(self):
    #titulo=input('Ingrese titulo del libro: ')
    #autor=input('Ingrese autor del libro: ')
    #publicacion=input('Ingrese fecha de publicacion del libro: ')

