def gen1():
    yield 1
    yield 2
    yield 3


def gen2(gen=None):
    if gen is not None:
        yield from gen
    yield 5
    yield 6


g = gen2()
for numero in g:
    print(numero)
