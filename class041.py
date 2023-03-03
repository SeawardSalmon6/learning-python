string = "valorqualquer"

i = 0
while i < len(string):
    letra = string[i]
    print(letra, end="")

    if letra == " ":
        break

    i += 1
else:
    print("Else nego")

print("Fim")
