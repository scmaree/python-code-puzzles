def reciprocal_decimal_representation(d: int) -> tuple:
    """Give the decimal representation of 1 / d
    Examples:
        1/7 = ([], [1, 4, 2, 8, 5, 7])
        1/6 = ([1], [6])
    """
    assert d > 1
    residuals = []
    representation = []
    r = 1
    while r not in residuals:
        residuals.append(r)
        r *= 10
        m = 0
        while r < d:
            r *= 10
            representation += [0]
        while r >= d:
            r -= d
            m += 1
        representation += [m]
        if r == 0:
            residuals.append(r)
            break
    period = residuals.index(r)
    return representation[:period], representation[period:]


def continued_fraction_to_fraction(seq):
    """Convert the simple continued fraction in `seq` into a fraction, num / den
    https://stackoverflow.com/questions/36077810/continued-fractions-python
    """
    n, d, num, den = 0, 1, 1, 0
    for u in seq:
        n, d, num, den = num, den, num * u + n, den * u + d
    return num, den
