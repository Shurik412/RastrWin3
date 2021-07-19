# -*- coding: utf-8 -*-
from openpyxl.reader.excel import load_workbook
from openpyxl.styles.borders import Border, Side
from openpyxl import Workbook


def set_cell_range(ws, cell_range_one):
    thick = 'thick'  # жирное выделение
    thin = 'thin'  # точнкое выделение
    excretion = thin
    thin_border = Border(
        left=Side(border_style=excretion),
        right=Side(border_style=excretion),
        top=Side(border_style=excretion),
        bottom=Side(border_style=excretion)
    )
    rows = ws.iter_rows(min_row=1, max_row=10, min_col=1, max_col=10)
    for row in rows:
        for cell in row:
            cell.border = thin_border


wb = Workbook()
ws = wb.active

set_cell_range(ws=ws,
               cell_range_one='A5:C10')

# ws.cell(row=3, column=2).border = thin_border
wb.save(r'C:\Users\Ohrimenko_AG\Desktop\22.xlsx')
# set_border(ws, 'A3:C10')
