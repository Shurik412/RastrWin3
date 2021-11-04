from RastrWin3.AstraRastr import RASTR
from RastrWin3.Load import LoadFile
from RastrWin3.ActionsObject.variable import Variable, FindNextSelection
from RastrWin3.ActionsObject.get import GettingParameter


load_obj = LoadFile(rastr_win=RASTR, switch_command_line=True)
load_obj.load(kod_rg=1,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\cx195.rst',
              name_shabl_russian='режим')

row = 0

var_obj = Variable(rastr_win=RASTR)

# var_obj.make_changes_row(table='vetv',
#                          column='r',
#                          row=row,
#                          value=5.02,
#                          switch_command_line=True)
#
var_obj.make_changes_vetv(table='vetv',
                          column='r',
                          ip=1, iq=6, np=0,
                          value=1.555,
                          switch_command_line=True)