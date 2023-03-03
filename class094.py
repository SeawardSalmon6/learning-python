a = 18
b = 0
try:
    print("Calculando...!")
    # p = s
    # c = a / b
    print("Calculei!")
except ZeroDivisionError as error:
    print("Divisão por zero!")
    print(f"Msg: {error}")
    print(f"Name: {error.__class__.__name__}")
except NameError as error:
    print("Variável inexistente!")
    print(f"Msg: {error}")
    print(f"Name: {error.__class__.__name__}")

print("Continuar...")
