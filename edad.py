NomUsuario = raw_input("Ingrese Nombre de usuario")
FActual = 2016
nacimiento = input("Ingrese anio de nacimiento")

Edad = FActual - nacimiento 
print  NomUsuario + ": Su edad es de " 
print Edad

if Edad <= 12:
	print "ninio"
else:
	print "adolecente"