params = {'sport': 'hockey', 'game': 2, 'time': 17}

def build_query_string(params):
    res = [f'{k}={v}' for k, v in params.items()]
    return '&'.join(sorted(res))
    
print(build_query_string(params))