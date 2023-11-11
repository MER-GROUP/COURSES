'''
Корпоративная почта 🌶️
В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, 
которая формируется как <имя-фамилия>@beegeek.bzz, например, 
timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок. 
Для решения такой проблемы было решено приписывать справа номер.

Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), 
второй — timyr-guev1@beegeek.bzz, третий — timyr-guev2@beegeek.bzz, и так далее.

Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии 
новых сотрудников в заранее подготовленном виде (латиницей с символом - между ними). 
Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

Формат входных данных
На вход программе в первой строке подается целое неотрицательное 
число n — количество выданных ящиков. В следующих n строках перечислены 
сами ящики в порядке выдачи, по одному на строке. На следующей строке 
задано целое неотрицательное число m — количество новых сотрудников, 
которым нужно раздать корпоративные ящики. Каждая из последующих m 
строк представляет собой имя и фамилию сотрудника в подготовленном 
к использованию формате.

Формат выходных данных
Программа должна вывести почтовые ящики (m строк) для новых сотрудников 
в том порядке, в котором они раздавались.

Примечание. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/569749/tests_2310074.zip

Sample Input 1:
6
ivan-petrov@beegeek.bzz
petr-ivanov@beegeek.bzz
ivan-petrov1@beegeek.bzz
ivan-ivanov@beegeek.bzz
ivan-ivanov1@beegeek.bzz
ivan-ivanov2@beegeek.bzz
3
ivan-ivanov
petr-petrov
petr-ivanov
Sample Output 1:
ivan-ivanov3@beegeek.bzz
petr-petrov@beegeek.bzz
petr-ivanov1@beegeek.bzz

Sample Input 2:
2
timyr-guev2@beegeek.bzz
anri-tabuev@beegeek.bzz
3
timyr-guev
timyr-guev
anri-tabuev
Sample Output 2:
timyr-guev@beegeek.bzz
timyr-guev1@beegeek.bzz
anri-tabuev1@beegeek.bzz
'''
def mail():
    # begin vars
    n = int(input())
    mails_old_arr = [input() for _ in range(n)]
    m = int(input())
    new_users = [input() for _ in range(m)]

    # DB vars
    mails_old_dict = dict()
    for mail_old in mails_old_arr:
        name, domen = mail_old.split('@')
        end = 0
        check = False
        for i, c in enumerate(name):
            if (c.isdigit()):
                end = i
                check = True
                break
        if check:
            mails_old_dict[name[ : end]] = mails_old_dict.get(name[ : end], []) + [name]
        else:
            mails_old_dict[name] = mails_old_dict.get(name, []) + [name]
    # print(mails_old_dict) # test

    # add new users in mail
    for user in new_users:
        i = 0
        while True:
            new_user = user if 0 == i else user + str(i)
            if new_user not in mails_old_dict and 0 == i:
                mails_old_dict[user] = mails_old_dict.get(user, [])
            if new_user not in mails_old_dict[user]:
                mails_old_arr.append(new_user+'@beegeek.bzz')
                mails_old_dict[user] = mails_old_dict.get(user, []) + [new_user]
                break
            i += 1
    # print(*mails_old_arr, sep='\n') # test

    # print new users mail
    # print('----------') # delimeter
    length = len(mails_old_arr) - m
    print(*mails_old_arr[length :], sep='\n')
    
    
if __name__ == '__main__':
    mail()