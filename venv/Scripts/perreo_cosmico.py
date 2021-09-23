##Libreria para el reto 5
def tipo_melenudos(lista):
    '''
    :param lista: lista de alienigenas
    :return lista sin repetir:
    '''
    l = [];
    for elemento in lista:
        if elemento not in l:
            l.append(elemento);
    return l;

def si_son(turno,alien,validar):
    '''
    :param turno: turnos dados
    :param alien: razas encontradas en la lista
    :param validar: raza a verificar posicion
    :return: aliens que corresponden efectivamente en los turnos
    '''
    sillas = [];
    for i in range(len(turno)):
        if(alien[turno[i]] == validar):
            sillas.append(turno[i]);
    return sillas;

def no_estan(turnoN,turnoP):
    '''
    :param turnoN: turnos en la fila de nick
    :param turnoP: turnos en la fila de porty
    :return:
    '''
    lista = []
    for i in range(len(turnoN)):
        for j in range(len(turnoP)):
            if (turnoN[i] == turnoP[j]):
                break;
            elif((j == len(turnoP)-1) and (turnoN[i] != turnoP[j])):
                lista.append(turnoN[i]);
    return lista;

def uno_y_uno(listaN,listaP):
    '''
    :param listN: lista de invitados Nick
    :param listaP:  lista de invitados Porty
    :return: retorna la cantidad de alienigenas de cada lista que podrian entrar al evento
    '''
    cantidadN = [];
    cantidadP = [];
    ##Para Nick
    for i in range(len(listaN)):
        for j in range(len(listaP)):
            if (listaN[i] == listaP[j]):
                break;
            elif ((j == len(listaP) - 1) and (listaN[i] != listaP[j])):
                cantidadN.append(listaN[i]);
    ##Para porty:
    for i in range(len(listaP)):
        for j in range(len(listaN)):
            if (listaP[i] == listaN[j]):
                break;
            elif ((j == len(listaN) - 1) and (listaP[i] != listaN[j])):
                cantidadP.append(listaP[i]);
    return len(cantidadP) if (len(cantidadP) < len(cantidadN)) else len(cantidadN);