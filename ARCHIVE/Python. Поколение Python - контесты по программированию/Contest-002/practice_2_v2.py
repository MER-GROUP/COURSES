# авторское решение
def key_difference(dict1, dict2):
    result = dict()
    for key in dict1:
        if key not in dict2:
            result[key] = 'deleted'
        else:
            if dict1[key] != dict2[key]:
                result[key] = 'changed'
            else:
                result[key] = 'equal'
    for key in dict2:
        if key not in dict1:
            result[key] = 'added'
    return result

def key_difference2(dict1, dict2):
    s=list({**dict1, **dict2}.keys())
    dict3={}
    for i in s:
        if dict1.get(i)==None:
            dict3[i]='added'
        elif dict2.get(i)==None:
            dict3[i]='deleted'  
        else:
            dict3[i]=['changed','equal'][dict1.get(i)==dict2.get(i)]
            
    return dict3  

def key_difference3(dict1, dict2):
  d={}
  for i in dict1:
      if i in dict2:
        d[i]=('changed','equal')[dict2[i]==dict1[i]]
      else:
        d[i]=dict2.get(i,'deleted')
  for i in dict2:
    if i not in d:
      d[i]='added'
  return d

dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
dict2 = {'two': 'own', 'zero': '4', 'four': 'True'}
# dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
# dict2 = {}
result = key_difference(dict1, dict2)
print(result)