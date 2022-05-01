def key_difference(dict1, dict2):
    list1 = list(dict1.keys())
    list2 = list(dict2.keys())
    res = dict()
    for key in list1:
        if key in list2 and dict1[key] == dict2[key]:
            res[key] = 'equal'
        elif key not in list2:
            res[key] = 'deleted'
        elif key in list2 and not dict1[key] == dict2[key]:
            res[key] = 'changed'
    added = list(set(list2) - set(list1))
    for key in added:
        res[key] = 'added'

    return res

dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
dict2 = {'two': 'own', 'zero': '4', 'four': 'True'}
# dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
# dict2 = {}
result = key_difference(dict1, dict2)
print(result)