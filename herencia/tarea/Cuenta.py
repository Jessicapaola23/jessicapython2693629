class Cuenta:
    def __init__(self,libros_prestados, libros_reservados,libros_devueltos, libros_perdidos, monto_multa): #constructor
        self.__libros_prestados=libros_prestados
        self.__libros_reservados=libros_reservados
        self.__libros_devueltos=libros_devueltos
        self.__libros_perdidos=libros_perdidos
        self.__monto_multa=monto_multa

    

#calcuar fila