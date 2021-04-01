input = "abcba"


def is_palindrome(string):
    first = 0
    last = len(string) - 1
    if string[first] == string[last]:
        while first is not last:
            first += 1
            last -= 1
    return True


print(is_palindrome(input))