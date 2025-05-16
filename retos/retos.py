###IMPORTS
import random;

##Reto hola mundo
print("hola mundo");
##Reto operaciones con numeros
a = int(input("ingrese el numero a: "));
b = int(input("Ingrese el numero b: "));
print("suma: "+str(a+b));
print("resta: "+str(a-b));
print("mult: "+str(a*b));
print("div: "+str(a/b));
##reto numero mayor
if(a>b):
    print("El numero mayor es: "+str(a));
    print("El numero menor es: "+str(b));
else:
    print("El numero mayor es: "+str(b));
    print("El numero menor es: "+str(a));

##Reto numero aleatorio
print("El numero aleatorio generado es: "+str(random.randrange(0,100)));