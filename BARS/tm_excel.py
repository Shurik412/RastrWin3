# -*- coding: utf-8 -*-
import re
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.utils import get_column_interval, column_index_from_string
from icecream import ic


#####################################################################
def create_dop_ts(ws):
    # DIR_FILE_NAME = os.path.basename(DIR_FILE_NAME)
    STR_COLS = 'AB'
    INDEX_STR_COLS = column_index_from_string(STR_COLS)
    for row in range(2, ws.max_row):
        cell_ = ws[f'{STR_COLS}{row}'].value
        if cell_ is not None:
            try:
                list_cell = list(map(int, re.findall(r"\[(\d+)\]", cell_)))  # \[(\d+)\]'
                print(f'Data List = {list_cell}')
                for index, val_list_cell in enumerate(list_cell):
                    index_ = index + 1
                    ws[f'{str(get_column_letter(INDEX_STR_COLS + index_))}{row}'].value = val_list_cell
                    # wb.save(filename=DIR_FILE_NAME)
            except TypeError:
                print('Не соответствует типу!')


def create_list_ts(ws):
    my_list = []
    STR_COLS_TWO = 'AC'
    for row in range(2, ws.max_row):
        cell_ = ws[f'{STR_COLS_TWO}{row}'].value
        if cell_ != 0 and cell_ != 1 and cell_ != '' and cell_ is not None:
            col_index = column_index_from_string(STR_COLS_TWO)
            for col_iter in range(col_index, ws.max_column):
                cell_list = ws[f'{get_column_letter(col_iter)}{row}'].value
                my_list.append(cell_list)
    print(my_list)


#####################################################################

DIR_FILE_NAME = r'C:\Users\Ohrimenko_AG\Desktop\ТИ_Каналы.xlsx'
NAME_SHEET = '12'
try:
    wb = load_workbook(filename=DIR_FILE_NAME)
    try:
        ws = wb[NAME_SHEET]
    except KeyError:
        ws = wb.active
    create_dop_ts(ws)
    create_list_ts(ws)
    wb.save(filename=DIR_FILE_NAME)
    print('The END')
except FileNotFoundError:
    print('Файл не найден!')
