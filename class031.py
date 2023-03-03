v1 = "a"
v2 = "a"
print(id(v1))
print(id(v2))

condicao = False
passou = None

if condicao:
    passou = True
    print("Faça algo")
else:
    print("Não faça algo")

if passou is not None:
    print("Passou no if")
else:
    print("Não passou no if")
