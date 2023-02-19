from os import system

lista_compras = []
op = ""
val = None

while op != "0":
    print("\n===== Menu")
    print("(1) Inserir na lista")
    print("(2) Remover da lista")
    print("(3) Mostrar a lista")
    print("(0) Sair")
    op = input("\n--> Digite a opção: ")

    if op not in ["1", "2", "3", "0"]:
        print("\n!--> Insira uma opção válida: ")
        continue

    system("clear")

    if op == "1":
        val = input("\n--> Digite o item a ser inserido: ")

        if not val:
            print("\n!--> Insira um valor!")
        else:
            lista_compras.append(val)
            print("\n--> Valor inserido com sucesso!")

    elif op == "2":
        if len(lista_compras) > 0:
            print("==> Lista de Compras")
            for i, item in enumerate(lista_compras):
                print(f"{i + 1}: {item}")
        else:
            print("\n--> Lista Vazia")
            continue

        val = input("\n--> Digite o número do item a ser removido: ")

        try:
            val = int(val)

            if val < 1 or val > len(lista_compras):
                print("\n!--> Insira um valor válido!")
            else:
                lista_compras.pop(val - 1)
                print("\n--> Valor removido com sucesso!")
        except:
            print("\n!--> O valor digitado não é um valor válido!")

    elif op == "3":
        if len(lista_compras) > 0:
            print("==> Lista de Compras")
            for i, item in enumerate(lista_compras):
                print(f"{i + 1}: {item}")
        else:
            print("\n--> Lista Vazia")
