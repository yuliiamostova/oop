def sum_ab(n):
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    a[0] = 1
    b[0] = 5
    if n >= 1:
        a[1] = 2
        b[1] = 5

    for k in range(2, n + 1):
        b[k] = b[k - 2] ** 2 - a[k - 1]
        a[k] = a[k - 2] + b[k] / 2

    s = 0

    for k in range(1, n + 1):
        s += (a[k] / b[k]) ** k
    return s


def main():
    n = int(input("Введіть n: "))
    result = sum_ab(n)
    print(result)


if __name__ == "__main__":
    main()