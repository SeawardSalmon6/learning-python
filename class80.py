letra_secreta = "l"
letras = set()

while True:
    letra = input("Digite: ")
    letras.add(letra.lower())

    if letra_secreta in letras:
        print("\nParabéns, você encontrou a letra secreta!")
        break

    print(f"{letras}\n")
