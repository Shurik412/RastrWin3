# -*- coding: utf-8 -*-
from RastrWinLib.Load import load_file
from win32com.client import Dispatch
from RastrWinLib.Load.shablon import Shabl

rast = Dispatch('Astra.Rastr')
load_file(rastr_win=rast,
          path_file='',
          shabl=Shabl.shablon_file_regime)

sb = rast.SubstServer
substId = sb.TypeIdByName("Substation")
print(substId)