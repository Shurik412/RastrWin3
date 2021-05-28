# -*- coding: utf-8 -*-
import os

dir = fr'C:\Users\Ohrimenko_AG\Desktop\expp'

n = 100

for i in range(1, n + 1):
    try:
        os.rename(src=fr'{dir}\{i}N.expp', dst=fr'{dir}\1_{i}_N_220kV.exp')
        os.rename(src=fr'{dir}\{i}Y.expp', dst=fr'{dir}\1_{i}_Y_220kV.exp')
    except FileNotFoundError:
        print(f'Не найден файл {i}.')
    print(f'i = {i}')
