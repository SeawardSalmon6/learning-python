lista = [
    ("lista", []),
    ("dicionario", {}),
    ("conjunto", set()),
    ("tupla", ()),
    ("string", ""),
    ("inteiro", 0),
    ("flutuante", 0.0),
    ("nada", None),
    ("falso", False),
    ("intervalo", range(0)),
]


def falsy(valor):
    return "falsy" if not valor else "truthy"


for (nome, valor) in lista:
    print(f"{nome}: {valor}\t--> {falsy(valor)}")
