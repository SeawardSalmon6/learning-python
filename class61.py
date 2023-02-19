from re import sub

cpf = input("Insira o CPF para validação: ")

if len(cpf) < 11:
    print("Erro: quantidade mínima de dígitos inválida!")
    exit(-1)
elif len(cpf) > 11:
    cpf = sub(r"[^0-9]", "", cpf)

if len(cpf) != 11:
    print("Erro: o valor inserido não é válido como um CPF!")
    exit(-1)

print(f"O CPF inserido foi: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[-2:]}")

if cpf == cpf[0] * len(cpf):
    print("Resultado: CPF Inválido!")
    exit(0)

# ============ Cálculo Primeiro Dígito
cpf_corpo_numeros = list(cpf[:9])

i = 0
soma = 0
for digito in cpf_corpo_numeros:
    soma += int(digito, 10) * (10 - i)
    i += 1

digito = (soma * 10) % 11
primeiro_digito_validador = 0 if digito > 9 else digito

print(f"O primeiro dígito deve ser: {primeiro_digito_validador}")

if int(cpf[-2]) != primeiro_digito_validador:
    print("Resultado: CPF Inválido, o primeiro dígito verificador não confere!")
    exit(0)

# ============ Cálculo Segundo Dígito
cpf_corpo_numeros += str(primeiro_digito_validador)

i = 0
soma = 0
for digito in cpf_corpo_numeros:
    soma += int(digito, 10) * (11 - i)
    i += 1

digito = (soma * 10) % 11
segundo_digito_validador = 0 if digito > 9 else digito

print(f"O segundo dígito deve ser: {segundo_digito_validador}")

if int(cpf[-1]) != segundo_digito_validador:
    print("Resultado: CPF Inválido, o segundo dígito verificador não confere!")
else:
    print("Resultado: CPF Válido, ambos os dígitos verificadores são válidos!")
