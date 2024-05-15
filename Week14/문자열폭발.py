x = list(input())
M =list(input())
m = len(M)
stack = []
for i in x:
    stack.append(i)
    if stack[len(stack)-m:len(stack)] == M: 
        for _ in range(m): 
            stack.pop() 
if stack:
    print(''.join(stack))
else:
    print("FRULA")
