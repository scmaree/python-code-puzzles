import math
from itertools import chain, combinations


def n_th_lexicographic_permutation(ordinals: list, r: int = 1) -> list:
    """returns the n_th permutation of ordinals when using lexicographic ordering
    0 < r < n! is 1-based, ordinals a list of the things you want sorted.
    example: r=3, ordinals = [0, 1, 2] -> [1, 0, 2].
    """
    ords = ordinals.copy()
    sorted(ords)
    r -= 1  # make it 0-based
    res = []
    while (n := len(ords)) > 0:
        i = r // (m := math.factorial(n - 1))
        res += [ords[i]]
        r -= i * m
        del ords[i]
    return res


def powerset(s: list):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
    """
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def non_empty_powersets(s: list):
    """powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3), (1, 2, 3, 4)
    https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
    """
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))


def powersubsets(s: list):
    """powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
    """
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))
