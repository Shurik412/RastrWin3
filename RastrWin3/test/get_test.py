# -*- coding: utf-8 -*-
from icecream import ic

from RastrWin3.ActionsObject.get import GettingParameter
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Load import LoadFile

load = LoadFile(rastr_win=RASTR)

load.load(kod_rg=1,
          path_file=r'C:\Program Files\RastrWin3\RastrWin3\test-rastr\cx195.rg2',
          name_shabl_russian='режим')

get_ = GettingParameter(rastr_win=RASTR)

# Получение фактическое количество строк в таблице
ic(get_.get_cell_row(table='node',
                     column='ny',
                     row_id=0))

ic(type(get_.get_cell_row(table='node',
                          column='ny',
                          row_id=0)))

# Тестирование Count
ic(get_.get_count_table('node'))
ic(type(get_.get_count_table('node')))

# Тест SetSel
ic(get_.get_cell_SetSel(table='node', column='name', key='ny=805'))
ic(type(get_.get_cell_SetSel(table='node', column='name', key='ny=805')))

# Тест get_count_table_starting_zero
ic(get_.get_count_table_starting_zero(table='node'))
ic(type(get_.get_count_table_starting_zero(table='node')))

# Тест get_cell_index
ic(get_.get_cell_index(table='node', key='ny = 805'))
ic(type(get_.get_cell_index(table='node', key='ny = 805')))
