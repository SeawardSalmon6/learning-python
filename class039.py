nome = "Luiz Otávio"
nova_string = ""

i = 0
while i < len(nome):
    nova_string += f"*{nome[i]}"
    i += 1

nova_string += "*"
print(nova_string)
