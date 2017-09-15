# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Генератор паролей v 0.21

import random
import datetime as t

text = open('passwd.txt', 'w')

alpha = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o'],
         ['p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k'],
         ['l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '2'],
         ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O'],
         ['P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K'],
         ['L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '3'],
         ['0', '1', '4', '5', '6', '7', '8', '9', '~'],
         ['`', '[', ']', '}', '{', '}', '!', '@', '#'],
         ['$', '%', '^', '&', '*', '(', ')', '_', '-']]

matr = [0, 1, 2, 3, 4, 5, 6, 7, 8]

num = input('Колличество символов: ')     # Колличество символов в пароле
colll = input('Колличество паролей: ')    # Колличество самих паролей


# Генератор по матрице
def generator():
    c = random.choice(matr)
    b = random.choice(matr)
    d = alpha[c][b]
    return d


# Генератор по колличеству символов в пароле
def coll(num):
    c = ''
    d = range(num)
    for x in d:
        h = generator()
        c = c.__add__(h)
    return c


# Генерация колличества самих паролей и добавление их в список
def genColl(colll):
    c = []
    d = range(colll)
    for x in d:
        h = coll(num)
        c.append(h)
    return c


# Пробег по списку сгенерированном функцией genColl() и вывод его на экран
for x in genColl(colll):
    ps = x
    print '| ' + str(ps) + ' | ' + str(t.datetime.today()) + ' |'
    text.write(ps + '\n')

text.close()
