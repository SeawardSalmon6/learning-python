# Exercício 01
entrada = input("Digite um número inteiro: ")

try:
    numero = float(entrada)
    eh_par_impar = numero % 2 and "ímpar" or "par"

    if numero.is_integer():
        print(f"O número {numero:.0f} é {eh_par_impar}")
    else:
        print("O número inserido não é inteiro!")
except:
    print("O valor inserido não é um número!")


# Exercício 02
entrada = input("Que horas são? ")

try:
    horario = int(entrada)

    if horario >= 0 and horario < 12:
        print("Bom dia!")
    elif horario >= 12 and horario < 18:
        print("Boa tarde!")
    elif horario >= 18 and horario < 24:
        print("Boa noite!")
    else:
        print("O horário inserido não é válido!")
except:
    print("O valor inserido não é um número inteiro!")

# Exercício 03
nome = input("Qual o seu nome? ")
qtd_letras_nome = len(nome)

if qtd_letras_nome <= 4:
    print("Seu nome é curto")
elif qtd_letras_nome >= 5 and qtd_letras_nome <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
