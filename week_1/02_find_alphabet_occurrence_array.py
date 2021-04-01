def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for s in string:
        if not s.isalpha():
            continue
        alphabet_occurrence_array[ord(s)-ord("a")] += 1
    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))