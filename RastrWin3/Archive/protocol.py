# -*- coding: utf-8 -*-
from win32com.client import Dispatch, WithEvents
from RastrWinLib.AstraRastr import RASTR


class RastrEvents:
    """
    Метод Onprot - выводит сообщения написанные: rastr.Printp("Сообщение из Printp")
    Метод OnLog
    """

    def OnLog(self, code, level, id, name, index, description, formName):
        if code == 2:
            print('[Error]', description)
        elif code == 3:
            print('[Warning]', description)
        elif code == 4:
            print('[Lightbulb]', description)
        elif code == 5:
            print('[Info]', description)
        else:
            print([code, description])

    def Onprot(self, message):
        print(message)


# RASTR = Dispatch('Astra.Rastr')
WithEvents(RASTR, RastrEvents)

if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR, RastrEvents
    from RastrWinLib.Load import load_file

    # FWDynamic = RASTR.FWDynamic()
    WithEvents(RASTR, RastrEvents)

    load_file(rastr_win=RASTR,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
              shabl='динамика')

    load_file(rastr_win=RASTR,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\КЗ на ветви.scn',
              shabl='сценарий')

    # d = Dynamic(rastr_win=RASTR)
    # d.run()
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # d.run()
