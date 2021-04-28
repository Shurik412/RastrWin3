from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.getting.get import get_param
from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.shablon import shablon_file_dynamic
import RastrWinLib.tables.Dynamic.ExcControl as ExcControl
from RastrWinLib.AstraRastr import RASTR

file = r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst'
load_file(file_path=file,
          shablon=shablon_file_dynamic)

# table_ = rastr_win.Tables(table)
# table_.SetSel('Id=1320')
# row_ = table_.FindNextSel(-1)
# print(row_)
# print(f'K_u={Ku}')
#
# value_cell_of_set_sel = table_.Cols(Ku).Z(row_)
#
# print(value_cell_of_set_sel)

# Ku = gett.get_cell(table=table,
#                    column=Ku,
#                    row_id=0)

# print(get_param(table=table,
#                 column=Ku,
#                 key=f'Id=1320'))
#
gett = GettingParameter()
Ku_par = get_param(table=ExcControl.table,
                   column=ExcControl.Ku,
                   key=f'Id=1320')
print(Ku_par)
print(f'{ExcControl.Id}={1320}')
Tf = get_param(table=ExcControl.table,
               column=ExcControl.Tf,
               key=f'{ExcControl.Id}={1320}')
print(f'Tf={Tf}')

# # print(Ku)
# print(f'Ku_par={Ku_par}')

# Tff = get_param(table=ExcControl.table,
#                 column=ExcControl.Tf,
#                 key=f'({ExcControl.Id}=1320)')
# t = RASTR.Tables('ExcControl')
# tt = t.Cols('Tf').Z(0)
# print(t)


# table_ = rastr_win.Tables(table)
# table_.SetSel(f'Id=1320')
# row_ = table_.FindNextSel(-1)
# print(row_)
# print(f'Ku={Ku}')
# value_cell_of_set_sel = table_.Cols(Ku).Z(row_)
# print(value_cell_of_set_sel)
