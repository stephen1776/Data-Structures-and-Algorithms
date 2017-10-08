# python3
'''
Input Format. Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation
marks and brackets from the set []{}().

Output Format. If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise,
output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing
brackets, output the 1-based index of the first unmatched opening bracket.
'''

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False



if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i))
        elif next == ')' or next == ']' or next == '}':
            # Process closing bracket
            if len(opening_brackets_stack) == 0:
                opening_brackets_stack.append(Bracket(next, i))
                break
            top = opening_brackets_stack.pop()
            if not top.Match(next):
                opening_brackets_stack.append(Bracket(next, i))
                break
    if len(opening_brackets_stack) == 0:
        print("Success")
    else:
        print(opening_brackets_stack.pop().position + 1)