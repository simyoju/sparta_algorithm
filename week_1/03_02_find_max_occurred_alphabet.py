input = "hihihihih"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alph = [0] * 26
    max = 0
    i = 0
    result_i = 0

    for s in string:
        if not s.isalpha():
            continue
        alph[ord(s)-ord("a")] += 1

    for a in alph:
        if max <= a:
            max = a
            result_i = i
        i += 1

    return chr(result_i+ord("a"))


result = find_max_occurred_alphabet(input)
print(result)