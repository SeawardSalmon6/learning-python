from pprint import pprint as p

string = "Luiz"
metodo = "upper1"
p(dir(string))
print()

if hasattr(string, metodo):
    print("Existe upper!")
    print(getattr(string, metodo)())
else:
    print(f"{metodo} não existe")
