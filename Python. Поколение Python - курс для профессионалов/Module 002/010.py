'''
Функция choose_plural() 🌶️🌶️
Реализуйте функцию choose_plural(), которая принимает 
два аргумента в следующем порядке:

amount — натуральное число, количество
declensions — кортеж из трех вариантов склонения существительного
Функция должна возвращать строку, полученную путем объединения 
подходящего существительного из кортежа declensions и количества amount, в следующем формате:

<количество> <существительное>

Примечание 1. Передаваемый в функцию кортеж легко составить 
по мнемоническому правилу: один, два, пять. Например:

для слова «арбуз»: арбуз, арбуза, арбузов
для слова «рубль»: рубль, рубля, рублей

Примечание 2. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию choose_plural(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/569748/tests_2310122.zip

Sample Input 1:
print(choose_plural(21, ('пример', 'примера', 'примеров')))
Sample Output 1:
21 пример

Sample Input 2:
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
Sample Output 2:
92 гвоздя

Sample Input 3:
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
Sample Output 3:
8 яблок
'''
def choose_plural(amount, declensions):
    if (
        (str(amount).endswith('1')) 
        and not (amount in range(11, 10**16, 100))
        ):
        return f'{amount} {declensions[0]}'
    elif (
        (
            (str(amount).endswith('2')) 
            or (str(amount).endswith('3')) 
            or (str(amount).endswith('4'))
        )
        and not (
            (amount in range(12, 10**16, 100)) 
            or (amount in range(13, 10**16, 100)) 
            or (amount in range(14, 10**16, 100))
            )
        ):
        return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[2]}'

if __name__ == '__main__':
    print(choose_plural(21, ('пример', 'примера', 'примеров')))
    print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
    print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
    print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))