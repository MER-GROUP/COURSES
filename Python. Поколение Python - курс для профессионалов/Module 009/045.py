'''
Декоратор make_html

Тег — элемент языка разметки, используемый для форматирования текста. Например, текст, 
заключённый между начальным тегом <small> и конечным тегом </small>, отображается 
с меньшим размером, чем основной текст, а текст между тегами <big> и </big> отображается 
с большим размером.

Реализуйте декоратор make_html(), который принимает один аргумент:

tag — HTML-тег, например, del

Декоратор должен обрамлять возвращаемое значение декорируемой функции в HTML-тег tag.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является 
объект типа str.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое 
значение декорируемой функции, а также должен уметь декорировать функции с произвольным 
количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый 
декоратор make_html, но не код, вызывающий его. 

Примечание 4. Тестовые данные доступны по по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640040/tests_3129780.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.8/Module_9.8.18

Sample Input 1:
@make_html('del')
def get_text(text):
    return text 
print(get_text('Python'))
Sample Output 1:
<del>Python</del>

Sample Input 2:
@make_html('i')
@make_html('del')
def get_text(text):
    return text
print(get_text(text='decorators are so cool!'))
Sample Output 2:
<i><del>decorators are so cool!</del></i>
'''
from functools import wraps

def make_html(tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return f'<{tag}>{res}</{tag}>'
        return wrapper
    return decorator

if __name__ == '__main__':
    @make_html('del')
    def get_text(text):
        return text 
    print(get_text('Python'))

    @make_html('i')
    @make_html('del')
    def get_text(text):
        return text
    print(get_text(text='decorators are so cool!'))