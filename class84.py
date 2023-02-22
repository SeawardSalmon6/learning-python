a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza",
}

# (a1, a2), b = pessoa.items()
# print(a, b)

dados_pessoa = {
    "idade": 16,
    "altura": 1.60,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)


def mostro_argumentos_nomeados(*args, **kwargs):
    print("Não nomeados:", args)
    for chave, valor in kwargs.items():
        print(f"{chave}={valor}")


mostro_argumentos_nomeados(1, 2, 3, 4, **pessoa_completa)
