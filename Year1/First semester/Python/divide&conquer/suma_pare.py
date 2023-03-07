def suma_pare(lst):

    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        if lst[0] % 2 == 0:
            return lst[0]
        else:
            return 0
    middle = len(lst) // 2

    suma_left = suma_pare(lst[:middle])
    suma_right = suma_pare(lst[middle:])

    return suma_left + suma_right


def test_suma_pare():
    l1 = [1, 4, 4, 5, 8]
    l2 = [2, 4, 6, 8]
    l3 = []
    l4 = [5]
    l5 = [1, 3, 5]
    l6 = [2]
    l7 = [2, 3, 4, 8, 10, 4, 90]
    l8 = [22, 21, 19, 10]
    l9 = [1, 4, 4, 5]
    l10 = [0, 0, 1, 2, 3]

    assert (suma_pare(l1) == 16)
    assert (suma_pare(l2) == 20)
    assert (suma_pare(l3) == 0)
    assert (suma_pare(l4) == 0)
    assert (suma_pare(l5) == 0)
    assert (suma_pare(l6) == 2)
    assert (suma_pare(l7) == 118)
    assert (suma_pare(l8) == 32)
    assert (suma_pare(l9) == 8)
    assert (suma_pare(l10) == 2)
