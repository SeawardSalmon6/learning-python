def python(param: str = "") -> bool:
    print("Something", param)
    return not not param


print(python(""))
