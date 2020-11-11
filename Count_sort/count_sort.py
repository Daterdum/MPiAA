import timeit
from utils import random_ints


def count_sort(lst, min, max):
    """
    Puts number of occurrences of element in lst into counts[element + abs(min)]
    indexes of elements move right by abs(min) so it could be possible to access negative elements by their index.
    """
    min = abs(min)
    counts = [0] * (max + min + 1)
    output_lst = []
    for num in lst:
        counts[num + min] += 1
    counter = 0
    for num in counts:
        a = 1
        while a <= num:
            output_lst.append(counter - min)
            a += 1
        counter += 1
    return output_lst


def count_sort_dict(lst, min, max):
    """
    Same logic as count_sort but counts is dict type
    """
    counts = {i: 0 for i in range(min, max+1)}
    output_lst = []
    for num in lst:
        counts[num] += 1
    for num, value in counts.items():
        a = 1
        while a <= value:
            output_lst.append(num)
            a += 1
    return output_lst


def test_lst():
    return random_ints(10 ** 1 * 1)  # change number of elements in list to sort, applies to all tested functions


def main():
    a = timeit.Timer(stmt="count_sort(test_lst(), 0, int(1e6))", setup="from __main__ import count_sort, test_lst")
    b = timeit.Timer(stmt="sorted(test_lst())", setup="from __main__ import test_lst")
    c = timeit.Timer(stmt="count_sort_dict(test_lst(), 0, int(1e6))", setup="from __main__ import count_sort_dict, test_lst")
    print(a.timeit(1))
    print(b.timeit(1))
    print(c.timeit(1))


if __name__ == "__main__":
    main()
