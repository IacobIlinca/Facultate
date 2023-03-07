def odd_numbers_in_list(lst):
    if len(lst) == 0:
        return False
    if len(lst) == 1:
        if lst[0] % 2 == 1:
            return True
        else:
            return False
    return (lst[0] % 2 == 1) or odd_numbers_in_list(lst[1:])


def odd_numbers_in_list2(lst):
    if len(lst) == 0:
        return False
    if len(lst) == 1:
        if lst[0] % 2 == 1:
            return True
        else:
            return False
    middle = len(lst) // 2
    return odd_numbers_in_list2(lst[:middle]) or odd_numbers_in_list(lst[middle:])


def test_odd_numbers_in_list2():
    l3 = [1, 4, 4, 5, 5, 5, 10, 3, 4, 5, 10, 100]
    l2 = [2, 4, 6, 8]
    l1 = []
    l4 = [15]
    l5 = [1, 3, 5]
    l6 = [2]
    l7 = [1, 1, 1, 1]
    l8 = [22,21]

    assert (odd_numbers_in_list2(l1) == False)
    assert (odd_numbers_in_list2(l2) == False)
    assert (odd_numbers_in_list2(l3) == True)
    assert (odd_numbers_in_list2(l4) == True)
    assert (odd_numbers_in_list2(l5) == True)
    assert (odd_numbers_in_list2(l6) == False)
    assert (odd_numbers_in_list2(l7) == True)
    assert (odd_numbers_in_list2(l8) == True)


def test_odd_numbers_in_list1():
    l3 = [1, 4, 4, 5, 5, 5, 10, 3, 4, 5, 10, 100]
    l2 = [2, 4, 6, 8]
    l1 = []
    l4 = [15]
    l5 = [1, 3, 5]
    l6 = [2]
    l7 = [1, 1, 1, 1]
    l8 = [22,21]

    assert (odd_numbers_in_list(l1) == False)
    assert (odd_numbers_in_list(l2) == False)
    assert (odd_numbers_in_list(l3) == True)
    assert (odd_numbers_in_list(l4) == True)
    assert (odd_numbers_in_list(l5) == True)
    assert (odd_numbers_in_list(l6) == False)
    assert (odd_numbers_in_list(l7) == True)
    assert (odd_numbers_in_list(l8) == True)

