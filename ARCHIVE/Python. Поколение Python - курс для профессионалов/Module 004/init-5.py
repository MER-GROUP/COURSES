print('------------------')

import pickle

obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}

with open('file.pkl', 'wb') as file:
    pickle.dump(obj, file)

print('------------------')

import pickle

# используется файл полученный на предыдущем шаге
with open('file.pkl', 'rb') as file:     
    obj = pickle.load(file)
    print(obj)
    print(type(obj))

print('------------------')

import pickle

obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
binary_obj = pickle.dumps(obj)

print(binary_obj)
print(type(binary_obj))

print('------------------')

import pickle

obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
binary_obj = pickle.dumps(obj)

new_obj = pickle.loads(binary_obj)

print(new_obj)

print('------------------')

import pickle

obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
binary_obj = pickle.dumps(obj)
new_obj = pickle.loads(binary_obj)

print(obj == new_obj)
# проверка на идентичность
print(obj is new_obj)       

print('------------------')