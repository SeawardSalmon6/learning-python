palavra_secreta = "vai_um_output_aí"
tamanho_palavra_secreta = len(palavra_secreta)
palavra_usuario = (tamanho_palavra_secreta) * "*"
tentativas = 0

while palavra_secreta != palavra_usuario:
    letra = input("Digite uma letra: ")

    if not letra:
        print("Por favor, insira uma letra!")
        continue

    if len(letra) > 1:
        print("Por favor, digite apenas uma letra!")
        continue

    if letra in palavra_secreta:
        for i in range(tamanho_palavra_secreta):
            if letra == palavra_secreta[i]:
                palavra_usuario = (
                    f"{palavra_usuario[:i]}{letra}{palavra_usuario[(i + 1):]}"
                )

    print(f"A palavra se encontra dessa forma:\t{palavra_usuario}")
    tentativas += 1

print("VOCÊ GANHOU, PARABÉNS!!")
print(f"A palavra secreta era:\t{palavra_secreta}")
print(f"Número de tentativas:\t{tentativas}")
