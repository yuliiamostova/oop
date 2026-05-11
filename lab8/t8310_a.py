import math

def element_sequence(x, k):
    numerator = (-1) ** k * x ** (2 * k + 1)
    denominator = math.factorial(2 * k - 1) * math.factorial(2 * k + 1)
    return numerator / denominator


def main():
    x = float(input("Введіть x: "))
    k = int(input("Введіть k: "))
    result = element_sequence(x, k)
    print(result)


if __name__ == "__main__":
    main()
