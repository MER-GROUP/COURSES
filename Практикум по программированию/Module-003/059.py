'''
Диета
В некоторой сверхсекретной лаборатории изучаются физические возможности животных. 
Любой живой организм нуждается в трех компонентах пищи – белках, жирах и углеводах. 
Известен набор продуктов, имеющийся в распоряжении лаборатории, 
и меню животных – сколько единиц каждого продукта они получают. 
Известно также, сколько белков, жиров и углеводов необходимо для нормальной 
жизнедеятельности животного. Необходимо определить, получает ли животное 
достаточное количество питательных веществ. Известно, что животному требуется 
в сутки X белков, Y жиров и Z углеводов. 

Известно также, что всего животное получает в сутки N продуктов питания, 
и для каждого из них известны A_i, B_i, C_i, и Q_i – соответственно, 
энергетическая ценность единицы продукта в белках, жирах и углеводах 
и количество единиц этого продукта. Все числа – действительные, 
заданные с точностью до 5 знаков после запятой.

Входные данные
На первой строке входных данных записаны числа X , Y и Z. На второй 
строке записано число N. Далее на N строках записаны, соответственно, 
A_i, B_i, C_i, и Q_i.

Выходные данные
Выведите YES , если данный пищевой рацион является достаточным 
по всем параметрам, и NO в противном случае.

Sample Input:
1.0 1.0 1.0
3
1 0 0 1
0 0.5 0 2
0 0 0.25 4
Sample Output:
YES
'''
import sys
import decimal as d

# sys.stdin = open(file='059.csv', mode='rt', encoding='utf-8', newline='')
_xyz, _, *_abcq = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(_xyz) # test
# print(_) # test
# print(_abcq) # test

_list_xyz = list()
for i in map(d.Decimal, _xyz.split()):
    _list_xyz.append(i)

_list_abcq = list()
for _str in _abcq:
    _arr = tuple(map(d.Decimal,_str.split()))
    _list_abcq.append(sum(_arr[:-1]) * _arr[-1])

x, y, z = map(lambda x, y: x - y, _list_xyz, _list_abcq)
if (x<=0) and (y<=0) and (z<=0):
    print('YES') 
else:
    print('NO')
# print(('NO', "YES")[all(map(lambda x, y: x - y <= 0, _list_xyz, _list_abcq))])

"""
var
  x,y,z,a,b,c,q:real;
  i:integer;
begin
  readln(x,y,z);
  readln(i);
  for i:=1 to i do begin
    readln(a,b,c,q);
    x:=x-a*q;
    y:=y-b*q;
    z:=z-c*q;
  end;
  if (x<=0) and (y<=0) and (z<=0) then writeln('YES') else writeln('NO');
end.
"""