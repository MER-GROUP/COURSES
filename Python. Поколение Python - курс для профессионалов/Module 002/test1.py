"""
Вам доступна строка txt, которая содержит некоторый текст.

Дополните приведенный код, используя срезы, так чтобы переменные 
first, second и third содержали текст в соответствии с условием:

 - first: каждый третий символ строки txt, начиная с пятого символа
 - second: все символы строки txt с сотого по трехсотый (включительно)
 - third: каждый десятый символ строки txt в обратном порядке (начиная с конца строки)

Примечание. Считайте, что нумерация символов в строке начинается с нуля.
"""

txt = '''Travelling to far countries is always a thrilling and interesting adventure. Heading for the other end of the world, it’s impossible to go without such an aircraft as “a plane”. But before boarding a plane, one must book a seat in advance and go though other different formalities.

If you got your foreign passport or have just applies for it, it’s time to think about buying airplane tickets. You can buy tickets at ticket offices or book flights online. Moreover, don’t forget to get travel insurance. As a rule, it’s required (it’s obligatory).

The tickets are on hand, the insurance is in a pocket, a suitcase is packed – it’s time to go to the airport. You should arrive at the airport two hours earlier whether you fly in business class or in economy class. Why? In order to go to check-in counter (desk) and afterwards to passport control. If you don’t like traveling light, you will be charged for excess baggage.

Thst’s it – it’s high time you boarded ( got on) a place. It will take off any moment. We hope that you don’t suffer from travel sickness. Bon voyage!'''

first = txt[5 : : 3]
second = txt[100 : 301 : 1]
third = txt[-1 : : -10]

print(first)
print('------------')
print(second)
print('------------')
print(third)