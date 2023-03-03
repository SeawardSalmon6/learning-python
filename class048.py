# const = list("something")
# const[4] = "T"
# print("".join(const))

# print("as".replace("", "hello", 2))

# lista = [10, 20, 30, 40]
# nome = lista.append("Luiz")
# print(lista, nome)

# del lista[-1]
# print(lista)

# lista.insert(-12, 2)
# print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)

lista_a.extend(lista_b)
print(lista_a, lista_b)

lista_c.clear()
print(lista_c)
