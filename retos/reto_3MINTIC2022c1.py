##Ingresa valores separados por guion, devuelve esos valores separados
##Por espacio y solo uno, teniendo en cuenta si estan repetidos seguidos
##tambien devuelve un array con el numero de repeticiones por valor
def separacion(v):
    '''
    funcion que recibe una entrada, y separa los valores en una lista, segun algun valor
    que este en el medio
    :param v:
    :return valor separado:
    '''
    v = v.split("-");
    return v;

def borrarSeparados(v):
    '''
    Funcion que borra los valores repetidos
    :param v:
    :return: borrar separados
    '''
    VSR = []
    repetidos = []
    for i in range(len(v)):
        ##puntaje
        valor = 1;
        try:
            while (v[i] == v[i + 1]):
                valor += 1;
                v.pop(i);
            repetidos.extend(str(valor));
            VSR.extend(v[i]);
        except:
            None
    retorno = "";
    for i in range(len(VSR)):
        retorno += VSR[i]+" ";
    retorno += "\n";
    for i in range(len(repetidos)):
        retorno += repetidos[i]+" ";
    return retorno;

def iniciar(v):
    '''
    funcion que hace el objetivo del programa
    :param entrada:
    :return impresion:
    '''
    v = separacion(v);
    v = borrarSeparados(v);
    return v;

##Para la entrada del programa

try:
    entrada = str(input());
    entrada += "-s";
    print(iniciar(entrada));
except:
    print("Entrada no valida");