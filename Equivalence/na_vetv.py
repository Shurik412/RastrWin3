# -*- coding: utf-8 -*-
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.save import save_file
from RastrWinLib.loading.shablon import shablon_file_regime
from RastrWinLib.tables.tables_attributes import vetv_table, node_table
from RastrWinLib.variables.variable_parametrs import Variable

load_file(file_path=r'C:\Users\Ohrimenko_AG\Desktop\Test_equiPy\02-БРМ Зима максимум [уст].rg2',
          shablon=shablon_file_regime,
          switch_command_line=True)

get_ = GettingParameter()
variable_ = Variable()
for i in range(0, 26558):
    ip = get_.get_cell(table=vetv_table,
                       column='ip',
                       row_id=i)
    row_ny = get_.get_row_node(node_ny=ip)
    na_node = get_.get_cell(table=node_table,
                            column='na',
                            row_id=row_ny)

    variable_.make_changes_row(table=vetv_table,
                               column='na',
                               row_id=i,
                               value=na_node)

save_file(file_path=r'C:\Users\Ohrimenko_AG\Desktop\Test_equiPy\test_123.rg2',
          shablon=shablon_file_regime)
