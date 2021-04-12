# 수식문자열을 읽어서 피연산자는 바로 출력하고 연산자는 스택에 push
# 수식이 끝나면 스택에 남아있는 연산자를 모두 pop하여 출력

# 우선순위가 없는 후위표기법 (연습을 위한 간소한 과정)
text = '2+3*4/5'
s = []
postfix = ''


for i in range(len(text)):                      # 수식 문자열 순회
    if ord('0') <= ord(text[i]) <= ord('9'):    # 숫자를 만날 경우
        postfix += text[i]                      # 바로 출력
    else:
        s.append(text[i])                       # 연산자의 경우 스택에 push

while len(s) > 0:                               # 스택 순회
    postfix += s.pop()                          # 피연산자만 있는 문자열에 연산자를 pop

print('후위표기법 : ', postfix)  # => 2345/*+

# -------------------------------------- #

# 후위 표기법의 수식을 스택을 이용하여 계산

# 피연산자를 만나면 스택에 push
# 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산
# 연산결과를 다시 스택에 push
# 수식이 끝나면, 스택을 pop하여 출력

s = []
op = ''

for i in range(len(postfix)):                       # 후위표기법을 순회
    if ord('0') <= ord(postfix[i]) <= ord('9'):     # 숫자일 경우 스택에 푸쉬
        s.append(postfix[i])
    else:                                           # 연산자일 경우
        num1 = float(s.pop(-2))                     # 스택의 마지막 2개 숫자를 할당
        num2 = float(s.pop(-1))

        if postfix[i] == '+':                       # 연산 기호에 맞는 연산 후
            s.append(num1 + num2)                   # 스택에 다시 추가
            
        elif postfix[i] == '-':
            s.append(num1 - num2)

        elif postfix[i] == '*':
            s.append(num1 * num2)

        elif postfix[i] == '/':
            s.append(num1 / num2)

print('계산 결과 : ', s.pop())

# ---------------------------------- #

# 소괄호, 사칙연산을 포함한 연산 순서가 있는 후위표기법
op_order = {"-": 1, "+": 1, "*": 2, "/": 2, "(": 0}

arr = input()
res = ''
stack = []
for i in range(len(arr)):
    if arr[i] == '(' or arr[i] == ')':
        if arr[i] == '(':
            stack.append(arr[i])
        else:
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()
    elif arr[i].isdigit():
        res += arr[i]
    else:
        if len(stack) > 0:
            while op_order[stack[-1]] >= op_order[arr[i]]:
                res += stack.pop()
                if len(stack) == 0:
                    break
            stack.append(arr[i])
        else:
            stack.append(arr[i])
while len(stack) > 0:
    res += stack.pop()

print(res)