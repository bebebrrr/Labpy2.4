#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__=='__main__':
    a = list(map(int, input().split()))
    if not a:
        print("заданный список пуст", file = sys.stderr)
        exit(1)
    # поиск индекса максимального элемента
    a_max = a[0]
    i_max = 0
    for i, item in enumerate(a):
        if item >= a_max:
            i_max, a_max = i, item
    print("Номер максимального элемента списка: ", i_max)
    # поиск индексов нулевых элементов для произведения между ними
    p = 1
    z1 = a.index(0)
    z2 = a.index(0, z1+1)
    for j in a[z1+1:z2]:
        p*=j
    print("Произведение элементов между нулевыми значениями: ", p)
    # изменение положения индексов на четные и нечетные
    nch = a[::2]
    ch = a[1::2]
    ar = nch + ch
    print("Список с измененным порядком индексов (сначала нечетные, а после четные): ", ar)
    