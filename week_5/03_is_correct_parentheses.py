from collections import deque

balanced_parentheses_string = "()))((()"

def is_correct_parentheses(string):
    stck = []
    for s in string:
        if s == '(':
            stck.append(s)
        else:
            stck.pop()
        return len(stck) == 0

def change_to_correct_parenthesis(string):
    if string == '':
        return ''
    # 문자열 w를 두 균형잡힌 괄호 문자 u,v로 분리
    # 단 u는 '균형잡힌 괄호 문자'로 더 이상 분리할수 없어야 하며,
    # v는 빈 문자열이 될 수 있습니다. 


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        pass
    return 'hi'


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!