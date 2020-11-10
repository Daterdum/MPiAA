from datetime import datetime
from utils import random_ints


def add_list(list_to_add, *elements):
    for element in elements:
        list_to_add.append(element)
    return list_to_add


def add_list_beginning(list_to_add, *elements):
    for element in elements:
        list_to_add.insert(0, element)
    return list_to_add


def find_list(list_to_find, element):
    if element in list_to_find:
        return True
    else:
        return False


def add_set(set_to_add, *elements):
    for element in elements:
        set_to_add.add(element)
    return set_to_add


def add_set_beginning(set_to_add, *elements):
    for element in elements:
        set({element}).update(set_to_add)
    return set_to_add


def find_set(set_to_find, element):
    if element in set_to_find:
        return True
    else:
        return False


def main():
    num_to_put = 10 ** 5 * 10  # number to use in range functions
    num_to_find = 10 ** 3 * 1
    ex_list = list()
    ex_list_b = list()
    ex_set = set()
    ex_set_b = set()
    num_to_find = random_ints(num_to_find)

    # List functions
    # list.add
    lst_start = datetime.now()
    for number in range(num_to_put):
        add_list(ex_list, number)
    lst_end = datetime.now()
    print("add lst time = ", lst_end - lst_start)

    # list.find
    lst_start = datetime.now()
    for number in num_to_find:
        find_list(ex_list, number)
    lst_end = datetime.now()
    print("find lst time = ", lst_end - lst_start)

    # list.add_beginning
    lst_start = datetime.now()
    for number in range(num_to_put):
        add_list_beginning(ex_list_b, number)
    lst_end = datetime.now()
    print("add_b lst time = ", lst_end - lst_start)

    # Set functions
    # set.add
    set_start = datetime.now()
    for number in range(num_to_put):
        add_set(ex_set, number)
    set_end = datetime.now()
    print("add set time = ", set_end - set_start)

    # set.find
    set_start = datetime.now()
    for number in num_to_find:
        find_set(ex_set, number)
    set_end = datetime.now()
    print("find set time = ", set_end - set_start)

    # set.add_beginning
    set_start = datetime.now()
    for number in range(num_to_put):
        add_set_beginning(ex_set_b, number)
    set_end = datetime.now()
    print("add_b set time = ", set_end - set_start)


if __name__ == '__main__':
    main()
