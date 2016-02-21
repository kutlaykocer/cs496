"""
Hellinger Distance calculation python file
"""
import math
from sketch import Sketch

_SQRT2 = math.sqrt(2)     # sqrt(2) with default precision np.float64
"""
def pcalculation(n, i, N):



def q_calculation(m, i, M):
"""
def hit_calculation(p,i,j):
    return math.sqrt(p.get(i,j)/p.get_totalhit(i))


def hellinger1(p, q):

    result=0

    """

    :rtype: float
    """
    for i in range(p.get_rowsize()):
        for j in range(p.get_columnsize()):
           result=result+(hit_calculation(p,i,j)-hit_calculation(q,i,j))


    return result/_SQRT2

def hellinger3(p, q):

    return math.sqrt(math.sum((math.sqrt(p) - math.sqrt(q)) ** 2)) / _SQRT2

