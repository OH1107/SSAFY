def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        # underflow
        return
    else:
        return s.pop(-1)

def paren_stack(word):
    
    for i in range(len(word)):
        if word[i] == '(':
            push(word[i])
        else:
            pop()

    if len(s) != 0:
        return 'X'
    else:
        return 'O'

s = []

paren_1 = '()()((()))'
paren_2 = '((()((((()()((()())((())))))'

print(paren_stack(paren_1)) # => O
print(paren_stack(paren_2)) # => X
print('-' * 10)
# ----------

# 대괄호 중괄호 추가

def extend_paren_stack(word):

    for i in range(len(word)):
        if word[i] == '(' or word[i] == '{' or word[i] == '[':
            push(word[i])
        elif word[i] == ')' and s[-1] == '(':
            pop()
        elif word[i] == '}' and s[-1] == '{':
            pop()
        elif word[i] == ']' and s[-1] == '[':
            pop()
        else:
            return 'X'

    if len(s) != 0:
        return 'X'
    else:
        return 'O'

s = []

paren_3 = '[{()}]'
paren_4 = '{](}[)'
paren_5 = '[{(()}]'

print(extend_paren_stack(paren_3)) # => O
print(extend_paren_stack(paren_4)) # => X
print(extend_paren_stack(paren_5)) # => X