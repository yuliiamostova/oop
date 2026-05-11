def determinant(n):
    if n == 1:
        return 2
    d0 = 1
    d1 = 2
    for k in range(2, n + 1):
        d = 2 * d1 - d0
        d0 = d1
        d1 = d
    return d1


def main():
    n = int(input("Введіть n: "))
    result = determinant(n)
    print(result)


if __name__ == "__main__":
    main()