import math


def cos_taylor(x, eps):
    term = 1
    s = term
    k = 1
    while abs(term) > eps:
        term = -term * x ** 2 / ((2 * k - 1) * (2 * k))
        s += term
        k += 1
    return s


def main():
    x = float(input("Введіть x: "))
    eps = float(input("Введіть eps: "))
    result = cos_taylor(x, eps)
    library_result = math.cos(x)
    print("cos(x) за рядом Тейлора =", result)
    print("cos(x) з бібліотеки math =", library_result)
    print("Різниця:", abs(result - library_result))


if __name__ == "__main__":
    main()