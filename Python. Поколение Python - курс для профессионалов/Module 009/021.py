'''
Функция verification()
Реализуйте функцию verification(), которая проверяет правильность введенного пароля. 
Она должна принимать четыре аргумента в следующем порядке:

login — логин пользователя
password — пароль пользователя
success — некоторая функция
failure — некоторая функция

Пароль считается правильным, если в нем присутствует, хотя бы одна заглавная латинская буква, 
хотя бы одна строчная латинская буква и хотя бы одна цифра. Функция verification() 
должна вызывать функцию success() с аргументом login, если переданный пароль является 
правильным, иначе — функцию failure() с аргументами login и строкой-сообщением об ошибке:

в пароле нет ни одной буквы, если в пароле отсутствуют латинские буквы
в пароле нет ни одной заглавной буквы, если в пароле отсутствуют заглавные латинские буквы
в пароле нет ни одной строчной буквы, если в пароле отсутствуют строчные латинские буквы
в пароле нет ни одной цифры, если в пароле отсутствуют цифры

Примечание 1. Если пароль не удовлетворяет нескольким условиям, то приоритеты 
выбора строки-сообщения об ошибке являются следующими:

в пароле нет ни одной буквы
в пароле нет ни одной заглавной буквы
в пароле нет ни одной строчной буквы
в пароле нет ни одной цифры

Примечание 2. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию verification(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640036/tests_2670414.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.3/Module_9.3.18

Sample Input 1:
def success(login):
    print(f'Привет, {login}!')
def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')
verification('timyrik20', 'Beegeek314', success, failure)
Sample Output 1:
Привет, timyrik20!

Sample Input 2:
def success(login):
    print(f'Здравствуйте, {login}!')
def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')
verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)
Sample Output 2:
Ruslan_Chaniev, попробуйте снова. Текст ошибки: в пароле нет ни одной заглавной буквы
'''
def verification(login: str, password: str, success: None, failure: None):
    _password = ''.join(i for i in password if i.isascii())
    _isupper = _password.isupper()
    _islower = _password.islower()
    _isalpha = _password.isalpha()
    _isnumeric = _password.isnumeric()
    _check_pswd = not any(
        (_isupper, _islower, _isalpha, _isnumeric)
    )
    if _check_pswd:
        success(login)
    else:
        _is_not_alpha_text = 'в пароле нет ни одной буквы' if not _password or _isnumeric else ''
        _is_not_upper_text = 'в пароле нет ни одной заглавной буквы' if _islower else ''
        _is_not_lower_text = 'в пароле нет ни одной строчной буквы' if _isupper else ''
        _is_not_numeric_text = 'в пароле нет ни одной цифры' if _isalpha else ''
        _text = str()
        for _str in (_is_not_alpha_text, _is_not_upper_text, _is_not_lower_text, _is_not_numeric_text):
                if _str:
                    _text += _str
                    break
        failure(login, _text)

if __name__ == '__main__':
    # 1 test-1
    def success(login):
        print(f'Привет, {login}!')
    def failure(login, text):
        print(f'{login}, попробуйте снова. Ошибка: {text}')
    verification('timyrik20', 'Beegeek314', success, failure)

    # 2 test-2
    def success(login):
        print(f'Здравствуйте, {login}!')
    def failure(login, text):
        print(f'{login}, попробуйте снова. Текст ошибки: {text}')
    verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)

    # 3 test-7
    def success(login):
        print(f'Здравствуйте, {login}!')
    def failure(login, text):
        print(f'{login}, попробуйте снова. Текст ошибки: {text}')
    verification('Arthur_Davletov', 'мойпароль123', success, failure)

    # 4 test-8
    def success(login):
        print(f'Здравствуйте, {login}!')
    def failure(login, text):
        print(f'{login}, попробуйте снова. Текст ошибки: {text}')
    verification('Arthur_Davletov', 'мойпарольbee123', success, failure)

    # 4 test-9
    def success(login):
        print(f'Здравствуйте, {login}!')
    def failure(login, text):
        print(f'{login}, попробуйте снова. Текст ошибки: {text}')
    verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)

    # # test
    # print(sorted('мойпароль123', key=lambda x : (x.isnumeric(), not x.isascii())))
    # print(sorted('мойпароль123', key=lambda x : (x.isnumeric(), not x.isascii()))[0].isascii())

    # # test
    # print(sorted('мойпарольbee123', key=lambda x : (x.isnumeric(), not x.isascii())))
    # print(sorted('мойпарольbee123', key=lambda x : (x.isnumeric(), not x.isascii()))[0].isascii())

    # # test
    # print(sorted('мойпарольBEE123', key=lambda x : (x.isnumeric(), not x.isascii())))
    # print(sorted('мойпарольBEE123', key=lambda x : (x.isnumeric(), not x.isascii()))[0].isascii())
    # print('мойпарольBEE123'.isupper())
    # print('мойпарольBEE123'.islower())
    # print(''.isascii())
    # print(' '.isascii())