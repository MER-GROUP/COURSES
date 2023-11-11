'''
Даты

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют даты следующих форматов:

DD.MM.YYYY
DD/MM/YYYY
YYYY.MM.DD
YYYY/MM/DD

Примечание 1. Дополнительная проверка даты на корректность не требуется.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/683127/tests_2833101.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.2/Module_11.2.21

regex = r''

Sample Input 1:
-- Exam days -- Math: 24.03.2022 Chemistry: 24/03/2022 Physics: 2022.03.25 France: 2022/03/29
Sample Output 1:
24.03.2022 24/03/2022 2022.03.25 2022/03/29

Sample Input 2:
first date: 01.12.22, second date: 01/12/22, thirs date 09.07.2003 07/09/2003
Sample Output 2:
09.07.2003 07/09/2003
'''
regex = r'\d{2}\.\d{2}\.\d{4}|\d{2}/\d{2}/\d{4}|\d{4}\.\d{2}\.\d{2}|\d{4}/\d{2}/\d{2}'

regex = r'\d{2}\.\d{2}\.\d{4}|' \
        r'\d{2}/\d{2}/\d{4}|' \
        r'\d{4}\.\d{2}\.\d{2}|' \
        r'\d{4}/\d{2}/\d{2}'

regex = r'\d{2}[.]\d{2}[.]\d{4}|'\
        r'\d{2}[/]\d{2}[/]\d{4}|'\
        r'\d{4}[.]\d{2}[.]\d{2}|'\
        r'\d{4}[/]\d{2}[/]\d{2}'