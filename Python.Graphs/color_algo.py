'''
Пусть k есть максимальная из степеней вершин простого связного графа G, 
и пусть этот граф не является k-регулярным. Упорядочим вершины графа 
по невозрастанию степеней этих вершин. Докажите, что при таком упорядочивании 
адный алгоритм всё равно может использовать более k цветов, предъявив описание 
такого графа. Формат — список пар вершин через пробел, где каждая 
пара — описание очередного ребра. Проверяющая система будет подразумевать, 
что вершины графа уже упорядочены и имеют номера от 1 до некоторого n, например:

1 2 2 3 4 1 — граф на четырёх вершинах {1, 2, 3, 4} и трёх рёбрах {1, 2}, {2, 3} и {4, 1}.

Граф не должен содержать более 50 рёбер.
'''
     
G = {1:[4,6,8], 2: [5,7,3], 3: [2,6,8], 4:[5,1,7],
     5:[2,4], 6:[5,3,1], 8:[1,3], 7:[2,4]}


def to_edges(G):
    G1 =G.copy()
    edges = []
    for v in G1:
        for n in G1[v]:
            edges.append((v,n))
            if v in G1[n]:
                G1[n].remove(v)
    return " ".join(map(str,sum(edges,())))
    
COLORS = set(G.keys()) 
def color_it(order):
    def get_neighb_colors(v, dict_colors):
        return {dict_colors[n] for n in G[v] if dict_colors[n]!=None}
    cur_colors = dict.fromkeys(G.keys(), None)
    for v in order:
        cur_colors[v] = min(COLORS - get_neighb_colors(v, cur_colors))
    return set(cur_colors.values())
      
order = list(G.keys())
print(order)
print(color_it(order))
print(to_edges(G))