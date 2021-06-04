# -*- coding: utf-8 -*-
import os

dir = fr'L:\SER\Охрименко\06. АРВ\Москва\2\expp'

n = 100
flag1 = 0
if flag1 == 1:
    for i in range(1, n + 1):
        try:
            os.rename(src=fr'{dir}\{i}N.expp', dst=fr'{dir}\1_{i}_N_220kV.exp')
            os.rename(src=fr'{dir}\{i}Y.expp', dst=fr'{dir}\1_{i}_Y_220kV.exp')
        except FileNotFoundError:
            print(f'Не найден файл {i}.')
        print(f'i = {i}')

flag2 = 1
if flag2 == 1:
    for i in range(1, n + 1):
        try:
            os.rename(src=fr'{dir}\1_{i}_N_220kV.expp', dst=fr'{dir}\1_{i}_N_220kV.exp')
            os.rename(src=fr'{dir}\1_{i}_Y_220kV.expp', dst=fr'{dir}\1_{i}_Y_220kV.exp')
        except FileNotFoundError:
            print(f'Не найден файл {i}.')
        print(f'i = {i}')
