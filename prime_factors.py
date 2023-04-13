import math

# A function to print all prime factors of
# a given number n
def primeFactors(num):

    # Print the number of two's that divide n
    while num % 2 == 0:
        print 2,
        num = num / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(num))+1,2):

        # while i divides n , print i and divide n
        while num % i== 0:
            print i,
            num = num / i

    # Condition if n is a prime
    # number greater than 2
    if num > 2:
        print num

# Driver Program to test above function

n = 315
primeFactors(n)