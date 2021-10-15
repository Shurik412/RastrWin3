# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Tables.Node.node import Node
from RastrWinLib.loading.load import load_file
from win32com.client import Dispatch
from RastrWinLib.loading.shablon import Shabl

rast = Dispatch('Astra.Rastr')
load_file(rastr_win=rast,
          file_path='',
          shabl=Shabl.shablon_file_regime)

sb = rast.SubstServer
substId = sb.TypeIdByName("Substation")
print(substId)