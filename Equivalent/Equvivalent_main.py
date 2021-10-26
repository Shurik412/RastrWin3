# -*- coding: utf-8 -*-
from RastrWinLib.calculation.regime import SteadyState
from RastrWinLib.operation.Selection import Selection
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.calculation.equivalent import Equivalent

regimObj = SteadyState(rastr_win=RASTR,
                       switch_command_line=True)  # объект для расчета режимов
selectionObj = Selection(rastr_win=RASTR,
                         switch_command_line=True)  # объект для отключения выделений
eqvObj = Equivalent(rastr_win=RASTR,
                    switch_command_line=True)

