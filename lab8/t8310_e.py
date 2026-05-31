import math

def cos_elements(x):
    k = 0
    element = 1
    while True:
        yield element
        k += 1
        element = -element * x ** 2 / ((2 * k - 1) * (2 * k))


def cos_taylor(x, eps):
    generator = cos_elements(x)
    s = 0
    while True:
        element = next(generator)
        s += element
        if abs(element) <= eps:
            return s


def main():
    x = float(input())
    eps = float(input())
    result = cos_taylor(x, eps)
    library_result = math.cos(x)

    print("cos(x) за рядом Тейлора^: ", result)
    print("cos(x) з бібліотеки math: ", library_result)
    print("Різниця: ", abs(result - library_result))


if __name__ == "__main__":
    main()