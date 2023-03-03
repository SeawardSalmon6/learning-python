pessoa = {
    "nome": "Jean Achour",
    "sobrenome": "Miranda",
    "idade": 18,
    "altura": 1.8,
    "enderecos": [
        {"rua": "tal tal", "numero": 123},
        {"rua": "outra rua", "numero": 321},
    ],
}

for i, chave in enumerate(pessoa):
    print(i, pessoa[chave])
