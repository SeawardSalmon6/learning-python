def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"

    return saudar


falar_bomdia = criar_saudacao("Bom dia")
falar_boanoite = criar_saudacao("Bom noite")

for nome in ["Maria", "João", "Luiz"]:
    print(falar_bomdia(nome))
    print(falar_boanoite(nome))
