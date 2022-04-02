# params = {'sport': 'hockey', 'game': 2, 'time': 17}
def build_query_string(params):
    res = list()
    for k, v in params.items():
    	s = str(k) + '=' + str(v)
    	res.append(s)
    return '&'.join(sorted(res))
# print(build_query_string(params))