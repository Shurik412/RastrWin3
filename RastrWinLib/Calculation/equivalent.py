# -*- coding: utf-8 -*-

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tools.tools import separator_noun
from RastrWinLib.tools.tools import Tools


class Equivalent:
    """
    Эквивалентирование – упрощение электрической сети
    """

    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line=False):
        f"""

        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def __bool__(self):
        return self.switch_command_line

    def ekv(self, par=""):
        kod = self.rastr_win.Ekv(par)
        if self.switch_command_line is not False:
            print(Tools.separator_noun)
            print(f'Запуск "Эквивалентирование режима":')
            print(f'\tСообщение о результатх расчета УР: {kod}')
            if kod != 0:
                print('\t\tРежим не сбалансирован!')
            elif kod == 0:
                print('\t\tРасчет УР завершен успешно!')
            print(Tools.separator_noun)
        return kod
