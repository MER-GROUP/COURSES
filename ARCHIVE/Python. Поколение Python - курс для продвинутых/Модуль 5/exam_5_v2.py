values = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]

def merge(values):
    dictor = dict()
    for dic in values:
    	for k, v in dic.items():
    		if k not in dictor:
    			dictor[k] = set()
    		dictor[k].add(v)
    return dictor
    
print(merge(values))