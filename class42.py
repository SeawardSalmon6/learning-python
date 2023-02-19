frase = "O Python é uma linguagem de programação multiparadigma. \
        Python foi criado por Guido van Rossum."

i = 0
count_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""
while i < len(frase):
    letra_atual = frase[i]
    qtd_aparicoes_da_letra = letra_atual != " " and frase.count(letra_atual)

    if qtd_aparicoes_da_letra > count_apareceu_mais_vezes:
        count_apareceu_mais_vezes = qtd_aparicoes_da_letra
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f"A letra que apareceu mais vezes é: {letra_apareceu_mais_vezes}")
