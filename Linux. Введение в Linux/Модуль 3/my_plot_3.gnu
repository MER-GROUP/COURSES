#!usr/bin/gnuplot -persist
# в первой строке указываем какая программа запускает скрипт
# переменные
# название файла куда записывать график
# out_name = "my_plot2.png"
# название файла откуда боать данные для построения графика
# in_name = "authors.txt"
# наименование 2-й колонки в файле
column_1 = 2
# наименование 3-й колонки в файле
column_2 = 3

# тип епртинки (расширенный png)
set terminal png enhanced
# куда сохраняем картинку
set output out_name
# отношение сторон картинки
set size ratio 0.5
# название графика
set title "График для данных в файле ".in_name." столбцы ".column_1.", ".column_2
# название оси X
set xlabel "Время работы, c"
# название оси Y
set ylabel "Повышение сорбции красителя, %"
# установить количество отсечек на оси X
set xtics ("0" 0, "15" 15, "30" 30, "60" 60, "120" 120, "180" 180)
# автомасштабирование оси Y
set autoscale y
# установить сетку
set grid
# брать название ряда данных из первой строчки файла
set key autotitle columnhead

# вязять данный из файла authors.txt и для каждого графика 
# используем линии и точки
plot in_name using 1:column_1 smooth csplines notitle with lines lt 1,\
in_name  using 1:column_1 with points pointsize 1 pointtype 7 lt 1,\
in_name  using 1:column_2 smooth csplines notitle with lines lt 2,\
in_name  using 1:column_2 with points pointsize 1 pointtype 13 lt 2