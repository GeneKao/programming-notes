# create list with values from 0 to 9
a = [i for i in range(10)]
print(a)
# create list with 10 zeros
a = [0 for i in range(10)]
print(a)

# List slicing
b = [1, 2, 3, 4]
b[1:] = [2, 3, 4]
b[:2] = [1, 2]
b[:-1] = [1, 2, 3]
b[1:-1] = [2, 3]
print(b)

#List manipulation
c = [1, 2, 3]
[str(x) for x in c]  # Output: ['1','2','3']
map(lambda x: str(x), c)  # Output: ['1','2','3']
[str(x) for x in c if x % 2]  # Output: ['1','3']
print(c)

# List as queue
d = [1, 2, 3]
d.append(4)  # push 4 into a queue
d.pop(0)  # queue.pop()
d[0]  # queue.peek()
print(d)

# List as stack
e = [1, 2, 3]
e.append(4)  # push 4 into stack
e.pop()  # stack.pop()
e[-1]  # stack.peek()
print(e)
