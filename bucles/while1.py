yo = 1
suma = 0
#indentacion
while  yo <= 10 :
    print ( yo )
    suma += yo  #suma=suma+i
    yo += 1  #i=i+1
    print( 'la suma es:' , suma )

yo = 0
sp , si = 0 , 0
while  yo <= 10 :
      print ( yo )
      if yo % 2 == 0 :
        sp += yo
      else :
        si += yo
        yo += 1
print ( 'la suma de los pares es:' , sp )
print ( 'la suma de los impares es:' , si )