def msjOrigi(m):
    msj = "";
    for i in range(len(m)):
        msj += m[i] + " ";
    return msj;

def mensajeEncr(d,m):
    encr = "";
    for i in range(len(m)):
        for j in range(len(d)):
            if(m[i]== d[j]):
                try:
                    encr += d[j+1];
                except:
                    print("");

    return encr + "\n" +msjOrigi(m);

def separar(dicc,mensaje):
    m = mensaje.split(",");
    d = [];
    for i in range(len(dicc)):
        try:
            if (dicc[i-1] == '"' and dicc[i+1] =='"'):
                d.extend(dicc[i]);
        except:
            print("");
    return mensajeEncr(d,m);


diccionario = input(str("Ingrese el diccionario: "));
mensaje = input(str("Ingrese el mensaje encriptado: "));
print(separar(diccionario,mensaje));