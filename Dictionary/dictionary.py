class Dictionary:

    def __init__(self, num_of_buckets=1000):
        self.num_of_buckets = num_of_buckets
        self.vector = [None] * self.num_of_buckets
        print(type(self.vector))

    def __del__(self):
        pass

    def hash_key(self, key):  # can be extended for custom hash function
        return abs(int(hash(key)//1e7))

    def set(self, key, value):
        self.vector[self.hash_key(key=key)] = [key, value]
        # check if element with this key already exists,
        # check for collision
        pass

    def get(self, key):
        return self.vector[self.hash_key(key=key)][1]

    def size(self):
        pass


def main():
    print(abs(int(hash(None)//1e7)))
    dictionary = Dictionary()


if __name__ == "__main__":
    main()
