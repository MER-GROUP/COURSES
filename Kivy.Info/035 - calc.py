Простой калькулятор

Создадим простой калькулятор. Какие виджеты нам для этого нужно:
1.Вертикальный макет BoxLayout(у нас будет класс Calculator который будет наследоваться от класса BoxLayout)
2.Виджет Label где будут отображаться числа
3.Нам нужен будет макет в виде таблицы GridLayout для кнопок(мы определим его в разметке)
4.Кнопки от 0 до 9
5.Кнопки с операциями '+', '-', '*', '/', '='
6.Кнопка 'C' для очистки текста у виджета Label
Создадим два файла calcapp.py для кода и calc.kv для разметки. Начнем с кода calcapp.py. Для начала зададим размер окна 400х500 с помощью Config.set

Далее создадим класс Calculator который будет наследоваться от BoxLayout и который так же будет у нас в разметке. В нем объявим переменную label которая так же будет у нас в разметке. Так же объявим переменную first_number и будем присваивать ей первое число, но в начале присвоем ей None. Так же создадим переменную operand куда будет присваивать операции '+', '-', '*', '/', '=', но в начале она будет равна None

Начнем писать методы в этом классе. Первый метод write_number который будет присвоен событию on_press кнопкам с числами в разметке. При нажатию на кнопку с числом в нашем виджете Label будет отображаться это число. Обратите внимание что в этом методе вторым параметром после self идет instance. Параметр instance это объект который вызывает этот метод. В нашем случае это нажатая кнопка. Через instance мы будем обращаться к атрибуту text у кнопки. Сначала в этом методе мы пишим условие что operand не равен знаку '='. Если это так то переменной label(где отображаются числа) мы присваиваем старое значение переменной label плюс instance.text(число с кнопки). Далее в этом же условии пишем условие что если переменная first_number равна None, то присвоим ей же значение 0

Следующие методы операций сложения(метод add), вычитания(метод subtract), умножения(метод multiply) и деления(метод division) будут похожи и присваиваться событию on_press к соответствующим кнопкам этих операций в разметке. Единственное что в этих методах переменная operand будет принимать знак взависимости от операции. Рассмотрим метод сложения add:
1.Пишем условие если first_number равен None то выходим из метода с помощью ключевого слова return
2.Пишем условие что если переменная operand равна знаку '=' то присваиваем этой переменной operand значение None
3.Пишем условие что если operand не пустой и равен какому то знаку операции то выходим из метода с помощью ключевого слова return
4. Присваеваем переменной first_number значение с виджета label приводя его к типу int
5. Очищаем label присвоив ему пустой символ ''
6.Присваиваем переменной operand знак '+'
В остальных методах операций такой же алгоритм за исключением только того что переменная operand бует соответствовать знаку операции. Например если метод substract(вычитание) то переменная operand будет равна знаку '-',если метод multiply(умножение) то переменная operand будет равна знаку '*' и если метод division(деление) то переменная operand будет равна знаку '/'




Далее идет метод equal(равно) который в разметке мы присвоим событию on_press кнопки с текстом '=' и этот метод будет выводить в Label результат операции. Итак пишем в этом методе:
1.Условие если переменная operand равна знаку '=' или first_number равен None то мы выходим из метода с помошью ключевого слова return
2.Пишем условие для сложения чисел. Если переменная first_number не равна None и переменная operand не равна None и переменная operand равна знаку '+' то в переменную label(напомню что это переменная виджета где отображаются числа) мы присваиваем сложение переменной first_number и значение с переменной label(приведя его к числу с помощью int) и все это приводим к строчному типу с помошью str
3.Иначе если переменная first_number не равна None и переменная operand не равна None и переменная operand равна знаку '-' то в переменную label(напомню что это переменная виджета где отображаются числа) мы присваиваем вычитание переменной first_number и значение с переменной label(приведя его к числу с помощью int) и все это приводим к строчному типу с помошью str
4.Иначе если переменная first_number не равна None и переменная operand не равна None и переменная operand равна знаку '*' то в переменную label(напомню что это переменная виджета где отображаются числа) мы присваиваем умножение переменной first_number и значение с переменной label(приведя его к числу с помощью int) и все это приводим к строчному типу с помошью str
5.Иначе если переменная first_number не равна None и переменная operand не равна None и переменная operand равна знаку '/' и label.text не равен 0(потому что на ноль делить нельзя) то в переменную label(напомню что это переменная виджета где отображаются числа) мы присваиваем деление переменной first_number и значение с переменной label(приведя его к числу с помощью int) и все это приводим к строчному типу с помошью str(деление на целые числа в Python это //)
6.Присваиваем переменной operand знак '='

Следующий метод clear для очистки виджета Label, переменной first_number и переменной operand. Этот метод мы присвоим событию on_press на кнопку с текстом 'C' в разметке. Итак в этом методе все просто. Переменной first_number мы присваиваем значение None. Далее переменной operand присваиваем значение None. Переменной label присваиваем пустой текст ''

Далее создаем класс CalcApp который наследуется от класса App и в методе build создаем экземпляр класса Calculator под названием calculator

C кодом все.Теперь рассмотрим разметку calc.kv


Сначало пишем в треугольных скобках название класса Calculator как писали в коде. Далее пишем переменную label как в коде и присваиваем id:label. Так как наш класс Calculator наследуется от BoxLayout то у него есть так же атрибут orientation значение которого мы ставим 'vertical'

Далее пишем виджет Label(который отображает числа). Пишем ему id:label. Устанавливаем размер шрифта font_size значение '50sp'

Далее пишем макет GridLayout где будут располагаться кнопки в табличном виде.

Далее пишем кнопки устанавливаем у них атрибут text. У кнопок с числами событию on_press(нажатие на кнопку) присваиваем метод write_number(self) перед этим написав root.Параметр self это сама же кнопка на которую мы нажали. Это параметр нужен для того чтобы мы пользовались параметром instance в методе.

Далее кнопкам с операциями '+', '-', '*', '/', '=' мы присваем событию on_press соответствующий метод с класса. Для кнопки с '+' метод root.add(), для кнопки с '-' метод root.subtract(), для кнопки с '*' метод root.multiply(), для кнопки с '/' метод root.division() и для кнопки с '=' метод root.equal()

Для кнопки с текстом 'C' событию on_press присваиваем метод root.clear()
