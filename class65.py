def soma(x=None, y=None, z=None):
    resultado = (x or 0) + (y or 0) + (z or 0)
    return resultado


soma(1, 2, 3)
soma(3, 23, 23)
soma(y=2100, z=888, x=200)
