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
# import numpy as np
# from datetime import datetime, timedelta
# from dateutil.parser import parse

# def return_names(names: np, dates: np) -> np:
#     _date = datetime.strptime('2022-03-22', '%Y-%m-%d').date()

#     my_dates = [
#         datetime(
#             int(str(i).split('-')[0]), 
#             int(str(i).split('-')[1]), 
#             int(str(i).split('-')[2])
#         ).date()
#         for i in dates
#     ]
#     dates = np.array(
#         object=my_dates,
#         dtype=None
#     )

#     return ' '.join(names[timedelta(60) < (_date - dates)])

import numpy as np
from datetime import datetime, timedelta

def return_names(names: np, dates: np) -> np:
    _date = datetime.strptime('2022-03-22', '%Y-%m-%d')
    return ' '.join(names[timedelta(60) < (_date - dates)])

if __name__ == '__main__':
    print(
        return_names(
            np.array(
                object='Alice Bob Charlie Dave Eve Frank Grace Harry Iris Jack Kate Liam Mia Nate Olivia Peter Quinn Rose Steve Tina'.split(),
                # object=input().split(),
                dtype=str
            ),
            np.array(
                object='2022-01-10 2022-01-09 2022-01-01 2022-02-28 2022-02-20 2022-02-15 2022-03-01 2022-03-05 2022-02-10 2022-02-20 2022-03-10 2022-02-05 2022-02-08 2022-01-20 2022-03-05 2022-02-02 2022-01-01 2022-02-28 2022-03-01 2022-03-05'.split(),
                # object=input().split(),
                dtype=str
            )
        )
    )