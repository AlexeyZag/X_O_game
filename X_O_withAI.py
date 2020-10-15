import random
win_x = 0  # счетчик побед икса
win_o = 0  # счетчик побед нуля
draw = 0  #  счетчик ничей
def restart():  # главня функция, которая перезпускает игру
    global l_, n, a, winner, x_move, allow_list_int
    global a11, a12, a13, a21, a22, a23, a31, a32, a33, q
    allow_list_int = {1, 2, 3, 4, 5, 6, 7, 8, 9}  # список доступных ходов
    a = 0  # зануляем счетчики
    q = 0  # --
    x_move = set()  # список ходов икса
    winner = None
    a11, a12, a13, a21, a22, a23, a31, a32, a33 = 1, 2, 3, 4, 5, 6, 7, 8, 9
    l_ = [a11, a12, a13, a21, a22, a23, a31, a32, a33]
    n = 0  # --
    paint()  # выводим игру на консоль
    play()  # начинаем игру
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
            allow_list_int.remove(q)
            return
def omove():  # добавляет о вместо введенного числа
    for h in l_:
        if h == q:
            l_[h - 1] = 'o'
            allow_list_int.remove(q)
            return
def input_num():  # функция ввода числа
    global q, allow_list_int, x_move, allow_list_int   # введенное число
    allow_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    q = input('введите число от 1 до 9 ')
    if q not in allow_list or int(q) not in l_ :
        print("введите другое число")
        input_num()
    else:
        q = int(q)
        x_move.add(q)

def win():  # функция условия победы
    global a
    if l_[0] == l_[1] == l_[2] or l_[0] == l_[3] == l_[6] or l_[0] == l_[4] == l_[8] or l_[1] == l_[4] == l_[7] or l_[2] == l_[5] == l_[8] or l_[3] == l_[4] == l_[5] or l_[6] == l_[7] == l_[8] or l_[6] == l_[4] == l_[2]:
        a = 1  # если какая-нибудь строка, столбец или диагональ состоит из одинаковых элементов
    else:
        a = 0  # если нет победителя
def play():  #  функция самой игры, возвращает победителя
    global win_o, win_x, draw, winner
    for i in range(9):
        if n % 2 == 1:  # если номер хода нечетный, то записываем х
            input_num()  # вводим число
            xmove()  # записываем х в список
            paint()  # вызываем игру на консоль
            win()  # вызываем значение a, которое отвечает за победу
            if a == 1:  # то есть победитель есть
                win_x += 1  # даем очко победы
                winner = "Выиграл х. "
                end_game()
                return
            elif a == 0 and n > 9:
                draw += 1
                winner = "Ничья! "
                end_game()
                return
        else:  # если номер хода нечетный, то записываем о
            input_num()
            omove()
            paint()
            win()
            if a == 1:
                win_o += 1
                winner = "Выиграл o. "
                end_game()
                return

def end_game():  # вызывается, когда игра подошла к концу
    print(f"{winner} \nСчёт х:о - {win_x}:{win_o}, ничей: {draw}")  # счет партии
    asq_str = input('Сыграем снова? Против человека/бота/выход (o/y/n) ')
    if  asq_str == str('o'):  # после завершения игры предлагает сыграть снова
        print('Новая игра!')
        restart()  # вызываем главную функцию запуска игры
    elif asq_str == str('y'):
        print('Новая игра с ботом!')
        restartAI()
    elif asq_str == str('n'):
        print('Выход')
        return
    else:
        print('Введите другое значение')
        end_game()

def playAI():  #  функция самой игры, возвращает победителя
    global win_o, win_x, draw, winner, q, c, allow_list_int
    for i in range(9):
        if n % 2 == 1:  # если номер хода нечетный, то записываем х
            input_num()  # вводим число
            xmove()  # записываем х в список
            paint()  # вызываем игру на консоль
            win()  # вызываем значение a, которое отвечает за победу
            if a == 1:  # то есть победитель есть
                win_x += 1  # даем очко победы
                winner = "Выиграл х. "
                end_game()
                return
            elif a == 0 and n > 9:
                draw += 1
                winner = "Ничья! "
                end_game()
                return
        else:  # если номер хода нечетный, то записываем о

            move_list11, move_list12 = {1, 3, 7, 9, 2, 4, 6, 8}, {5}
            c = 0
            if n == 2 and q in move_list11:  # если икс ставится не в центр, то ставим о в центр
                q = 5
            elif n == 2 and q in move_list12:
                allow_list_1 = [1, 3, 7, 9] # если первым ходом икс стоит в центре
                q = random.choice(list(allow_list_1))
            if n == 4 and (x_move == {1, 9} or x_move == {3, 7}): # если после второго хода иксы стоят по углам
                allow_list_2 = [2, 4, 6, 8]
                q = random.choice(list(allow_list_2))
            elif n == 4 and (allow_list_int == {1, 2, 4, 6, 8, 9}):  # если по диагонали стоят два икса и ноль в углу
                q = random.choice([1, 9])
            elif n == 4 and (allow_list_int == {2, 3, 4, 6, 7, 8}):
                q = random.choice([3, 7])
            elif n == 4: # and (x_move != {1, 9} or x_move != {3, 7} or x_move != {1, 5} or x_move != {3, 5} or x_move != {5, 9} or x_move != {5, 7}):
                hot_moves()
                if c == 0:
                    q = random.choice(list(allow_list_int))
            if c == 0 and n > 4:
                very_hot_moves()
                if c == 0:
                    hot_moves()
                    if c == 0:
                        q = random.choice(list(allow_list_int))
            omove()
            paint()
            win()
            if a == 1:
                win_o += 1
                winner = "Выиграл o. "
                end_game()
                return
def very_hot_moves():
    global q, c
    c = 0
    if (l_[0] == l_[1] == 'o' or l_[4] == l_[6] == 'o' or l_[5] == l_[8] == 'o') and l_[2] == 3:
        q, c = 3, 1
    elif (l_[0] == l_[2] == 'o' or l_[4] == l_[7] == 'o') and l_[1] == 2:
        q, c = 2, 1
    elif (l_[1] == l_[2] == 'o' or l_[3] == l_[6] == 'o' or l_[4] == l_[8] == 'o') and l_[0] == 1:
        q, c = 1, 1
    elif (l_[2] == l_[8] == 'o' or l_[4] == l_[3] == 'o') and l_[5] == 6:
        q, c = 6, 1
    elif (l_[0] == l_[8] == 'o' or l_[1] == l_[7] == 'o' or l_[2] == l_[6] == 'o' or l_[3] == l_[5] == 'o') and l_[4] == 5:
        q, c = 5, 1
    elif (l_[0] == l_[6] == 'o' or l_[4] == l_[5] == 'o') and l_[3] == 4:
        q, c = 4, 1
    elif (l_[2] == l_[5] == 'o' or l_[6] == l_[7] == 'o' or l_[0] == l_[4] == 'o') and l_[8] == 9:
        q, c = 8, 1
    elif (l_[6] == l_[8]== 'o' or l_[1] == l_[4] == 'o') and l_[7] == 8:
        q, c = 8, 1
    elif (l_[0] == l_[3] == 'o' or l_[4] == l_[2] == 'o' or l_[8] == l_[7] == 'o') and l_[6] == 7:
        q, c = 7, 1
def hot_moves():
    global q, c
    if (l_[0] == l_[1] == 'x' or l_[4] == l_[6] == 'x' or l_[5] == l_[8] == 'x') and l_[2] == 3:
        q, c = 3, 2
    elif (l_[0] == l_[2] == 'x' or l_[4] == l_[7] == 'x') and l_[1] == 2:
        q, c = 2, 2
    elif (l_[1] == l_[2] == 'x' or l_[3] == l_[6] == 'x' or l_[4] == l_[8] == 'x') and l_[0] == 1:
        q, c = 1, 2
    elif (l_[2] == l_[8] == 'x' or l_[4] == l_[3] == 'x') and l_[5] == 6:
        q, c = 6, 2
    elif (l_[0] == l_[8] == 'x' or l_[1] == l_[7] == 'x' or l_[2] == l_[6] == 'x' or l_[3] == l_[5] == 'x') and l_[4] == 5:
        q, c = 5, 2
    elif (l_[0] == l_[6] == 'x' or l_[4] == l_[5] == 'x') and l_[3] == 4:
        q, c = 4, 2
    elif (l_[2] == l_[5] == 'o' or l_[6] == l_[7] == 'o' or l_[0] == l_[4] == 'o') and l_[8] == 9:
        q, c = 9, 2
    elif (l_[6] == l_[8] == 'x' or l_[1] == l_[4] == 'x') and l_[7] == 8:
        q, c = 8, 2
    elif (l_[0] == l_[3] == 'o' or l_[4] == l_[2] == 'o' or l_[8] == l_[7] == 'o') and l_[6] == 7:
        q, c = 7, 2
def restartAI():
    global l_, n, a, winner, c, allow_list_int, x_move
    global a11, a12, a13, a21, a22, a23, a31, a32, a33, q
    allow_list_int = {1, 2, 3, 4, 5, 6, 7, 8, 9} # список доступных ходов
    x_move = set()  # список ходов икса
    a = 0  # зануляем счетчики
    q = 0  # --
    c = 0
    winner = None
    a11, a12, a13, a21, a22, a23, a31, a32, a33 = 1, 2, 3, 4, 5, 6, 7, 8, 9
    l_ = [a11, a12, a13, a21, a22, a23, a31, a32, a33]
    n = 0  # --
    paint()  # выводим игру на консоль
    playAI()
def start():
    x = int(input("введите 1 для игры вдвоем или 2 против ИИ "))
    if x == 1:
        restart()
    else:
        restartAI()
start()