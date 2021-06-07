# -*- coding: utf-8 -*-
import os

dir = fr'L:\SER\Охрименко\06. АРВ\7. Московское РДУ\ТЭЦ-20\ТГ-11Б ТЭЦ-20\exp'

n = 100
flag1 = 1
if flag1 == 1:
    for i in range(1, n + 1):
        try:
            os.rename(src=fr'{dir}\{i}N.expp', dst=fr'{dir}\1_{i}_N_220kV.exp')
            os.rename(src=fr'{dir}\{i}Y.expp', dst=fr'{dir}\1_{i}_Y_220kV.exp')
        except FileNotFoundError:
            print(f'Не найден файл {i}.')
        print(f'i = {i}')

flag2 = 0
if flag2 == 1:
    for i in range(1, n + 1):
        try:
            os.rename(src=fr'{dir}\1_{i}_N_220kV.expp', dst=fr'{dir}\1_{i}_N_220kV.exp')
            os.rename(src=fr'{dir}\1_{i}_Y_220kV.expp', dst=fr'{dir}\1_{i}_Y_220kV.exp')
        except FileNotFoundError:
            print(f'Не найден файл {i}.')
        print(f'i = {i}')
