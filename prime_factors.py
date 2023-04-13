import doctest


def prime_factors(value):
    """
    >>> value = 15
    >>> primefactors(value)
    [3, 5]
    >>> value = 36
    >>> primefactors(value)
    [2, 2, 3, 3]
    """
    divisor = 2
    factors = []
    while divisor * divisor <= value:
        if value % divisor:
            divisor += 1
        else:
            value //= divisor
            factors.append(divisor)
    if value > 1:
        factors.append(value)
    return factors


def convert_to_tuple(factors):
    """
    >>> factors = [3, 5]
    >>> convert(factors)
    (3, 5)
    >>> factors = [2, 2, 3, 3]
    >>> convert(factors)
    (2, 2, 3, 3)
    """
    return tuple(factors)


def main():
    doctest.testmod(verbose=True)
    value = "hi"
    factors = []
    try:
        if isinstance(value, int):
            factors = prime_factors(value)
            print(convert_to_tuple(factors))
        else:
            raise ValueError
    except ValueError:
        print("Please enter an integer")


if __name__ == "__main__":
    main()
