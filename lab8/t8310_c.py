def determinant_sequence():
    d0 = 1
    d1 = 2
    yield d0
    yield d1
    while True:
        d = 2 * d1 - d0
        yield d
        d0 = d1
        d1 = d


def determinant(n):
    generator = determinant_sequence()
    for i in range(n + 1):
        result = next(generator)
    return result


def main():
    n = int(input())
    result = determinant(n)
    print(result)


if __name__ == "__main__":
    main()