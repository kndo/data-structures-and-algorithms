"""
[1] M. T. Goodrich, R. Tamassia, M. H. Goldwasser.
    Data Structures and Algorithms in Python. New Jersey: John Wiley & Sons, Inc., 2013.
"""

def fibonacci(n):
    """
    >>> list(fibonacci(10))
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    >>> for i in fibonacci(10):
    ...     print(i)
    ...
    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
    """
    a = 0
    b = 1
    for i in range(n):
        yield a
        future = a + b
        a = b
        b = future
