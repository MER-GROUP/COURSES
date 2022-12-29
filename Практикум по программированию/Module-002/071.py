'''
Нули

Входные данные
Вводится число N, а затем N чисел.

Выходные данные
Подсчитайте и выведите, сколько среди данных N чисел нулей.

Sample Input:
3
1
2
3
Sample Output:
0
'''
# print(
#     len(
#         list(
#             filter(
#                 lambda x: 0 == x, 
#                 [int(input()) for _ in range(int(input()))]
#             )
#         )
#     )
# )

print(
    sum(
        map(
            lambda x: 0 == x, 
            [int(input()) for _ in range(int(input()))]
        )
    )
)