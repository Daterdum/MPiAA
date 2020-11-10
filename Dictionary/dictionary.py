from Dictionary.dict_timer import time_me
from timer import time_me as time_def
from utils import random_string, random_ints
from datetime import datetime


def default_hash(key):
    # default hash function for dictionary with 1000 buckets
    return abs(int(hash(key) // 1e7))


class Dictionary:

    def __init__(self, num_of_buckets=1000, hash_func=default_hash):
        self.num_of_buckets = num_of_buckets
        self.vector = [None] * self.num_of_buckets
        self.hash_func = hash_func

    def __del__(self):
        pass

    def hash_key(self, key):
        return self.hash_func(key)

    def set(self, key, value):
        hashed_key = self.hash_key(key=key)
        if hashed_key > self.num_of_buckets:
            while hashed_key > self.num_of_buckets:
                hashed_key //= 10
        if self.vector[hashed_key] is None:
            self.vector[hashed_key] = [[key, value]]
        else:
            if self.vector[hashed_key][0][0] == key:
                self.vector[hashed_key][0][1] = value
            else:
                self.vector[hashed_key].append([key, value])

    def get(self, key):
        hashed_key = self.hash_key(key)
        if hashed_key > self.num_of_buckets:
            hashed_key //= 10
        if self.vector[hashed_key] is None:
            return ""
        if len(self.vector[hashed_key]) > 1:
            for element in self.vector[hashed_key]:
                if element[0] == key:
                    return element[1]
        return self.vector[hashed_key][0][1]

    def size(self):
        counter = 0
        for element in self.vector:
            if element is not None:
                counter += len(element)
        return counter

    def print_dict(self):
        for element in self.vector:
            if element is not None:
                print(element, '\n')


def custom_hash_func(key):
    return len(str(key))**5


def main():

    d = Dictionary(num_of_buckets=100000, hash_func=custom_hash_func)
    start_1 = datetime.now()
    time_me("Set", d.set, ns=[10] * 10 ** 4 * 10, generator=random_ints, repeats=1)
    end_1 = datetime.now()
    print("Time to set - ", end_1 - start_1)
    start = datetime.now()
    time_def("Get", d.get, ns=[10] * 10 ** 2 * 1, generator=random_ints, repeats=1)
    end = datetime.now()
    print("Time to set - ", end_1 - start_1)
    print("Time to get - ", end - start)
    print(d.size())
    # print(len(d.vector[0][0]))


if __name__ == "__main__":
    main()
