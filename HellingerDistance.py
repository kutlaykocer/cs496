"""
Hellinger Distance calculation
"""
import math


_SQRT2 = math.sqrt(2)     # sqrt(2) with default precision np.float64


def hellinger1(p, q):
    """

    :rtype: float
    """
    return (math.sqrt(p) - math.sqrt(q)) / _SQRT2


def hellinger3(p, q):
    return math.sqrt(math.sum((math.sqrt(p) - math.sqrt(q)) ** 2)) / _SQRT2

