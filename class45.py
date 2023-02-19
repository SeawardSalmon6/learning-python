texto = "Hello"
iterator = iter(texto)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
