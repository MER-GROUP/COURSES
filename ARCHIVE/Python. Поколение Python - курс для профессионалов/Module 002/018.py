'''
Схожие слова
Напишите программу, которая находит все схожие слова для заданного слова. 
Слова называются схожими, если имеют одинаковое количество и 
расположение гласных букв. При этом сами гласные могут различаться.

Формат входных данных
На вход программе подается одно слово, записанное в первой строке, 
затем натуральное число n — количество слов для сравнения и n строк со словами.

Формат выходных данных
Программа должна вывести все схожие слова для заданного слова, 
сохранив их исходный порядок следования.

Примечание 1. После последней гласной в начальном и проверяемом 
слове может быть любое количество согласных.

Примечание 2. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) 
и 21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/569749/tests_2310069.zip

Sample Input 1:
машина
8
сеть
машинист
дорога
урок
работа
аксиома
железо
ветеран
Sample Output 1:
машинист
дорога
работа
железо
ветеран

Sample Input 2:
весть
3
месть
гость
лань
Sample Output 2:
месть
гость
лань

Sample Input 3:
фигура
5
машинаннннн
ржавчина
граль
река
полинанннннннннн
Sample Output 3:
машинаннннн
полинанннннннннн
'''
def equal_words(word_std: str, n: int) -> list[str]:
    word_std_len = len(word_std)
    words = [input() for _ in range(n)]
    vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
    # consonants = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')
    res = list()
    vowels_index = [i for i in range(word_std_len) if word_std[i] in vowels]
    # consonants_index = [i for i in range(word_std_len) if word_std[i] in consonants]

    for word in words:
        if word_std_len <= len(word):
            vowels_index_word = [i for i in range(word_std_len) if word[i] in vowels]
            # consonants_index_word = [i for i in range(word_std_len) if word[i] in consonants]
            if vowels_index == vowels_index_word:
                if vowels_index[-1] == vowels_index_word[-1]:
                    res.append(word)
        else:
            word_len = len(word)
            vowels_index_word = [i for i in range(word_len) if word[i] in vowels]
            if vowels_index == vowels_index_word:
                if vowels_index[-1] == vowels_index_word[-1]:
                    res.append(word)

    return res
    
if __name__ == '__main__':
    print(*equal_words(input() ,int(input())), sep='\n')
    # print(equal_words(input() ,int(input())))