def paired_bracket(bracket):
    if bracket == '}':
        return '{'
    elif bracket == ']':
        return '['
    elif bracket == ')':
        return '('
    return None

def is_matched(expression):
    stack = []
    for bracket in expression:
        if bracket == '{' or bracket == '[' or bracket == '(':
            stack.append(bracket)
        elif bracket == '}' or bracket == ']' or bracket == ')':
            if len(stack) == 0 or stack.pop() != paired_bracket(bracket):
                return False
    return stack == []

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
