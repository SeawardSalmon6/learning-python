def criar_multiplicador(multiplicador):
    def mult_razao(num):
        return num * multiplicador

    return mult_razao


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))
