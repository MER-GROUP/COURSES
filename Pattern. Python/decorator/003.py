'''
Это простое упражнение на использование функции как аргумента.

Если вы не использовали раньше сортировку по заданному ключу при 
помощи встроенной функции sorted, рекомендую прочитать вот 
этот python-howto (https://docs.python.org/3/howto/sorting.html) 
(упражнение про это, да и вообще возможность чрезвычайно полезная).

На вход подаётся некоторое количество (не больше сотни) разделённых 
пробелом целых чисел (каждое не меньше 0 и не больше 19).

Выведите их через пробел в порядке лексикографического возрастания 
названий этих чисел в английском языке.

Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, 
поскольку слово two в словаре встречается позже слова three, 
а слово three -- позже слова one (иначе говоря, поскольку 
выражение 'one' < 'three' < 'two' является истинным)

number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 
        12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 
        16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}

Sample Input:
0 1 1 2 3 5 8 13
Sample Output:
8 5 1 1 13 3 2 0
'''
number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 
        12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 
        16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}

if __name__ == '__main__':
    print(
        *sorted(
            map(int, input().split()),
            key=lambda x: number_names[x]
        )
    )