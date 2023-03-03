from pprint import pprint

# print(list(range(10)))
l1 = []
for numero in range(10):
    l1.append(numero)
# print(l1)

l2 = [numero * 2 for numero in range(10)]
# print(l2)

produtos = [
    {"nome": "p1", "preco": 20},
    {"nome": "p2", "preco": 10},
    {"nome": "p3", "preco": 30},
]

novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
    if produto["preco"] > 20
    else produto
    for produto in produtos
    if produto["preco"] > 10
]

# print(*novos_produtos, sep="\n")
pprint(novos_produtos)

l3 = [n for n in range(10) if n < 5]
print(l3)
