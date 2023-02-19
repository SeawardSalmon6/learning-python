string = "ABCD"
lista = ["Maria", "Helena", "Hey", "Woh", "Eduarda"]
tupla = "Python", "é", "legal"
salas = [
    ["Maria", "Helena"],
    ["Elaine"],
    ["Luiz", "João", "Eduarda"],
]

# a, b, c, *_, u = lista
# print(a, u)

# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep="\n")
