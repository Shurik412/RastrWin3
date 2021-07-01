# -*- coding: utf-8 -*-
from openpyxl import load_workbook

file_main = r'L:\SER\Охрименко\08. БАРС\Карта ветвей от РДУ\Карта Ветвей.xlsx'

wb_main = load_workbook(file_main)
ws_main = wb_main['Лист1']

for i in range(2, 3400):
    nach2 = ws_main[f'G{i}'].value
    nach_2str = str(nach2)
    split_nach2 = ' '.join(nach_2str.split())
    ws_main[f'G{i}'] = split_nach2

wb_main.save(file_main)