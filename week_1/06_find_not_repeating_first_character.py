input = "abacabade"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    alph = [0]*26
    i = 0
    for s in string:
        alph[ord(s)-ord("a")] += 1

    for a in alph:
        if a == 1:
            return chr(i + ord("a"))
        i += 1


result = find_not_repeating_character(input)
print(result)