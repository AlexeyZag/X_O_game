a11, a12, a13, a21, a22, a23, a31, a32, a33 = 1, 2, 3, 4, 5, 6, 7, 8, 9
l_ = [a11, a12, a13, a21, a22, a23, a31, a32, a33]
n = 0  # счетчик ходов
win_x = 0  # счетчик побед икса
win_o = 0  # счетчик побед нуля
draw = 0  #  счетчик ничей
с = 0  # условие: если c = 1, то нужно выходить из программы (испавляет баг)
def restart():  # главня функция, которая перезпускает игру
    global l_, n, a, win_x, win_o, draw, c
    global a11, a12, a13, a21, a22, a23, a31, a32, a33, q
    a = 0  # зануляем счетчики
    q = 0  # --
    c = 0
    a11, a12, a13, a21, a22, a23, a31, a32, a33 = 1, 2, 3, 4, 5, 6, 7, 8, 9
    l_ = [a11, a12, a13, a21, a22, a23, a31, a32, a33]
    n = 0  # --
    paint()  # выводим игру на консоль
    play()  # начинаем игру
    if a == 0 and c == 0:  # если победитель не определен и команда выхода не была объявлена, то вызываем функцию ничьи
        draw_f()
def paint():  # выводит тело игры на консоль
    global n
    n += 1  # ход
    print(l_[0], '|',  l_[1], '|', l_[2])
    print('__|___|__')
    print(l_[3], '|',  l_[4], '|', l_[5])
    print('__|___|__')
    print(l_[6], '|',  l_[7], '|', l_[8])

def xmove():  # добавляет х вместо введенного числа
    for k in l_:
        if k == q:
            l_[k - 1] = 'x'
def omove():  # добавляет о вместо введенного числа
    for h in l_:
        if h == q:
            l_[h - 1] = 'o'

def input_num():  # функция ввода числа
    global q  # введенное число
    q = int(input('введите число от 1 до 9 '))
    if q not in l_:
        print("введите другое число")
        input_num()
def win():  # функция условия победы
    global a
    if l_[0] == l_[1] == l_[2] or l_[0] == l_[3] == l_[6] or l_[0] == l_[4] == l_[8] or l_[1] == l_[4] == l_[7] or l_[2] == l_[5] == l_[8] or l_[3] == l_[4] == l_[5] or l_[6] == l_[7] == l_[8] or l_[6] == l_[4] == l_[2]:
        a = 1  # если какая-нибудь строка, столбец или диагональ состоит из одинаковых элементов
    else:
        a = 0  # если нет победителя
def play():  #  функция самой игры, возвращает победителя
    global win_o, win_x, draw, c
    for i in range(9):
        if c != 0:
            break
        if a == 1:  # если уже есть победитель, то в этот цикл входить нельзя
            break
        if n % 2 == 1:  # если номер хода нечетный, то записываем х
            input_num()  # вводим число
            xmove()  # записываем х в список
            paint()  # вызываем игру на консоль
            win()  # вызываем значение a, которое отвечает за победу
            if a == 1:  # то есть победитель есть
                win_x += 1  # даем очко победы
                print(f"Выиграл х \nСчёт х:о - {win_x}:{win_o}, ничей: {draw}")  # счет партии
                if input('Сыграем снова? (y/n) ') == str('y'):  # после завершения игры предлагает сыграть снова
                    print('Новая игра!')
                    restart()  # вызываем главную функцию запуска игры
                else:
                    print('Выход')
                    break  # выходим из игры
        else:  # если номер хода нечетный, то записываем о
            input_num()
            omove()
            paint()
            win()
            if a == 1:
                win_o += 1
                print(f"Выиграл o \nСчёт х:о - {win_x}:{win_o}, ничей: {draw}")
                if input('Сыграем снова? (y/n) ') == str('y'):
                    print('Новая игра!')
                    restart()
                else:
                    print('Выход')
                    break

def draw_f():  # функция ничьи
    global a, win_x, win_o, draw
    if a == 0:  # если победитель так и не появился, то увеличиваем колво ничей
        draw += 1
        print(f"Ничья!\nСчёт х:о - {win_x}:{win_o}, ничей: {draw}")
        if input('Сыграем снова? (y/n) ') == str('y'):
            print('Новая игра!')
            restart()
        else:
            global c
            c = 1
            print('Выход')
restart() # запускает саму программу в первый раз
