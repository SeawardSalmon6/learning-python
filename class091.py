from sys import getsizeof

iterable = ["eu", "tenho", "__iter__"]
iterator = iter(iterable)
# print(next(iterator))
# print(list(iterator))

# lista = [n for n in range(1000)]
generator = (n for n in range(1000))
# print(getsizeof(lista))
print(getsizeof(generator))

for n in generator:
    print(n, end=" ")
