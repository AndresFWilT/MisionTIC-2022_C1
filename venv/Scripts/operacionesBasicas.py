def division(a,b):
    try:
        coc = a//b;
        res = a%b;
        return coc,res;
    except:
        return ("Error en la division de: ",a," entre ",b);

def multiplicacion(a,b):
    return a*b;

def suma(a,b):
    return a+b;

def resta(a,b):
    return a-b;

try:
    a = float(input("Ingrese el valor del primer numero: "));
    b = float(input("Ingrese el valor del segundo numero: "));
    print("la suma de los numeros", a, " + ", b, " es: ", suma(a, b));
    print("la resta de los numeros", a, " - ", b, " es: ", resta(a, b));
    print("la multiplicacion de los numeros", a, " * ", b, " es: ", multiplicacion(a, b));
    print("la division de los numeros", a, " / ", b, " es: ", division(a, b));
except :
    print("Ingrese un valor valido");

##Para logaritmos
def log_entero(num,base=2):
    cont = 0;
    while num >= base:
        cont = num;
        num /= base;
    return num;

print(log_entero(1024));