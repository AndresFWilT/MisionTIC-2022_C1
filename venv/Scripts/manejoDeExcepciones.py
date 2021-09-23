def division_raise(a,b):
    if b==0:
        raise ZeroDivisionError("¡Error de division por cero!. Funcion: division_raise");
    else:
        coc = a//b;
        res = a%b;
        return (coc,res);

try:
    num = int(input("Ingrese un numero: "));
    re = 100/num; #Generar excepcion si se digito 0
    print(re);
except Exception as e:
    print(e,"\n", type(e));

try:
    print(division_raise(10,num));
except Exception as e:
    print(e, "\n", type(e));

print("Ejemplo para finally: ");
try:
    num = int(input("Ingrese un numero: "));
    re = 1/num;
except:
    print("Existe un error");
else:
    print("El resultado es: ",re);
finally:
    print("Aqui sucede lo que tenga que suceder si o si");