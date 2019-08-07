import math
import random


def pi():
    """
    Estimating PI's value from N points, a rectangle and a circle
    :param N: number of random points
    :return: a float approximates to PI
    """
    N = 100000
    Nt = 0      #number of random points inside the circle
    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        Nt = Nt + (x*x + y*y <= 1.0)*1

    return 4.0*Nt/N

def e():
    """
    Estimating e's value
    :return: a float approximates to e
    """
    n = 1000
    e = 0
    for i in range(n):
        e = e + 1/math.factorial(i)

    return e
