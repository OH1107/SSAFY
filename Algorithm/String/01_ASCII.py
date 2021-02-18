arr = [1, 2, 3]
print(arr[1])

arr[1] = 4
print(arr)

#####

str1 = '123'
print(str1[1])

# TypeError
# str1[1] = '4'

#####

line = '안녕하세요'
print(line.replace('세', '시')) # 내부 수정이 이뤄지는 것이 아님
print(line)

#####

line2 = 'a12bc'

flag_alpha = False
flag_number = False
for i in line2:
    if i.isalpha():
        flag_alpha = True

    if i.isdigit():
        flag_number = True

if not flag_alpha:
    print('비밀번호에 알파벳이 사용되지 않았음')
elif not flag_number:
    print('비밀번호에 숫자가 사용되지 않았음')
else:
    print('완벽한 비밀번호임')

#####

line2 = '안녕하시요'
print(line2.find("녕")) # 없으면 -1을 반환
print(line2.index("녕")) # 없으면 에러를 반환