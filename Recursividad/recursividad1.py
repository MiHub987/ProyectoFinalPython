"""Calcular el factorial de un numero"""
def recurs(num):
    numeros = num -1
    if (num == 2):
        return 2
    else:
        return numeros

recurs(5)

def iterativa(num):
    result = 1
    for i in range(num):
        result*=(i+1)
    return result


iterativa(5)
