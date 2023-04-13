
import doctest

def check_for_primality(value):
    try:
        value == int(value)
    except ValueError:
        print("Enter an prime value")
    else:
        print("Thank you for entering a prime value")

def primefactors(value):
    """
    >>> value = 15 
    >>> primefactors(value)
    [3, 5]
    """
    # even number divisible
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

def convert(factors):
    return tuple(factors)

def main():
    doctest.testmod(verbose=True)
    value = 216
    check_for_primality(value)
    primefactors(value)
    factors = primefactors(value)
    print(tuple(factors))



if __name__ == "__main__":
    main()