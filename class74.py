pessoa = {}

chave = "nome_completo"
pessoa[chave] = "hello"
pessoa["hey"] = "oi gato"
del pessoa[chave]
print(pessoa)

if pessoa.get("sobrenome") is None:
    print("Não existe")
