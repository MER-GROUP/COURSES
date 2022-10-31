# авторское решение
string = input()
stack = []
result = ''
count_str = ''
a = 0
for i in range(len(string)):
    if string[i].isdigit():
        a = a * 10 + int(string[i])
        if string[i+1] == '(':
            if len(stack) >= 1 and type(stack[-1]) == str:
                stack[-1] += count_str
            else:
                stack.append(count_str)
            count_str = ''
    else:
        if string[i] == '(':
            stack.append(a)
        elif string[i] == ')':
            if type(stack[-1]) == int:
                stack[-2] = stack[-2] + count_str * stack[-1]
                stack.pop()
            else:
                stack[-3] = stack[-3] + (stack[-1] + count_str) * stack[-2]
                stack.pop()
                stack.pop()
            count_str = ''
        else:
            count_str += string[i]
        a = 0
if (len(stack) == 0):
    print(count_str)
else:
    print(stack[-1] + count_str)