def soma(*args):
    soma = 0
    for numero in args:
        soma += numero or 0
    return soma


print(soma(1, 2, 3, 4, 5))
print(sum((1, 2, 3, 4, 5)))
