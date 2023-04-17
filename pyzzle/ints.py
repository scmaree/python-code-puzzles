from functools import reduce
import math
from typing import Generator

from pyzzle import primes


def is_odd(n: int) -> int:
    """check if int is odd"""
    return n & 1


def is_even(n: int) -> int:
    """check if int is even"""
    return not n & 1


def is_palindrome(n: int) -> bool:
    """check if int is a palindrome (i.e., 9009)"""
    return (s := str(n)) == s[::-1]


def fibonacci_gen(a: int = 0, b: int = 1) -> int:
    """fibonacci generator, starting with a, b = 0, 1"""
    while True:
        a, b = b, (a + b)
        yield a


def is_square(n: int) -> bool:
    """check if int is a square (n = x*x)"""
    return n == math.isqrt(n) ** 2


def triangle_numbers_gen(t: int = 0, n: int = 0) -> int:
    """generator of triangle numbers, starting with t"""
    while True:
        t += (n := n + 1)
        yield t


def triangle_number(n: int) -> int:
    """get the nth triangle number"""
    return n * (n + 1) // 2


def factors(n):
    """all factors of n"""
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if not n % i)))


def proper_divisors(n: int) -> set:
    """all proper divisors of n, e.g., 28 -> {1, 2, 4, 7, 14}"""
    s = set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if not n % i)))
    s.discard(n)
    return s


def is_deficient(n: int) -> bool:
    """A number n is called deficient if the sum of its proper divisors is less than n"""
    return sum(proper_divisors(n)) < n


def is_abundant(n: int) -> bool:
    """A number n is called abundant if the sum of its proper divisors exceeds n"""
    return sum(proper_divisors(n)) > n


def is_perfect(n: int) -> bool:
    return sum(proper_divisors(n)) == n


def is_abundance_lookup() -> list:
    """create lookup table of boolean vector"""
    abundants = [n for n in range(1, 28123 + 1) if is_abundant(n)]
    is_ab = [False] * (max(abundants) + 1)
    for a in abundants:
        is_ab[a] = True
    return is_ab


def is_sum_of_two_abundant_numbers(n: int, is_ab: list) -> bool:
    """Check if a number is the sum of two abundant numbers, using a lookup table is_ab from is_abundance_lookup()"""
    hit = False
    for i, a in enumerate(is_ab[:n]):
        if is_ab[i] and ((m := n - i) > 0 and is_ab[m]):
            hit = True
            break
    return hit


def digits(n: int) -> list:
    """return list of digits of number"""
    return [int(c) for c in str(n)]


def from_digits(d: list) -> int:
    """construct int from list of digits"""
    return int("".join([str(i) for i in d]))


def num_digits(n: int) -> int:
    """number of digits of an int"""
    return len(str(n))


def is_pandigital(n: int, start=1) -> bool:
    """number contains all digits start, start + 1, start + 2, .. up to its len"""
    return all(i in digits(n) for i in range(start, start + num_digits(n)))


def is_1_to_9_pandigital(n):
    """check if a number of len 9 contains all digits 1-9"""
    if num_digits(n) != 9:
        return False
    return is_pandigital(n)


def is_0_to_9_pandigital(n):
    """check if a number of len 10 contains all digits 0-9"""
    if num_digits(n) != 10:
        return False
    return is_pandigital(n, 0)


def concatenated_product(n: int, p: list) -> int:
    """multiply an int with a list of ints and contactenate the product.
    E.g., 12 times [1, 2, 3] = 122436"""
    return int("".join([str(n * i) for i in p]))


def write_number(n: int) -> str:
    """write a number in text"""
    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
    ]
    tens = [None, "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "onehundred"]
    s = ""

    something = False
    if n >= 1000:
        s += "one thousand"
        n -= 1000  # assuming the max number is 1000.
        something = True
    if n >= 100:
        s += words[int(str(n)[0])]
        s += " hundred"
        n = int(str(n)[1:])
        something = True

    #  something hundred - and - something
    if something and n > 0:
        s += " and"
    if n >= 20:
        s += " " + tens[int(str(n)[0])]
        n = int(str(n)[1:])
    if n > 0:
        s += " " + words[n]
    return s


def pentagonal_numbers_gen(n=1):
    """Pentagonal number generator"""
    while True:
        yield n * (3 * n - 1) // 2
        n += 1


def is_pentagonal(n):
    """check if n is a pentagonal numer"""
    return not (math.sqrt(24 * n + 1) + 1) % 6


def hexagonal_numbers_gen(n=1):
    """Hexagonal number generator"""
    while True:
        yield n * (2 * n - 1)
        n += 1


def all_ints_digit_gen(n=0):
    """Generator for the digits of 1, 2, 3, ..., 1, 0, 1, 1, 1, 2, 1, 3, ..."""
    d = digits(n)
    while len(d) > 0:
        yield d[0]
        d = d[1:]
        if len(d) == 0:
            n += 1
            d = digits(n)


def concatenate(*ints) -> int:
    """Concatenate ints as a single number"""
    return int("".join(str(i) for i in ints))


def is_squarefree(n: int) -> bool:
    """A positive integer n is called square-free, if no square of a prime divides n"""
    for p in range(2, 1 + int(n**0.5)):
        c = 0
        while n % p == 0:
            n, c = n // p, c + 1
            if c == 2:
                return False
    return True


def squarefree_numbers_below_n(n: int) -> Generator[int, None, None]:
    for i in range(1, n):
        if is_squarefree(i):
            yield i


def count_squarefree_numbers_below_n(n: int) -> int:
    return len(list(squarefree_numbers_below_n(n)))


def fast_count_squarefree_numbers_below_n(n):
    """
    Counts the ints below that are squarefree numbers
    https://leetcode.com/problems/count-primes/solutions/1722436/python-2-meissel-lehmer-algorithm-28-ms-164-mb/
    """
    if n in [0, 1, 2]:
        return 0

    squared_primes = [p**2 for p in primes.primes_below_n(int(n**0.5))]
    phi_cache = {}
    pi_cache = {}

    return primes.pi(n - 1, squared_primes, pi_cache, phi_cache)


def reverse_and_sum(n):
    """e.g. 32 -> 32 + 23 = 55"""
    return n + int(str(n)[::-1])


def is_lychrel(n, i=0, max_itt=50):
    """ints that do not become palindrome with the reverse_and_sum_approach"""
    while i <= max_itt:
        i, n = i + 1, reverse_and_sum(n)
        if is_palindrome(n):
            return False
    return True
