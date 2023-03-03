x = 1
y = 0


def escopo():
    y = 7

    def funcao():
        print(y)

    x = 10
    y = 1122


print(x, y)
escopo()
print(x, y)
