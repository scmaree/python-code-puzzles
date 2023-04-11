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


def prime_gen() -> int:
    """Generator for prime numbers
    Naive FAST approach, adapted from dawg at: https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
    """
    for p in (2, 3, 5):
        yield p

    while True:
        p += 5
        if is_prime(p):
            yield p
        p += 2
        if is_prime(p):
            yield p
