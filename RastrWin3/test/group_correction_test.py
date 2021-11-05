# -*- coding: utf-8 -*-
from RastrWin3.AstraRastr import RASTR
from RastrWin3.ActionsObject.selection import Selection
from RastrWin3.Load import LoadFile
from RastrWin3.Save import save_file
from RastrWin3.ActionsObject.group_correction import GroupCorr

_load = LoadFile(rastr_win=RASTR)
_load.load(path_file=r'C:\Users\Ohrimenko_AG\Desktop\cx195.rg2', name_shabl_russian='режим')

grup_obj = GroupCorr(rastr_win=RASTR)
grup_obj.calc(table='vetv', column='sel', viborka='ip=1', formula="1", switch_command_line=True)

save_file(rastr_win=RASTR,
          path_file=r'C:\Users\Ohrimenko_AG\Desktop\cx195_3.rg2',
          name_shabl_russian='режим')
