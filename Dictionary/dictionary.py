class Dictionary:

    def __init__(self, num_of_buckets=1000):
        self.num_of_buckets = num_of_buckets
        self.vector = [None] * self.num_of_buckets

    def __del__(self):
        pass

    def hash_key(self, key):  # can be extended for custom hash function
        return abs(int(hash(key)//1e7))

    def set(self, key, value):
        if self.vector[self.hash_key(key=key)] is None:
            self.vector[self.hash_key(key=key)] = [key, value]
        else:
            if self.vector[self.hash_key(key=key)][0] == key:
                self.vector[self.hash_key(key=key)][1] = value
            else:
                self.vector[self.hash_key(key=key)].append([key, value])

    def get(self, key):
        return self.vector[self.hash_key(key=key)][1]

    def size(self):
        counter = 0
        for element in self.vector:
            if element is not None:
                counter += 1
        return counter


def main():
    dictionary = Dictionary()
    for i in range(10000):
        dictionary.set(int(i), str(i))
    dictionary.set("123", "qwe")
    dictionary.set("123", "qwerty")
    for element in dictionary.vector:
        print(type(element))
        # if element is not None:
            # print("element = ", element[1], "index = ", element[0])
            # print("element = ", element, "index = ", dictionary.vector.index(element))


if __name__ == "__main__":
    main()
""""""