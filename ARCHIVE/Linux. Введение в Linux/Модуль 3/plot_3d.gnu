#!usr/bin/gnuplot --persist
# в первой строке указываем какая программа запускает скрипт

# настройки терминала gnuplot
# set terminal pngcairo transparent enhanced font "arial,10" fontscale 1.0 size 500, 350

# переменные
# название файла куда записывать график
# output = "plot_3d.png"

set grid nopolar
set grid xtics nomxtics ytics nomytics noztics nomztics \
nox2tics nomx2tics noy2tics nomy2tics nocbtics nomcbtics
set grid layerdefault linetype -1 linecolor rgb "gray" linewidth 0.200, \
linetype -1 linecolor rgb "gray" linewidth 0.200
# детализация для рисования (чем больше точек тем красивее)
set samples 21, 21
set isosamples 11, 11
set title "3D gnuplo demo"
set xlabel "X axis"
set xlabel offset character -3, -2, 0 font "" textcolor lt -1 norotate
set xrange [-10.000:10.000] noreverse nowriteback
set ylabel "Y axis"
set ylabel offset character 3, -2, 0 font "" textcolor lt -1 rotate by -270
set yrange [-10.000:10.000] noreverse nowriteback
set zlabel "Z axis"
set xlabel offset character 1, 0, 0 font "" textcolor lt -1 norotate

splot x**2+y**2, x**2-y**2