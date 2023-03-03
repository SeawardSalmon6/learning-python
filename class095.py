try:
    print(1)
    # print(8 / 0)
except ZeroDivisionError:
    print("Divisão por zero!")
else:
    print("Sem erros :)")
finally:
    print(2)
