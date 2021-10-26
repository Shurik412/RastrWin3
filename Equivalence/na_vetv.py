# -*- coding: utf-8 -*-
from RastrWinLib.operation.Get import GettingParameter
from RastrWinLib.Load import load_file
from RastrWinLib.Load.save import save_file
from RastrWinLib.Load.shablon import Shabl
from RastrWinLib.Tables.tables_attributes import vetv_table, node_table
from RastrWinLib.operation.Variable import Variable

load_file(file_path=r'C:\Users\Ohrimenko_AG\Desktop\Test_equiPy\02-БРМ Зима максимум [уст].rg2',
          shabl=Shabl.shablon_file_regime, switch_command_line=True)

get_ = GettingParameter()
variable_ = Variable()
for i in range(0, 26558):
    ip = get_.get_cell(table=vetv_table,
                       column='ip',
                       row_id=i)

    iq = get_.get_cell(table=vetv_table,
                       column='iq',
                       row_id=i)

    row_ny_ip = get_.get_row_node(node_ny=ip)
    row_ny_iq = get_.get_row_node(node_ny=iq)

    na_ip = get_.get_cell(table=node_table,
                          column='na',
                          row_id=row_ny_ip)

    na_iq = get_.get_cell(table=node_table,
                          column='na',
                          row_id=row_ny_iq)

    if na_ip == na_iq:
        print(f'na_ip={na_ip} == na_iq={na_iq}')
        variable_.make_changes_row(table=vetv_table,
                                   column='na',
                                   row_id=i,
                                   value=na_ip)
    else:
        print(f'ERROR: na_ip={na_ip} != na_iq={na_iq}')

save_file(file_path=r'C:\Users\Ohrimenko_AG\Desktop\Test_equiPy\test_123.rg2', shabl=Shabl.shablon_file_regime)
