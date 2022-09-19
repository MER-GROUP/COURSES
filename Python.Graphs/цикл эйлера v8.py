# put your python code here
from collections import deque

n, ee = map(int, input().split())
e = [[] for m in range(n + 1)]

for i in range(ee):
    v1, v2 = map(int, input().split())
    e[v1].append(v2)
    e[v2].append(v1)
len_e = [len(e[i]) for i in range(n + 1)]
len_e.pop(0)
visited = [False] * (n + 1)
visited[0] = True
#print('e', e)
#print('len_e', len_e)
counter =0
stack = deque()
stack.append(1)
result = False
answer = []

def cycle():
    if n<3 or ee<=0:
        print('NONE')
        return 'NONE'
    for k in len_e:
        if k % 2 != 0:
            
            print('NONE')           
            return 'NONE'

    while len(stack) != 0:

        if len(e[stack[-1]]) != 0:

            v1 = stack[-1]
            s1 = e[stack[-1]][0]
            stack.append(s1)
            e[v1].remove(s1)
            e[s1].remove(v1)
            visited[v1] = True
            visited[s1] = True
        else:
            answer.append(stack.pop())
    answer.reverse()

    if not all(visited):
            print ('NONE')
            return 'NONE'
    for i in range(len(answer)-1):
        if not all(visited):
            break
        print(answer[i], end=' ')

cycle()