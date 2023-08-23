'''
Компания-перевозчик

В базе данных компании-перевозчика есть таблица со списком всех маршрутов и датами отправления. 
Напишите функцию return_route(routes_array, dates_array), которая принимает два массива 
numpy routes_array,  содержащий названия маршрутов и dates_array, содержащий даты маршрутов 
в формате 'YYYY-MM-DD' в строковом представлении, которая находит и возвращает все маршруты, 
отправление на которые запланировано на дни с 10 по 20 включительно.

Sample Input 1:
New York - Los Angeles, San Francisco - Chicago, Seattle - Miami, Houston - Boston, Atlanta - Las Vegas, Denver - Washington, Portland - Austin, Dallas - San Diego, Boston - Philadelphia, Nashville - Memphis, Miami - Seattle, Chicago - New York, Las Vegas - Atlanta, Los Angeles - San Francisco, Washington - Denver, Austin - Portland, San Diego - Dallas, Philadelphia - Nashville, Memphis - Houston, New Orleans - Phoenix, Toronto - Montreal, Calgary - Vancouver, Montreal - Toronto, Vancouver - Calgary, Phoenix - New Orleans, Detroit - Pittsburgh, Cleveland - Cincinnati, Indianapolis - Kansas City, St. Louis - Minneapolis, Kansas City - Indianapolis
2023-04-06, 2023-04-23, 2023-04-02, 2023-04-25, 2023-04-22, 2023-04-04, 2023-04-05, 2023-04-01, 2023-04-13, 2023-04-20, 2023-04-17, 2023-04-21, 2023-04-03, 2023-04-15, 2023-04-08, 2023-04-11, 2023-04-19, 2023-04-28, 2023-04-18, 2023-04-10, 2023-04-16, 2023-04-14, 2023-04-29, 2023-04-26, 2023-04-30, 2023-04-24, 2023-04-07, 2023-04-12, 2023-04-27, 2023-04-09

Sample Output 1:
['Boston - Philadelphia' 'Nashville - Memphis' 'Miami - Seattle'
 'Los Angeles - San Francisco' 'Austin - Portland' 'San Diego - Dallas'
 'Memphis - Houston' 'New Orleans - Phoenix' 'Toronto - Montreal'
 'Calgary - Vancouver' 'Indianapolis - Kansas City']

 Sample Input 2:
New York - Chicago, San Francisco - Houston, Atlanta - Denver, Miami - Portland, Seattle - Las Vegas, Boston - Nashville, Austin - San Diego, Philadelphia - Memphis, Dallas - Washington, Chicago - New York, Houston - San Francisco, Denver - Atlanta, Portland - Miami, Las Vegas - Seattle, Nashville - Boston, San Diego - Austin, Memphis - Philadelphia, Washington - Dallas, New Orleans - Phoenix, Toronto - Calgary
2023-03-20, 2023-03-26, 2023-03-07, 2023-03-08, 2023-03-14, 2023-03-24, 2023-03-13, 2023-03-23, 2023-03-01, 2023-03-03, 2023-03-02, 2023-03-04, 2023-03-16, 2023-03-05, 2023-03-17, 2023-03-19, 2023-03-11, 2023-03-15, 2023-03-25, 2023-03-21

Sample Output 2:
['New York - Chicago' 'Seattle - Las Vegas' 'Austin - San Diego'
 'Portland - Miami' 'Nashville - Boston' 'San Diego - Austin'
 'Memphis - Philadelphia' 'Washington - Dallas']
'''
import numpy as np
from datetime import datetime, date

def return_route(routes_array: np, dates_array: np) -> np:
    # dates_array = dates_array.astype(datetime)
    dates_array = dates_array.astype(np.datetime64)
    start = date(year=dates_array[0].year, month=dates_array[0].month, day=10)
    end = date(year=dates_array[0].year, month=dates_array[0].month, day=20)
    # print(dates_array)
    # print(dates_array.dtype)
    # print(dates_array[0])
    return routes_array[start <= dates_array <= end]

if __name__ == '__main__':
    directions = 'New York - Los Angeles, San Francisco - Chicago, Seattle - Miami, Houston - Boston, Atlanta - Las Vegas, Denver - Washington, Portland - Austin, Dallas - San Diego, Boston - Philadelphia, Nashville - Memphis, Miami - Seattle, Chicago - New York, Las Vegas - Atlanta, Los Angeles - San Francisco, Washington - Denver, Austin - Portland, San Diego - Dallas, Philadelphia - Nashville, Memphis - Houston, New Orleans - Phoenix, Toronto - Montreal, Calgary - Vancouver, Montreal - Toronto, Vancouver - Calgary, Phoenix - New Orleans, Detroit - Pittsburgh, Cleveland - Cincinnati, Indianapolis - Kansas City, St. Louis - Minneapolis, Kansas City - Indianapolis'.split(', ')
    dates = '2023-04-06, 2023-04-23, 2023-04-02, 2023-04-25, 2023-04-22, 2023-04-04, 2023-04-05, 2023-04-01, 2023-04-13, 2023-04-20, 2023-04-17, 2023-04-21, 2023-04-03, 2023-04-15, 2023-04-08, 2023-04-11, 2023-04-19, 2023-04-28, 2023-04-18, 2023-04-10, 2023-04-16, 2023-04-14, 2023-04-29, 2023-04-26, 2023-04-30, 2023-04-24, 2023-04-07, 2023-04-12, 2023-04-27, 2023-04-09'.split(', ')
    return_route(np.array(directions), np.array(dates))