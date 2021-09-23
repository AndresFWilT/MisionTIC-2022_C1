def estrato(valor):
    if(valor>=0 and valor <21):
        return "\nuno";
    elif(valor>=21 and valor <31):
        return "\ndos";
    elif(valor>=31 and valor <51):
        return "\ntres";
    elif(valor >= 51):
        return "\ncuatro";
    else:
        return False;

def calculo(a):
    ##Betty
    b = (a+2)*2;
    ##Camilo
    c = int((a + b)/5);
    return str(a) + " " + str(b) + " " + str(c) + " " +estrato(c);

def validacion(valor):
    if(str.isdigit(valor)):
        return calculo(int(valor));
    else:
        return "Ingrese un valor valido";

valor = input();
print(validacion(valor));