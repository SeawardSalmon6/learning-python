from random import randint

cpf = ""
for i in range(9):
    cpf += str(randint(0, 9))

# ============ Cálculo Primeiro Dígito
i = 0
soma = 0
for digito in cpf:
    soma += int(digito, 10) * (10 - i)
    i += 1

digito = (soma * 10) % 11
digito_1 = 0 if digito > 9 else digito
cpf += str(digito_1)

# ============ Cálculo Segundo Dígito
i = 0
soma = 0
for digito in cpf:
    soma += int(digito, 10) * (11 - i)
    i += 1

digito = (soma * 10) % 11
digito_2 = 0 if digito > 9 else digito
cpf += str(digito_2)

print(f"   CPF Gerado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[-2:]}")
print(f"Sem pontuação: {cpf}")
