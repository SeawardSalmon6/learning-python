SENHA_PERMITIDA = "123456"

entrada = input("[E]ntrar [S]air: ").upper()

if entrada == "E":
    senha_digitada = input("Senha: ")

    if senha_digitada == SENHA_PERMITIDA:
        print("Seja bem-vindo")
    else:
        print("Senha incorreta")
else:
    print("Sair")
