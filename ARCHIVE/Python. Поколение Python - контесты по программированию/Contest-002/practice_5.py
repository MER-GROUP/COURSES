'''
Sample Input 1:

1 3 5 6 10 21 22
r g b w w r g
Sample Output 1:

20
Sample Input 2:

1 2 3 4 5 6 7
green blue b r white dark key
Sample Output 2:

0
Sample Input 3:

2 5 10 11 16 17 18 20
r w g w g r w b
Sample Output 3:

15
'''

class Algo:
    def __init__(self, coord_arr, color_arr) -> None:
        my_dict = dict()
        for key, val in zip(color_arr, coord_arr):
            # my_dict[key] = my_dict.get(key, list()).extend([val])
            my_dict[key] = my_dict.get(key, list()) + [val]
        self.__algo(my_dict)

    def __algo(self, my_dict):
        res_arr = list()
        for key in my_dict.keys():
            if 1 < len(my_dict[key]):
                res_arr.append(max(my_dict[key]) - min(my_dict[key]))
                pass
        print(max(res_arr) if res_arr else 0)

if __name__ == '__main__':
    Algo(list(map(int, input().strip().split())), 
            list(map(str, input().strip().split())))