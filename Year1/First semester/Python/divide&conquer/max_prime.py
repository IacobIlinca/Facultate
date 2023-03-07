import math

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for d in range(2, int(math.sqrt(x)) + 1):
        if x % d == 0:
            return False
    return True


def find_max_prime(lst):
    if len(lst) == 0:
        return -1
    if len(lst) == 1:
        if is_prime(lst[0]):
            return lst[0]
        else:
            return -1
    middle = len(lst) // 2
    return max(find_max_prime(lst[:middle]), find_max_prime(lst[middle:]))


def test_find_max_prime():
    l1 = []
    assert (find_max_prime(l1) == -1)

    l11 = [12, 6, 9]
    assert (find_max_prime(l11) == -1)

    l2 = [1, 2, 1, 4]
    assert (find_max_prime(l2) == 2)

    l3 = [14, 5, 6, 90, 41, 3, 17, 61]
    assert (find_max_prime(l3) == 61)

    l4 = [53, 40, 49, 75, 21, 23, 29]
    assert (find_max_prime(l4) == 53)

    l5 = [103, 1, 2, 4, 5, 49, 59, 18, 101, 19, 23]
    assert (find_max_prime(l5) == 103)
