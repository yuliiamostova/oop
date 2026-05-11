def alternating_sum(n):
    s = 0
    for k in range(1, n + 1):
        s += (-1) ** (k - 1) / k
    return s


def main():
    n = int(input("Введіть n: "))
    result = alternating_sum(n)
    print(result)


if __name__ == "__main__":
    main()