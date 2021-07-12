# -*- coding: utf-8 -*-
import os

dir = fr'C:\02_26_ZimaMin'

n = 58
sezon_do = 1
sezon_posle = 3

flag1 = 0
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

flag3 = 0
if flag3 == 1:
    for i in range(1, n + 1):
        try:
            os.rename(src=fr'{dir}\{sezon_do}_{i}.nwk', dst=fr'{dir}\{sezon_posle}_{i}.nwk')
        except FileNotFoundError:
            print(f'Не найден файл {i}.')
        print(f'i={i}')


flag4 = 1
if flag4 == 1:
    for i in range(1, n + 1):
        try:
            os.rename(src=fr'{dir}\1_{i}.nwk', dst=fr'{dir}\2_{i}.nwk')
        except FileNotFoundError:
            print(f'Не найден файл {i}.')
        print(f'i = {i}')