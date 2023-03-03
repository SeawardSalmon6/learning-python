## Exercício 01
def mult(*args):
    mult = 1
    for number in args:
        mult *= number or 1
    return mult


resultado = mult(10, 12, 4, 6)
print(resultado)

## Exercício 02
def par_impar(numero):
    texto = "ímpar" if (numero or 0) % 2 else "par"
    return f"{numero} é {texto}"


print(par_impar(1))
print(par_impar(2))
print(par_impar(3))
print(par_impar(112))
