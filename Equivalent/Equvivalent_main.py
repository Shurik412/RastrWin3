# -*- coding: utf-8 -*-
from RastrWinLib.Calculation.regime import SteadyState
from RastrWinLib.ActionsObject.Selection import Selection
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Calculation.equivalent import Equivalent

regimObj = SteadyState(rastr_win=RASTR,
                       switch_command_line=True)  # объект для расчета режимов
selectionObj = Selection(rastr_win=RASTR,
                         switch_command_line=True)  # объект для отключения выделений
eqvObj = Equivalent(rastr_win=RASTR,
                    switch_command_line=True)

