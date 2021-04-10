# -*- coding: utf-8 -*-
from RastrWin.AstraRastr import RASTR
from time import time, localtime, strftime


class Equivalent:
    """
    Эквивалентирование – упрощение электрической сети
    """

    def __init__(self, rastr_win=RASTR, switch_command_line=False):
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def __bool__(self):
        return self.switch_command_line

    def ekv(self, par=""):
        if self.switch_command_line is not False:
            start_time = time()
        else:
            start_time = 0
        print(f'Запуск "Эквивалентирование режима":')
        kod = self.rastr_win.Ekv(par)
        if self.switch_command_line is not False:
            print(f'\tСообщение о результатх расчета УР: {kod}')
            if kod != 0:
                print('\t\tРежим не сбалансирован!')
            elif kod == 0:
                print('\t\tРасчет УР завершен успешно!')
        if self.switch_command_line is not False:
            time_calc = time() - start_time
            print(
                f'\tВремя расчета режима: {strftime("M: %M [минут] S: %S [секунд]", localtime(time_calc))} (Seconds: {"%.2f" % (time_calc)} [секунд])')
        return kod
