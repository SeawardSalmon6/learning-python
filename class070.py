def executa(funcao, *args):
    return funcao(*args)


def saudacao(msg, nome):
    return f"{msg}, {nome}"


print(executa(saudacao, "hello", "world"))
