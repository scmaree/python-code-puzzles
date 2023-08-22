def argmin(seq: list, **kwargs) -> int:
    """index of min element in list-like"""
    return seq.index(min(seq, **kwargs))


def argmax(seq: list, **kwargs) -> int:
    """index of max element in list-like"""
    return seq.index(max(seq, **kwargs))


def argmin_gen(gen) -> int:
    """index of min element of a generator
    Warning: it's actually faster to just call argmin(list(gen)), but this saves memory.
    """
    return min(enumerate(gen), key=lambda x: x[1])[0]


def argmax_gen(gen) -> int:
    """index of max element of a generator
    Warning: it's actually faster to just call argmax(list(gen)), but this saves memory.
    """
    return max(enumerate(gen), key=lambda x: x[1])[0]
