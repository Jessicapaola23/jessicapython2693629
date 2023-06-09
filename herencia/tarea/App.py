from Usuario import*
from Libro import*
from estudiante import*
from Cuenta import*

Estudiante=Usuario('Jessica',1011107275,'Soacha')
infoLibro=Libro('cien años de soledad','gabriel garcia marquez',1978)
#print(type(Estudiante))
print(Estudiante.getNombre())
print(Estudiante.getDocumento())
print(Estudiante.getDepartamento())
print(infoLibro.getTitulo()) 
print(infoLibro.setAutor())
print(infoLibro.setFecha_publicacion())










