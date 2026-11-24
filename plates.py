def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 2 to 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # must start with at least two letters
    if not s[:2].isalpha():
        return False

    # no periods, spaces, or punctuation
    if not s.isalnum():
        return False

    # numbers only at the end, and the first number can't be 0
    for i, c in enumerate(s):
        if c.isdigit():
            if c == "0":
                return False
            return s[i:].isdigit()

    return True


main() 