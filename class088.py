lista = ["alele", 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {"nome": "Luiz"}]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        item = item.upper()
        print(item, isinstance(item, str))

    elif isinstance(item, (int, float)):
        print("Número:", item, item * 2)
