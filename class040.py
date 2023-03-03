while True:
    op = input("Digite a operação da calculadora (+-*/) ou digite 's' para sair: ")

    if op.lower() == "s":
        break

    eh_operacao = op in "+-*/"

    if not eh_operacao:
        print("Operação inválida!")
        continue

    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    except:
        print("Um ou ambos dos valores não são números!")
        break

    if op == "+":
        resultado = n1 + n2
    elif op == "-":
        resultado = n1 - n2
    elif op == "*":
        resultado = n1 * n2
    else:
        if n2:
            resultado = n1 / n2
        else:
            resultado = None
            print("Divisão por zero não é permitida")

    print(f"{n1} {op} {n2} = {resultado}")
