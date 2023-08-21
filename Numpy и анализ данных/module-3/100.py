'''
Автомобильная компания

В базе данных автомобильной компании есть таблица с информацией о моделях автомобилей 
и их стоимости. Напишите программу на Python, которая находит все модели автомобилей, 
стоимость которых больше 45 000 долларов.

На вход поступают две строки. В первой идут модели автомобилей через пробел. 
Во второй их стоимости - действительные числа.

Вывод - массив numpy моделей автомобилей, удовлетворяющих условиям задачи.

Sample Input:
BMW3-Series AudiA4 MercedesC-Class LexusIS VolvoS60 InfinitiQ50 JaguarXE CadillacATS AcuraTLX BuickRegal LincolnMKZ Chrysler300C ChevroletMalibu FordFusion ToyotaCamry HondaAccord NissanAltima Mazda6 SubaruLegacy VolkswagenPassat
33752.0 49604.0 59000.0 44695.0 50034.0 31102.0 52129.0 48795.0 39465.0 39388.0 54024.0 53606.0 40292.0 50819.0 53982.0 52782.0 50466.0 34118.0 53130.0 57512.0

Sample Output:
['AudiA4' 'MercedesC-Class' 'VolvoS60' 'JaguarXE' 'CadillacATS'
 'LincolnMKZ' 'Chrysler300C' 'FordFusion' 'ToyotaCamry' 'HondaAccord'
 'NissanAltima' 'SubaruLegacy' 'VolkswagenPassat']
'''
import numpy as np
from datetime import datetime, time

if __name__ == '__main__':
    pass