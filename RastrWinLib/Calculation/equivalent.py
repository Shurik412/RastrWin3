# -*- coding: utf-8 -*-
from prettytable import PrettyTable

from RastrWinLib.AstraRastr import RASTR


class Equivalent:
    """
    Эквивалентирование – упрощение электрической сети
    """

    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line: bool = False):
        f"""
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def __bool__(self):
        return self.switch_command_line

    def ekv(self, par: str = ""):
        kod = self.rastr_win.Ekv(par)
        if self.switch_command_line:
            self.messageResult(kod)
        return kod

    def messageResult(self, kod):
        pt = PrettyTable()
        pt.field_names = ['Описание', 'Параметр']
        pt.add_row(['Запуск "Эквивалентирование режима', ''])
        if kod != 0:
            pt.add_row(['Сообщение о результатх расчета УР', 'Режим не сбалансирован!'])
        elif kod == 0:
            pt.add_row(['Сообщение о результатх расчета УР', 'Расчет УР завершен успешно!'])
        print(pt.get_string(title="Эквивалентирование"))
        return kod
