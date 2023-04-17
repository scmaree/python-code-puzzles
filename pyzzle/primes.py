from bisect import bisect
import math

from pyzzle import ints


def factorization(n: int) -> list:
    """Naive prime factorization, 220 -> [2, 2, 5, 11]"""
    fs = []
    for p in range(2, 1 + int(n**0.5)):
        while n % p == 0:
            fs += [p]
            n //= p
    if n > 1:
        fs += [n]
    return fs


def prime_factor_count_dict(f: list) -> dict:
    """get dict with counts of values in list [2, 2, 3] -> {2: 2, 3: 1}"""
    return {n: sum(i == n for i in f) for n in set(f)}


def primes_below_n(n: int) -> list:
    """sieve of Eros... to find all primes below n"""
    q = [2]
    s = [True] * n
    for i in range(3, 1 + int(n**0.5), 2):
        if s[i]:
            s[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    q += [i for i in range(3, n, 2) if s[i]]
    return q


def is_prime(n: int) -> bool:
    """is n a prime number?
    Naive FAST approach, adapted from dawg at: https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
    """
    if n in (2, 3, 5):
        return True
    if n < 2 or not n & 1 or not n % 3:
        return False
    for f in range(5, 1 + int(n**0.5), 6):
        if not n % f or not n % (f + 2):
            return False
    return True


def is_circular_prime(n: int) -> bool:
    """A number is called a circular prime  when all rotations of the digits are primes themselves."""
    if not is_prime(n):
        return False
    d = ints.digits(n)
    hit = True
    for i in range(len(d) - 1):
        d = d[1:] + d[:1]
        if not is_prime(ints.from_digits(d)):
            hit = False
            break
    return hit


def is_truncatable_prime(n: int) -> bool:
    """n is a truncatable prime if its prime and by iteratively removing digits from left or right, its still prime.
    Naive implementation. Could be improved by noting that only numbers with odd digits can suffice.
    """
    if n <= 7 or not is_prime(n):
        return False
    digits = ints.digits(n)
    while len(digits) > 1:
        digits = digits[:-1]
        if not is_prime(ints.from_digits(digits)):
            return False
    digits = ints.digits(n)
    while len(digits) > 1:
        digits = digits[1:]
        if not is_prime(ints.from_digits(digits)):
            return False
    return True


def prime_gen(limit=None) -> int:
    """Generator for prime numbers
    Naive fast approach, adapted from dawg at: https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
    """
    for n in (2, 3):
        yield n
    while limit is None or n <= limit:
        # all primes > 3 are of the form 6n ± 1
        n += 2
        if is_prime(n):
            yield n


def phi(x, a, primes, phi_cache):
    """
    Implementation of the partial sieve function, which
    counts the number of integers <= x with no prime factor less
    than or equal to the ath prime.
    """
    # If value is cached, just return it
    if (x, a) in phi_cache:
        return phi_cache[(x, a)]

    # Base case: phi(x, a) is the number of odd integers <= x
    if a == 1:
        return math.ceil(x / 2)

    result = phi(x, a - 1, primes, phi_cache) - phi(x / primes[a - 1], a - 1, primes, phi_cache)
    phi_cache[(x, a)] = result  # Memoize
    return result


def pi(x, primes, prime_limit, pi_cache, phi_cache):
    """
    Computes pi(x), the number of primes <= x, using
    the Meissel-Lehmer algorithm.
    """
    # If value is cached, return it
    if x in pi_cache:
        return pi_cache[x]

    # If x < limit, calculate pi(x) using a bisection
    # algorithm over the sieved primes.
    if x < prime_limit:
        result = bisect(primes, x)
        pi_cache[x] = result
        return result

    a = pi(int(x ** (1.0 / 4)), primes, prime_limit, pi_cache, phi_cache)
    b = pi(int(x ** (1.0 / 2)), primes, prime_limit, pi_cache, phi_cache)
    c = pi(int(x ** (1.0 / 3)), primes, prime_limit, pi_cache, phi_cache)

    # This quantity must be integral,
    # so we can just use integer division.
    result = phi(x, a, primes, phi_cache) + (b + a - 2) * (b - a + 1) // 2

    for i in range(a + 1, b + 1):
        w = x // primes[i - 1]
        b_i = pi(w**0.5, primes, prime_limit, pi_cache, phi_cache)
        result = result - pi(w, primes, prime_limit, pi_cache, phi_cache)
        if i <= c:
            for j in range(i, b_i + 1):
                result = result - pi(w // primes[j - 1], primes, prime_limit, pi_cache, phi_cache) + j - 1
    pi_cache[x] = result
    return result


def count_primes_below_n(n):
    """
    Prime counting algorithm: number of primes below n
    https://leetcode.com/problems/count-primes/solutions/1722436/python-2-meissel-lehmer-algorithm-28-ms-164-mb/
    """
    if n in [0, 1, 2]:
        return 0

    prime_limit = 100
    primes = primes_below_n(prime_limit)
    phi_cache = {}
    pi_cache = {}

    return pi(n - 1, primes, prime_limit, pi_cache, phi_cache)
