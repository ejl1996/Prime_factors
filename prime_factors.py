
#import doctest

def primefactors(value):
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
    #doctest.testmod(verbose=True)
    #try:
        #value = int(input('Enter a number : '))
    #except(ValueError):
        #print('Please enter an integer !')
    #else:
        #print("Thank you for entering an integer")

    value = 216
    factors = primefactors(value)
    print(tuple(factors))



if __name__ == "__main__":
    main()