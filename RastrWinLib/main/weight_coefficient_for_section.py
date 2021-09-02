# -*- coding: utf-8 -*-
from RastrWinLib.calculation.regim import SteadyState
from RastrWinLib.tables.area.area import Area
from RastrWinLib.selection.selection import Selection
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.calculation.equivalent import Equivalent

regimObj = SteadyState(rastr_win=RASTR,
                       switch_command_line=True)  # объект для расчета режимов
selectionObj = Selection(rastr_win=RASTR,
                         switch_command_line=True)  # объект для отключения выделений
eqvObj = Equivalent(rastr_win=RASTR,
                    switch_command_line=True)

