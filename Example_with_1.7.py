import matplotlib.pyplot as plt
from termcolor import cprint

def μNUM_triangle(x, a, b, c):
    '''
    Функция принадлежности для треугольного
    нечеткого числа NUM
    '''
    if a != b != c:
        if x in range(a, b + 1):
            return round((x - a) / (b - a), 2)
        elif x in range(b, c + 1):
            return round((x - c) / (b - c), 2)
        else:
            return 0
    elif a == b < c:
        if x in range(b, c + 1):
            return round((x - c) / (b - c), 2)
        else:
            return 0
    elif a < b == c:
        if x in range(a, b + 1):
            return round((x - a) / (b - a), 2)
        else:
            return 0
    elif a == b == c:
        if x == b:
            return 1
        else:
            return 0

def μNUM_trapezoid(x, a, b, c, d):
    '''
    Функция принадлежности для трапецеидального
    нечеткого числа NUM
    '''
    if a < b <= c < d:
        if x in range(a, b + 1):
            return round((x - a) / (b - a), 2)
        elif x in range(b, c + 1):
            return 1
        elif x in range(c, d + 1):
            return round((d - x) / (d - c), 2)
        else:
            return 0
    elif a == b <= c < d:
        if x in range(b, c + 1):
            return 1
        elif x in range(c, d + 1):
            return round((d - x) / (d - c), 2)
        else:
            return 0
    elif a < b <= c == d:
        if x in range(a, b + 1):
            return round((x - a) / (b - a), 2)
        elif x in range(b, c + 1):
            return 1
        else:
            return 0


t = list(range(24, 37))
A1 = [24, 24, 27]
print(len('A1 - "медленно":')*'-')
print('A1 - "медленно":')
print('<a, b, c> =', A1)
t1_lst = []
μA1_lst = []
for t1 in range(A1[0], A1[2] + 1):
    #print('μ(' + str(t1) + ') =', μNUM_triangle(t1, A1[0], A1[1], A1[2]))
    cprint('μ(' + str(t1) + ') = ' + str(μNUM_triangle(t1, A1[0], A1[1], A1[2])), color="red")
    t1_lst.append(t1)
    μA1_lst.append(μNUM_triangle(t1, A1[0], A1[1], A1[2]))

A2 = [25, 28, 33]
print(len('A2 - "средне":')*'-')
print('A2 - "средне":')
print('<a, b, c> =', A2)
t2_lst = []
μA2_lst = []
for t2 in range(A2[0], A2[2] + 1):
    #print('μ(' + str(t2) + ') =', μNUM_triangle(t2, A2[0], A2[1], A2[2]))
    cprint('μ(' + str(t2) + ') = ' +
           str(μNUM_triangle(t2, A2[0], A2[1], A2[2])), color="yellow")
    t2_lst.append(t2)
    μA2_lst.append(μNUM_triangle(t2, A2[0], A2[1], A2[2]))

A3 = [28, 33, 36, 36]
print(len('A3 - "быстро":')*'-')
print('A3 - "быстро":')
print('<a, b, c, d> =', A3)
t3_lst = []
μA3_lst = []
for t3 in range(A3[0], A3[3] + 1):
    #print('μ(' + str(t3) + ') =', μNUM_trapezoid(t3, A3[0], A3[1], A3[2], A3[3]))
    cprint('μ(' + str(t3) + ') = ' +
           str(μNUM_trapezoid(t3, A3[0], A3[1], A3[2], A3[3])), color="green")
    t3_lst.append(t3)
    μA3_lst.append(μNUM_trapezoid(t3, A3[0], A3[1], A3[2], A3[3]))


s = list(range(30, 120))
B1 = [30, 30, 75]
print(len('B1 - "слабо":')*'-')
print('B1 - "слабо":')
print('<a, b, c> =', B1)
s1_lst = []
μB1_lst = []
for s1 in range(B1[0], B1[2] + 1):
    # print('μ(' + str(s1) + ') =', μNUM_triangle(s1, B1[0], B1[1], B1[2]))
    cprint('μ(' + str(s1) + ') = ' + \
           str(μNUM_triangle(s1, B1[0], B1[1], B1[2])), color="red")
    s1_lst.append(s1)
    μB1_lst.append(μNUM_triangle(s1, B1[0], B1[1], B1[2]))

B2 = [60, 80, 105]
print(len('B2 - "хорошо":')*'-')
print('B2 - "хорошо":')
print('<a, b, c> =', B2)
s2_lst = []
μB2_lst = []
for s2 in range(B2[0], B2[2] + 1):
    # print('μ(' + str(s2) + ') =', μNUM_triangle(s2, B2[0], B2[1], B2[2]))
    cprint('μ(' + str(s2) + ') = ' + \
           str(μNUM_triangle(s2, B2[0], B2[1], B2[2])), color="yellow")
    s2_lst.append(s2)
    μB2_lst.append(μNUM_triangle(s2, B2[0], B2[1], B2[2]))


B3 = [85, 110, 120, 120]
print(len('B3 - "отлично":')*'-')
print('B3 - "отлично":')
print('<a, b, c> =', B3)
s3_lst = []
μB3_lst = []
for s3 in range(B3[0], B3[3] + 1):
    # print('μ(' + str(s3) + ') =', μNUM_trapezoid(s3, B3[0], B3[1], B3[2], B3[3]))
    cprint('μ(' + str(s3) + ') = ' + \
           str(μNUM_trapezoid(s3, B3[0], B3[1], B3[2], B3[3])), color="green")
    s3_lst.append(s3)
    μB3_lst.append(μNUM_trapezoid(s3, B3[0], B3[1], B3[2], B3[3]))


# Σ = list(range(30, 120))
D1 = [0, 0, 35]
print(len('D1 - "низкая":')*'-')
print('D1 - "низкая":')
print('<a, b, c> =', D1)
Σ1_lst = []
μD1_lst = []
for Σ1 in range(D1[0], D1[2] + 1):
    # print('μ(' + str(Σ1) + ') =', μNUM_triangle(Σ1, D1[0], D1[1], D1[2]))
    cprint('μ(' + str(Σ1) + ') = ' + \
           str(μNUM_triangle(Σ1, D1[0], D1[1], D1[2])), color="red")
    Σ1_lst.append(Σ1)
    μD1_lst.append(μNUM_triangle(Σ1, D1[0], D1[1], D1[2]))


D2 = [20, 40, 65]
print(len('D2 - "средняя":')*'-')
print('D2 - "средняя":')
print('<a, b, c> =', D2)
Σ2_lst = []
μD2_lst = []
for Σ2 in range(D2[0], D2[2] + 1):
    # print('μ(' + str(Σ2) + ') =', μNUM_triangle(Σ2, D2[0], D2[1], D2[2]))
    cprint('μ(' + str(Σ2) + ') = ' + \
           str(μNUM_triangle(Σ2, D2[0], D2[1], D2[2])), color="yellow")
    Σ2_lst.append(Σ2)
    μD2_lst.append(μNUM_triangle(Σ2, D2[0], D2[1], D2[2]))


D3 = [55, 70, 85]
print(len('D3 - "хорошая":')*'-')
print('D3 - "хорошая":')
print('<a, b, c> =', D3)
Σ3_lst = []
μD3_lst = []
for Σ3 in range(D3[0], D3[2] + 1):
    # print('μ(' + str(Σ3) + ') =', μNUM_triangle(Σ3, D3[0], D3[1], D3[2]))
    cprint('μ(' + str(Σ3) + ') = ' + \
           str(μNUM_triangle(Σ3, D3[0], D3[1], D3[2])), color="yellow")
    Σ3_lst.append(Σ3)
    μD3_lst.append(μNUM_triangle(Σ3, D3[0], D3[1], D3[2]))

D4 = [80, 90, 100, 100]
print(len('D4 - "отлично":')*'-')
print('D4 - "отлично":')
print('<a, b, c> =', D4)
Σ4_lst = []
μD4_lst = []
for Σ4 in range(D4[0], D4[3] + 1):
    # print('μ(' + str(Σ4) + ') =', μNUM_trapezoid(Σ4, D4[0], D4[1], D4[2], D4[3]))
    cprint('μ(' + str(Σ4) + ') = ' + \
           str(μNUM_trapezoid(Σ4, D4[0], D4[1], D4[2], D4[3])), color="green")
    Σ4_lst.append(Σ4)
    μD4_lst.append(μNUM_trapezoid(Σ4, D4[0], D4[1], D4[2], D4[3]))

'''#
subplot(nrows, ncols, index)
nrows: int
    Количество строк.
ncols: int
    Количество столбцов.
index: int
    Местоположение элемента.'''

# Настройка размеров подложки
fig = plt.figure(figsize=(10, 5))
fig.canvas.set_window_title('Пример из 1.7.doc')

plt.subplot(2, 2, 1)
plt.title("Графики для термов переменной «гонка»")
plt.xlabel("t (мин)")
plt.ylabel("μ")
plt.ylim(0, 1.6)
plt.plot(t1_lst, μA1_lst, label='медленно', color='red')
plt.plot(t2_lst, μA2_lst, label='средне', color='orange')
plt.plot(t3_lst, μA3_lst, label='быстро', color='green')
plt.grid()
plt.legend(loc='upper right')

plt.subplot(2, 2, 2)
plt.title("Графики для термов переменной «прыжок»")
plt.xlabel("s (баллы)")
plt.ylabel("μ")
plt.ylim(0, 1.6)
plt.plot(s1_lst, μB1_lst, label='слабо', color='red')
plt.plot(s2_lst, μB2_lst, label='хорошо', color='orange')
plt.plot(s3_lst, μB3_lst, label='отлично', color='green')
plt.grid()
plt.legend(loc='upper right')

plt.subplot(2, 2, 3)
plt.title("Графики для термов переменной «сумма»")
plt.xlabel("Σ (баллы)")
plt.ylabel("μ")
plt.ylim(0, 1.9)
plt.plot(Σ1_lst, μD1_lst, label='низкая', color='red')
plt.plot(Σ2_lst, μD2_lst, label='средняя', color='orange')
plt.plot(Σ3_lst, μD3_lst, label='хорошая', color='#FFD440')
plt.plot(Σ4_lst, μD4_lst, label='отличная', color='green')
plt.grid()
plt.legend(loc='upper right')

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()
