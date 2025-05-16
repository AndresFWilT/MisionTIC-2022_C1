def factorial(n):
    '''
    funcion que calcula el factorial de un numero ingresado
    :param n:
    :return fac(n):
    '''
    if(n==0):
        return 1;
    else:
        return n * (factorial(n - 1));

