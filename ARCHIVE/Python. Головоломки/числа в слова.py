# объявление функции
def number_to_words(num):
    edinici = [None, 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    iskluch = [None, 'одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятннадцать']
    desytki = [None, 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят','девяносто']
    if 1 <= num <= 9:
    	return edinici[num]
    elif num in (10, 20, 30, 40, 50, 60, 70, 80, 90):
    	return desytki[int(num / 10)]
    elif 11 <= num <= 19:
    	return iskluch[num - 10]
    else:
    	a = int(str(num)[0])
    	b = int(str(num)[1])
    	return desytki[a] + ' ' + edinici[b]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))