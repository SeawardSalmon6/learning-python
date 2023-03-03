def generator(n=0, maximum=10):
    while n <= maximum:
        yield n
        n += 1


n = 0
gen = generator(n)
for n in gen:
    print(n)
