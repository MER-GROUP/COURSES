#!usr/bin/gnuplot --persist
# в первой строке указываем какая программа запускает скрипт

# настройки терминала gnuplot
# set terminal pngcairo transparent enhanced font "arial,10" fontscale 1.0 size 500, 350

# переменные
# название файла куда записывать график
# output = "plot_func.png"

# внешний вид графиков
set key inside left top vertical Right noreverse enhanced autotitles box linetype -1 linewidth 1.000
# детализация для рисования (чем больше точек тем красивее)
# set samples 50, 50
set samples 250, 250

plot [-10:10] sin(x),atan(x),cos(atan(x))