from aprendiz import *   #importa los metodos 
from curso import *

objeto=Aprendiz("Ana Kurnikova",123456,'ADSO',2693629) #nos va a mostrar esta informacion agregada
#print(objeto.__dict__)
objcurso=Curso("Programacion Software","tecnico") #nos  muestra los cursos que ha realizado 
objeto.agregarCurso(objcurso)  #esta linea de codigo imprime los cursos realizados 
#print(objeto.__dict__)
objeto.componerCurso()
objeto.componerCurso()
#print(objeto.verCursos())
for cursito in objeto.verCursos():   
    print(cursito.getNombre())