def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        # underflow
        return
    else:
        return s.pop(-1)


s = []

# s = ['a']
push('a')
print(s)

# s = ['a', 'b']
push('b')
print(s)

# s = ['a', 'b', 'c']
push('c')
print(s)

# s = ['a', 'b']
pop()
print(s)

# s = ['a']
pop()
print(s)

# s= []
pop()
print(s)

# None
print(pop())
