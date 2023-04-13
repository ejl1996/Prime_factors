from unittest import TestCase
from prime_factors import check_for_primality


class TestPrimeFactors(TestCase):
    def test_value_error(self):
        with self.assertRaises(ValueError):
            value = 3.5
            check_for_primality(value)

