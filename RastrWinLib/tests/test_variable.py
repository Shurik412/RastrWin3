from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.save import save_file
from RastrWinLib.tables.Dynamic.Generator import Generator, GeneratorsDescription
from RastrWinLib.variables.variable_parametrs import Variable
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.loading.shablon import Shabl

load_file(file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
          shabl=Shabl.shablon_file_dynamic,
          switch_command_line=True)

var_ = Variable(switch_command_line=True)
get_ = GettingParameter()
xd11 = get_.get_cell_row(table=Generator.table,
                         column=Generator.xd1,
                         row_id=1)
var_.make_changes_row(table=Generator.table,
                      column=Generator.xd1,
                      row_id=1,
                      value=0.5)

xd1 = get_.get_cell_row(table=Generator.table,
                        column=Generator.xd1,
                        row_id=1)
print(f'xd11={xd11}')
print(f'xd1={xd1}')

save_file(file_path=r'C:\Users\Ohrimenko_AG\Desktop\ForTest\test9.rst',
          shabl=Shabl.shablon_file_dynamic,
          switch_command_line=True)
