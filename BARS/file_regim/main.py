# -*- coding: utf-8 -*-
from shutil import copyfile

for num in range(1, 24):
    if num < 10:
        copyfile('00_00_00.7z', f'0{num}_00_00.7z')
    else:
        copyfile('00_00_00.7z', f'{num}_00_00.7z')

print('Работа завершена!')