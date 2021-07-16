# -*- coding: utf-8 -*-
import re
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.utils import get_column_interval, column_index_from_string

DIR_FILE_NAME = r'U:\ODU_DIR\СЭР\БАРС\TM.xlsx'
# DIR_FILE_NAME = os.path.basename(DIR_FILE_NAME)
NAME_SHEET = '12'
STR_COLS = 'AB'
#####################################################################
wb = load_workbook(filename=DIR_FILE_NAME)
ws = wb[NAME_SHEET]
INDEX_STR_COLS = column_index_from_string(STR_COLS)
for row in range(2, ws.max_row):
    cell_ = ws[f'{STR_COLS}{row}'].value
    if cell_ is not None:
        list_cell = list(map(int, re.findall(r"\[(\d+)\]", cell_)))  # \[(\d+)\]'
        print(f'Data List = {list_cell}')
        for index, val_list_cell in enumerate(list_cell):
            index_ = index + 1
            ws[f'{str(get_column_letter(INDEX_STR_COLS + index_))}{row}'].value = val_list_cell
            wb.save(filename=DIR_FILE_NAME)
wb.save(filename=DIR_FILE_NAME)
print('The END')
