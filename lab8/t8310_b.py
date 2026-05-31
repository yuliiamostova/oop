def alternating_elements():
    k = 1
    element = 1
    while True:
        yield element
        element = -element * k / (k + 1)
        k += 1

def alternating_sum(n):
    generator = alternating_elements()
    s = 0
    for i in range(n):
        s += next(generator)
    return s


def main():
    n = int(input())
    result = alternating_sum(n)
    print(result)


if __name__ == "__main__":
    main()