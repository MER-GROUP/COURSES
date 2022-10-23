'''
Транслитерация 🌶️
Транслитерация — передача знаков одной письменности знаками 
другой письменности, при которой каждый знак (или последовательность знаков) 
одной системы письма передаётся соответствующим знаком 
(или последовательностью знаков) другой системы письма.

Вам доступен текстовый файл cyrillic.txt, содержащий текст. 
Напишите программу для транслитерации этого файла, 
то есть замены кириллических символов на латинские в 
соответствии с предложенной таблицей. Все остальные 
символы надо оставить без изменений. Результат 
транслитерации требуется записать в файл transliteration.txt.

Кириллица 	Латиница	Кириллица	Латиница	Кириллица	Латиница
а	a	к	k	х	h
б	b	л	l	ц	c
в	v	м	m	ч	ch
г	g	н	n	ш	sh
д	d	о	o	щ	shh
е	e	п	p	ъ	*
ё	jo	р	r	ы	y
ж	zh	с	s	ь	'
з	z	т	t	э	je
и	i	у	u	ю	ju
й	j	ф	f	я	ya
Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем transliteration.txt 
в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа 
и указанные файлы находятся в одной папке.

Примечание 2. Обратите внимание, что заглавные буквы 
должны заменяться на соответствующие им заглавные 
же буквы, но если транслитерационная последовательность 
состоит из нескольких символов, то заглавным будет 
только первый из них: «С» на «S», а «Я» на «Ya».

Примечание 3. Если бы файл cyrillic.txt содержал текст:

Президент США Дональд Трамп продолжил обмен выпадами 
с руководством КНДР.
We all know why Joe Biden is rushing to falsely pose 
as the winner, and why his media allies are trying 
so hard to help him: they don’t want the truth to be exposed.

то содержимое файла transliteration.txt будет:

Prezident SShA Donal'd Tramp prodolzhil obmen vypadami s rukovodstvom KNDR.
We all know why Joe Biden is rushing to falsely pose as the winner, 
and why his media allies are trying so hard to help him: 
they don’t want the truth to be exposed.
Примечание 4. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/448983/cyrillic.txt
'''
# Решение
# with open('forbidden_words.txt', 'rt', encoding='utf-8') as file_words,\
#     open(input(), 'rt', encoding='utf-8') as file_in:
with open('cyrillic.txt', 'rt', encoding='utf-8') as file_in,\
    open('transliteration.txt', 'wt', encoding='utf-8') as file_out:
    my_dict = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }
    arr = list(file_in.read())
    # print(*arr)
    for i, el in enumerate(arr):
        check = False
        if(el.isupper()):
            check = True
            el = el.lower()
        if el in my_dict.keys():
            arr[i] = my_dict[el].capitalize() if check else my_dict[el]
    print(''.join(arr))
