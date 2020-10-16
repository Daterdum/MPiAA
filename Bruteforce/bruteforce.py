def bruteforce(hashed_pass, alphabet, max_length):
    possible_string = []

    def combination(existing_string="", iteration=0):
        if iteration == max_length + 1:
            return 0
        for letter in alphabet:
            existing_string += letter
            possible_string.append(existing_string)
            combination(existing_string, iteration+1)

    return ""


def main():
    print(bruteforce())


if __name__ == "__main__":
    main()
