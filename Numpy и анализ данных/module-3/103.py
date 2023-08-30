'''
Фитнес-центр

В базе данных фитнес-центра есть таблица со списком всех клиентов и датами их 
последнего посещения. Напишите функцию return_names(names, dates), принимающую 
два numpy массива names - имена клиентов, dates - даты в формате 'YYYY-MM-DD' 
их последнего посещения, и возвращающую строку с именами всех клиентов, 
разделенных пробелом, которые не посещали фитнес-центр более 60 дней, 
если текущая дата '2022-03-22'.

Sample Input:
Alice Bob Charlie Dave Eve Frank Grace Harry Iris Jack Kate Liam Mia Nate Olivia Peter Quinn Rose Steve Tina
2022-01-10 2022-01-09 2022-01-01 2022-02-28 2022-02-20 2022-02-15 2022-03-01 2022-03-05 2022-02-10 2022-02-20 2022-03-10 2022-02-05 2022-02-08 2022-01-20 2022-03-05 2022-02-02 2022-01-01 2022-02-28 2022-03-01 2022-03-05

Sample Output:
Alice Bob Charlie Nate Quinn
'''
import numpy as np
from datetime import datetime
from dateutil.parser import parse

pass

if __name__ == '__main__':
    pass