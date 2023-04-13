'''
Функция get_all_values() 🌶️
Реализуйте функцию get_all_values(), которая принимает два аргумента 
в следующем порядке:

nested_dicts — словарь, содержащий в качестве значений произвольные объекты 
или словари, которые, в свою очередь, так же содержат в качестве значений 
произвольные объекты или словари; вложенность может быть произвольной

key — хешируемый объект

Функция должна определять все значения, которые соответствуют ключу key 
в словаре nested_dicts и всех его вложенных словарях, и возвращать их 
в виде множества. Если ключа key нет ни в одном словаре, функция должна вернуть пустое множество.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию get_all_values(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/594680/tests_2429556.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.4/Module_8.4.7

Sample Input 1:
my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')
print(*sorted(result))
Sample Output 1:
4 5

Sample Input 2:
my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')
print(*sorted(result))
Sample Output 2:
math videogames

Sample Input 3:
my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'top_grade')
print(len(sorted(result)))
Sample Output 3:
0
'''
def get_all_values(nested_dicts: int, key: str) -> set:
    _set = set()
    def rec(_dict: dict = nested_dicts):
        if key in _dict:
            _set.add(_dict[key])
        for v in _dict.values():
            if isinstance(v, dict):
                rec(v)
    rec(nested_dicts)
    return _set

if __name__ == '__main__':
    my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
    result = get_all_values(my_dict, 'top_grade')
    print(*sorted(result))

    my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
    result = get_all_values(my_dict, 'hobby')
    print(*sorted(result))

    my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
    result = get_all_values(my_dict, 'top_grade')
    print(len(sorted(result)))