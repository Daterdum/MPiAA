import timeit
from utils import random_ints


def has_duplicates(lst):
    for element in lst:
        if lst.count(element) > 1:
            return True
    return False


def get_duplicates(lst):
    duplicates = []
    for element in lst:
        if element in duplicates:
            continue
        if lst.count(element) > 1:
            lst.remove(element)
            duplicates.append(element)
    return duplicates


def get_duplicates_2(lst):
    lst = sorted(lst)
    duplicates = []
    for index, element in enumerate(lst):
        if element in duplicates:
            continue
        if lst.count(element) > 1:
            lst.remove(element)
            duplicates.append(element)
    return duplicates


def lst_func():
    return random_ints(10 ** 4 * 1)


def main():
    t_1 = timeit.Timer("has_duplicates(lst=lst_func())", "from __main__ import has_duplicates, lst_func")
    t_2 = timeit.Timer("get_duplicates(lst=lst_func())", "from __main__ import get_duplicates, lst_func")
    print("has_duplicates time = ", t_1.timeit(1))
    print("get_duplicates time = ", t_2.timeit(1))


if __name__ == "__main__":
    main()
