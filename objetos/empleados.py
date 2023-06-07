class empleados:
    def __init__(self,nombre,cargo,salario,horas):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario

    def setNombre(self,nombre):
        self.__nombre=nombre
    def setCargo(self,cargo):
        self.__cargo=cargo
    def setSalario(self,salario):
        self.__salario=salario
    def setHorasExtra(self,horas):
        self.__horas=horas

    def getNombre(self):
        return self.__nombre
    def getCargo(self):
        return self.__cargo
    def getSalario(self):
        return self.__salario
    def getHoras(self):
        return self.__salario/8
    def incremento(self,ipc):
        if self.__salario==1000:
            return self.__salario*(1+ipc+0.03)
        else:
            return self.__salario*(1+ipc)
    def horasextra(self,horasExtra):
        if horasExtra>2:
            return "No puede hacer mas de dos horas extra diarias"
        else:
            pagoExtras=self.__salario,horasExtra*1.5*horasExtra
            salarioTotal=self.__salario+horasExtra
            return salarioTotal
