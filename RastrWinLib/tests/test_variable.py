from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.save import save_file
from RastrWinLib.tables.Dynamic.Generator import Generator, GeneratorsDescription
from RastrWinLib.variables.variable_parametrs import Variable
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.loading.shablon import Shabl
from RastrWinLib.AstraRastr import RASTR

load_file(file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
          shabl=Shabl.shablon_file_dynamic,
          switch_command_line=True, rastr_win=RASTR)

# var_ = Variable(switch_command_line=True)
# get_ = GettingParameter()
# xd11 = get_.get_cell_row(table=Generator.table,
#                          column=Generator.sel,
#                          row_id=1)
# var_.make_changes_row(table=Generator.table,
#                       column=Generator.sel,
#                       row_id=1,
#                       value=None)
#
# xd1 = get_.get_cell_row(table=Generator.table,
#                         column=Generator.sel,
#                         row_id=1)
# print(f'xd11={xd11}')
# print(f'xd1={xd1}')
#
# save_file(file_path=r'C:\Users\Ohrimenko_AG\Desktop\ForTest\test9.rst',
#           shabl=Shabl.shablon_file_dynamic,
#           switch_command_line=True)
list_ = []
for i in range(0, RASTR.Tables.Count-1):
    j = RASTR.Tables(i).Name
    list_.append(j)
    print(list_)

list_2 = []
for i in range(0, 5):
    g = RASTR.Tav