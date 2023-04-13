"""
FUNCTION:
_________

Implement a function called prime_factors that accepts a single parameter,
an integer called value, and returns a tuple of its prime factors in ascending order.

Use functional decomposition by creating helper functions to check for
primality, and to find the smallest prime factor.

DESCRIPTION:
____________

Prime factorization is a way of expressing a number as a product of its prime
factors. A prime number is a number that has exactly two factors, 1 and the
number itself. For example, consider the number 30:

a) We know that 30 = 5 × 6, but 6 is not a prime number
b) The number 6 can further be factorized as 2 × 3, where 2 and 3 are prime numbers
c) Therefore, the prime factorization of 30 = 2 × 3 × 5.

The prime factors of 15 are (3, 5) because 3 and 5 are prime and 3 x 5 = 15.

The prime factors of 56 are (2, 2, 2, 7) because 2 and 7 are prime and
2 x 2 x 2 x 7 = 56.

DOCTESTS:
________

Yes. Use the two matrices in the examples above.

MAIN FUNCTION:
_____________

Yes. In main, deliberately pass an argument to your function so that it raises
an exception, and show me how to avoid a program crash using try-except-else.

UNIT TESTS:
__________

Yes
"""