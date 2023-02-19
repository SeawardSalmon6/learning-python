contador = 0

while contador < 100:
    contador += 1

    if contador % 2:
        continue

    print(contador)

    if contador == 40:
        break
