def element_sequence(x):
    k = 1
    element = -x ** 3 / 6
    while True:
        yield element
        element = -element * x ** 2 / (
            (2 * k) * (2 * k + 1) * (2 * k + 2) * (2 * k + 3)
        )
        k += 1

def get_element(x, k):
    generator = element_sequence(x)
    for i in range(1, k + 1):
        element = next(generator)
    return element


def main():
    x = float(input())
    k = int(input())
    result = get_element(x, k)
    print(result)

if __name__ == "__main__":
    main()
