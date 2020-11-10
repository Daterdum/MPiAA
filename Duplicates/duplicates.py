import timeit


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


lst_1 = [1] * 10 ** 2


def main():
    t_1 = timeit.Timer("has_duplicates(lst=lst_1)", "from __main__ import has_duplicates, lst_1")
    t_2 = timeit.Timer("get_duplicates(lst=lst_1)", "from __main__ import get_duplicates, lst_1")
    print(t_1.timeit(100000))
    print(t_2.timeit(100000))


if __name__ == "__main__":
    main()
