def Porty(e,p):
    arreglo = "";
    punt=0;
    for i in range(len(p)):
        if(p[i] in e):
            punt+=1;
            arreglo += str(punt)+" ";
        else:
            arreglo += str(punt)+" ";
    return arreglo;

def Nick(e,p):
    arreglo = "";
    punt = 0;
    for i in range(len(p)):
        if (p[i] in e):
            punt += 1;
            arreglo += str(punt)+" ";
        else:
            arreglo += str(punt)+" ";
    return arreglo;

def puntuaciones(p,n):
    n = n.split();
    p = p.split();
    arreglo = "";
    for i in range(len(p)):
        ###Para empate
        if(int(n[i]) == int(p[i])):
            arreglo += "I";
        ##Para Nick
        elif(int(n[i]) > int(p[i])):
            arreglo += "N";
        ##Para porty
        elif(int(p[i]) > int(n[i])):
            arreglo += "P";
    return arreglo;

def separacion(p,n,pl):
    porty = p;
    nick = n;
    planetas = pl;
    porty = Porty(porty,planetas);
    nick = Nick(nick,planetas);
    return puntuaciones(porty,nick);


p = str(input());
n = str(input());
pl = str(input());
print(separacion(p,n,pl));