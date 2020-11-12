from hashlib import sha256
import timeit


def bruteforce(hashed_pass, alphabet, max_length):
    hashed_pass = hashed_pass.digest()

    def _bruteforce(string):
        temp_string = string
        if sha256(temp_string.encode()).digest() == hashed_pass:
            return temp_string
        for element in alphabet:
            a = None if len(string + element) > max_length else _bruteforce(temp_string + element)
            if a is not None:
                return a
    result = _bruteforce(string="")
    return result if result is not None else ""


def main():
    t = timeit.Timer("bruteforce(sha256('jjjjjj'.encode('utf-8')), 'abcdefghij', 6)", setup="from __main__ import bruteforce; from hashlib import sha256")
    print("Time = ", t.timeit(1))


if __name__ == "__main__":
    main()
