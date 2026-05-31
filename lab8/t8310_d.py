def ab_sequence():
    a0 = 1
    b0 = 5
    a1 = 2
    b1 = 5
    yield a1, b1
    while True:
        b = b0 ** 2 - a1
        a = a0 + b / 2
        yield a, b
        a0 = a1
        b0 = b1
        a1 = a
        b1 = b

def sum_ab(n):
    generator = ab_sequence()
    s = 0
    for k in range(1, n + 1):
        a, b = next(generator)
        s += (a / b) ** k
    return s


def main():
    n = int(input())
    result = sum_ab(n)
    print(result)


if __name__ == "__main__":
    main()