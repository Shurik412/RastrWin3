from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.save import save_file
from RastrWinLib.loading.shablon import shablon_file_dynamic
from RastrWinLib.variables.variable_parametrs import Variable
from RastrWinLib.tables.tables_attributes import generator_table, generator_attributes_list

load_file(file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
          shablon=shablon_file_dynamic,
          switch_command_line=True)

var = Variable(switch_command_line=True)

var.make_changes_row(table=generator_table,
                     column=generator_attributes_list[0],
                     row_id=None,
                     value='1')

var.make_changes_row(table=generator_table,
                     column=generator_attributes_list[0],
                     row_id='0',
                     value='1')

save_file(file_path=r'C:\Users\Ohrimenko_AG\Desktop\Test_equiPy\test9_9.rst',
          shablon=shablon_file_dynamic,
          switch_command_line=True)
