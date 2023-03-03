def divide(n: (float), d: (float)) -> float:
    try:
        return n / d
    except (ZeroDivisionError):
        print("--> Erro: denominador não pode ser 0!")
    except TypeError:
        raise
    return 0


def main() -> None:
    print(divide(1, 2))


if __name__ == "__main__":
    main()
