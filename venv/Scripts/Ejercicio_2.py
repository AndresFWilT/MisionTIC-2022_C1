## Script que calcula si un numero ingresado es positivo, negativo o neutro
def calcular(numero):
    if(numero > 0):
        return "El numero "+ str(numero)+" es positivo.";
    elif(numero == 0):
        return "El numero " + str(numero) + " es el neutro para la suma.";
    else:
        return "El numero " + str(numero) + " es negativo.";
print("Ingrese un numero: ");
a = float(input());
print(calcular(a));