# -*- coding: utf-8 -*-
from win32com.client import Dispatch, WithEvents, constants
from icecream import ic


# COM event handlers
class RastrEvents:
    """
    Метод Onprot - выводит сообщения написанные: rastr.Printp("Сообщение из Printp")
    Метод OnLog - выводит результаты протокола.
    """

    def OnLog(self, code, level, id, name, index, description, formName):
        print(f"[{code}] {description}")

    def Onprot(self, message):
        print(message)


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.shablon import Shabl
    from RastrWinLib.Calculation.dynamic import Dynamic

    # FWDynamic = RASTR.FWDynamic()
    # WithEvents(RASTR, RastrEvents)

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
              shabl=Shabl.shablon_file_dynamic)

    load_file(rastr_win=RASTR)

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\КЗ на ветви.scn',
              shabl=Shabl.shablon_file_scenario)

    d = Dynamic(rastr_win=RASTR)
    d.run()
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    d.run()
