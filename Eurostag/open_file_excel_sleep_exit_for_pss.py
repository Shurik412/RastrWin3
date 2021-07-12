# -*- coding: utf-8 -*-
from openpyxl import load_workbook
import win32com.client
from time import sleep


def open_file_excel(kol_file, dir_file_1, sezon_regim):
    for val_for in range(1, kol_file + 1):
        Excel = win32com.client.Dispatch("Excel.Application")
        Excel.Visible = True
        DirFileExcel = f'{dir_file_1}/{sezon_regim}_{val_for}.xlsx'
        wb_set = Excel.Workbooks.Open(DirFileExcel)
        sheet = wb_set.ActiveSheet
        val_set = sheet.Cells(11, 12).value
        val_D = val_set
        print(f'{val_for} - ValD => {val_D}')
        sleep(1)
        wb_set.Close()


open_file_excel(kol_file=57,
                dir_file_1=r'P:\RASTRWIN\12-Динамика\01-АРВ\07-Проверка АРВ\ОДУ Центра\3. ТЭЦ-26\1. Зима макс\01. EXCEL\ТГ-3 (220 кВ)',
                sezon_regim=1)

print('The End!')