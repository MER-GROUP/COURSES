#!usr/bin/gnuplot -persist
# в первой строке указываем какая программа запускает скрипт
# тип епртинки (расширенный png)
set terminal png enhanced
# куда сохраняем картинку
set output "my_plot.png"
# отношение сторон картинки
set size ratio 0.5
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
plot "authors.txt" using 1:2 smooth csplines notitle with lines lt 1,\
"authors.txt" using 1:2 with points pointsize 1 pointtype 7 lt 1,\
"authors.txt" using 1:3 smooth csplines notitle with lines lt 2,\
"authors.txt" using 1:3 with points pointsize 1 pointtype 13 lt 2