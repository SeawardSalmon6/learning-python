try:
    numero = float(input("Vou dobrar o número que você digitar: "))
    print(f"O dobro de {numero:.2f} é {(numero * 2):.2f}")
except:
    print("Erro ao calcular")
