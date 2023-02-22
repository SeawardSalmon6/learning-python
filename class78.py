## Exercício
def mostrar_opcoes(pergunta):
    print("\nOpções:")
    for i, opcao in enumerate(pergunta["Opções"]):
        print(f"{i}) {opcao}")
    print()
    return input("Escolha uma opção: ")


def eh_a_resposta_certa(pergunta, resposta):
    opcoes = pergunta["Opções"]
    acertou = False

    resposta_int = None
    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < len(opcoes):
            if opcoes[resposta_int] == pergunta["Resposta"]:
                acertou = True

    return acertou


perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]


qtd_acertos = 0
for pergunta in perguntas:
    print("Pergunta:", pergunta["Pergunta"])
    resposta = mostrar_opcoes(pergunta)

    if eh_a_resposta_certa(pergunta, resposta):
        print("\n--> Você acertou! 👍\n")
        qtd_acertos += 1
    else:
        print("\n--> Você errou! 😿\n")

print(f"Você acertou {qtd_acertos} de {len(perguntas)} perguntas.")
