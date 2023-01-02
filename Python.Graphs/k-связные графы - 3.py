'''
Докажите, что k-мерный гиперкуб k-связен с помощью теоремы Менгера.

k-мерным гиперкубом называется граф, в котором вершины — битовые 
строки длины k, а рёбра проведены между теми парами вершин, 
которые отличаются ровно в одном бите. На вход подаётся две 
различные битовых строки A и B длины k<100 через пробел. 
Выведите k простых путей в k-мерном гиперкубе из A в B, 
не пересекающихся по внутренним вершинам. Формат вывода: 
один путь на строку; путь – последовательности битовых строк, 
разделённая пробелами.

Sample Input 1:
1010 0010
Sample Output 1:
1010 0010
1010 1011 0011 0010
1010 1000 0000 0010
1010 1110 0110 0010

Sample Input 2:
0 1
Sample Output 2:
0 1
'''
###############################################################################

def print_list(list_):
    print(''.join(str(_) for _ in list_), end=' ')


def print_paths(source_string, target_string):
    source_li = [int(x) for x in source_string]
    target_li = [int(x) for x in target_string]
    sim = [i for i in range(len(source_li)) if source_li[i] == target_li[i]]
    diff = [i for i in range(len(source_li)) if source_li[i] != target_li[i]]
    for j in range(len(diff)):
        path = diff[j:] + diff[:j]
        cur = source_li[:]
        print_list(cur)
        for u in path:
            cur[u] = 1 - cur[u]
            print_list(cur)
        print()
    for v in sim:
        cur = source_li[:]
        print_list(cur)
        cur[v] = 1 - cur[v]
        print_list(cur)
        for u in diff:
            cur[u] = 1 - cur[u]
            print_list(cur)
        cur[v] = 1 - cur[v]
        print_list(cur)
        print()


if __name__ == '__main__':
    source_, target_ = input().split(' ')
    print_paths(source_, target_)

###############################################################################

def next_v(i, t):
    p[i].append(t)
    s.add(p[i][-1])
    find_p(i)


def find_p(i):
    if p[i][-1] == b:
        print(*p[i])
    else:
        for j in range(k-1):
            if p[i][-1][j] != b[j]:
                t = p[i][-1][:j] + b[j] + p[i][-1][j+1:]
                if t not in s or t == b:
                    next_v(i, t)
                    break
        if p[i][-1][k-1] != b[k-1]:
            t = p[i][-1][:k-1] + b[k-1]
            if t not in s or t == b:
                next_v(i, t)
        if p[i][-1] != b:
            for j in range(k-1):
                if p[i][-1][j] == b[j]:
                    t = p[i][-1][:j] + str(int(not(int(b[j])))) + p[i][-1][j+1:]
                    if t not in s:
                        next_v(i, t)
                        break


a, b = input().split()
k = len(a)
p = [[a] for _ in range(k)]
s = {a}
for i in range(k-1):
    p[i].append(a[:i] + str(int(not(int(a[i])))) + a[i+1:])
    s.add(p[i][-1])
p[k-1].append(a[:k-1] + str(int(not(int(a[k-1])))))
s.add(p[k-1][-1])
for i in range(k):
    find_p(i)

###############################################################################

def hyper_routings(x, y):
    
    if x == y: return print(x)
    length = len(x)
    
    for i in range(length):
        routing = list()
        routing, finder = routing + [x], list(x)
        if finder[i] == '1': finder[i] = '0'
        else: finder[i] = '1'
        routing += [''.join(finder)]
        if routing[-1] == y: 
            print(*routing)
            continue 
        for j in range(1, length+1):
            ind = i + j - length
            finder[ind] = y[ind]
            if ''.join(finder) not in routing: routing += [''.join(finder)]
            if routing[-1] == y: 
                print(*routing)
                break 

x, y = input().split(' ')
hyper_routings(x, y)

###############################################################################

"""
Немного другой подход: если вершины противоположны, то можно получить 
k различных непересекающихся путей путём циклического сдвига "флипа" 
каждого бита.  Т.е. 1, 2 ... k; 2, 3 ... k, 1; ... k, 1, 2 ... k-1. 
Если k = 1, то различные вершины всегда противоложны.
Теперь воспользуемся индукционным предположением, что k-1 гиперкуб 
k-1 связан. Если вершины не являются противоположными, то значит 
они имеют хотя бы 1 различный бит. Зафиксировав этот бит, получим k-1 
гиперкуб с k-1 путями.
Затем заменим значение этого бита на противоложно, и построим k-й 
путь меняя все биты, кроме того, который поменяли. Этот путь не может 
пересекаться не с одним из k-1предыдущих из-за измененного постоянного бита.
"""
class OppositeVertException(Exception):
    pass

def to_bin(x, k):
    return ('{:0' + str(k) + 'b}').format(x)

def is_opposite(x, y, k):
    return x ^ y

def traverse_opposite_shift(x, k, shift):
    nex = 1 << shift
    node = x
    for i in range(k):
        node = node ^ nex
        yield node
        nex = ((nex << 1) & ~(1 << k)) | ((nex >> (k - 1)) & 1)
        
def traverse_opposite(x, k):
    for i in range(k):
        yield tuple([x] + list(traverse_opposite_shift(x, k, i)))

def find_similar(x, y, k):
    for i in range(k):
        val_x = x & (1 << i)
        val_y = y & (1 << i)
        if val_x == val_y:
            return (i, val_x >> i)
    raise OppositeVertException("Opposite")

def exclude_constraint(x, constr):
    if constr == 0:
        return x >> 1
    return ((x & (~0 << (constr + 1))) >> 1) | (x ^ (x & (~0 << constr)))

def add_constraint(x, constr, val):
    if constr == 0:
        return x << 1 | val
    return (x & (~0 << constr)) << 1 | (val << constr) | (x ^ (x & (~0 << constr)))

def constrained_traverse(x, y, k, constr):
    nex = x
    for i in range(k):
        if i == constr:
            continue
        val_x = x & (1 << i)
        val_y = y & (1 << i)
        if val_x != val_y:
            nex = (nex ^ (1 << i)) | (~val_x & (1 << i))
            yield nex
    
def traverse(x, y, k):
    try:
        constr, constr_val = find_similar(x, y, k)
        # Find k-1 paths from k-1-hypercube
        sub_traverse = traverse(exclude_constraint(x, constr), exclude_constraint(y, constr), k - 1)
        #print([' '.join(map(lambda x: to_bin(x, k - 1), v)) for v in sub_traverse])
        sub_traverse = [tuple(map(lambda v: add_constraint(v, constr, constr_val), path)) for path in sub_traverse]
        # Find k-th path from different sub hypercube
        start = (x ^ (1 << constr)) | ((~constr_val & 1) << constr)
        return sub_traverse + [tuple([x, start] + list(constrained_traverse(start, y, k, constr)) + [y])]
    except OppositeVertException:
        return list(traverse_opposite(x, k))
        
a, b = input().split()
k = len(a)
a = int(a, 2)
b = int(b, 2)
print("\n".join([' '.join(map(lambda x: to_bin(x, k), v)) for v in traverse(a, b, k)]))

###############################################################################

"""
diff - координаты, в которых начальная вершина start не совпадает с конечной end

same - в которых совпадает

сначала формируем len(diff) путей используя циклический сдвиг множества индексов rotate

потом len(same) раз удлиняем последний из тех путей меняя одну 
координату из same в начале и в конце (путь увеличивается на 2)

строки не изменяемы - пришлось возится со списками, списки 
изменяемы - поэтому возня с copy() 
"""
start, end = map(list, input().split())
n = len(start)
neg = {'0': '1', '1': '0'}

same = [i for i in range(n) if start[i] == end[i]]
diff = [i for i in range(n) if start[i] != end[i]]

rotate = diff.copy()
for _ in diff:
    path = [start]
    for i in rotate:
        new = path[-1].copy()
        new[i] = neg[new[i]]
        path.append(new)
    print(*(''.join(p) for p in path))
    rotate = rotate[1:]+[rotate[0]]

for i in same:
    new_path = [start]
    for p in path:
        new_p = p.copy()
        new_p[i] = neg[new_p[i]]
        new_path.append(new_p)
    new_path.append(end)
    print(*(''.join(p) for p in new_path))

###############################################################################

a,b = input().split()
d,swap = [i for i in range(len(a)) if a[i] == b[i]],{'0':'1', '1':'0'}
def change(a,b,t=-1):
    c,d = [],[]
    for i in range(len(a)):
        if a[i] == b[i]: d.append(i)
        else: c.append(i)
    if t==-1:
        for j in range(len(c)):
            p,temp = c,a
            c.append(c.pop(0))
            print(temp, end=' ')
            for i in p:
                temp = temp[:max(0,i)] + swap[temp[i]] + temp[min(i+1,len(temp)):]
                print(temp, end=' ')
            print()
    else:
        c.remove(t),c.append(t)
        temp = a
        print(temp, end=' ')
        for i in c:
            temp = temp[:max(0,i)] + swap[temp[i]] + temp[min(i+1,len(temp)):]
            print(temp, end=' ')
        print()
change(a,b,-1)
for i in d:
    print(a, end=' ')
    temp = a
    temp = temp[:max(0,i)] + swap[temp[i]] + temp[min(i+1,len(temp)):]
    change(temp,b,i)

###############################################################################

def dfs(x):
    path.append(z)
    for step in steps:
        y = x ^ step
        if y == z:
            raise TabError
        if y not in visited:
            steps.remove(step)
            path[-1] = y
            dfs(y)
            steps.add(step)
    del path[-1]

(a, k), (z, k) = ((int(w, 2), len(w)) for w in input().split())
fmt, visited, tmp, s = f'{{:0>{k}b}}'.format, {a}, ([], []), 1
for _ in range(k):
    tmp[not s & (a ^ z)].append(s)
    s *= 2
right, wrong = tmp
for _ in right:
    path, steps = [a], set(right)
    try:
        dfs(a)
    except TabError:
        visited.update(path)
        print(*map(fmt, path))
for t in wrong:
    print(*map(fmt, [a, *[s ^ t for s in path], z]))

###############################################################################