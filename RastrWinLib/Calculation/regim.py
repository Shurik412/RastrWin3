# -*- coding: utf-8 -*-
from time import time, localtime, strftime
from prettytable import PrettyTable
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tools.tools import Tools


class SteadyState:
    """
    Расчет режима
    """

    def __init__(self,
                 rastr_win=RASTR,
                 par='',
                 switch_command_line: bool = False):
        """
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param par: строка дополнительных параметров
            Параметры могут быть следующими:
                "" – c параметрами по умолчанию;
                "p" – расчет с плоского старта;
                "z" – отключение стартового алгоритма;
                "c" – отключение контроля данных;
                "r" – отключение подготовки данных (можно использовать при повторном расчете режима
                      с измененными значениями узловых мощностей и модулей напряжения);
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        self.rastr_win = rastr_win
        self.par = par
        self.switch_command_line = switch_command_line

    def __bool__(self):
        return self.switch_command_line

    def rgm(self):
        kod = self.rastr_win.rgm(self.par)
        if self.switch_command_line:
            self.messageResult(kod)
        return kod

    def messageResult(self, kod):
        pt = PrettyTable()
        pt.field_names = ['Описание', 'Параметр']
        pt.add_row(['Запуск "Расчет режима"', ''])
        if kod != 0:
            pt.add_row(['Сообщение о результатх расчета УР', 'Режим не сбалансирован!'])
        elif kod == 0:
            pt.add_row(['Сообщение о результатх расчета УР', 'Расчет УР завершен успешно!'])
        print(pt)
        return kod


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.shablon import Shabl

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
              shabl=Shabl.shablon_file_dynamic)
    load_file(rastr_win=RASTR)

    regim = SteadyState(rastr_win=RASTR, switch_command_line=True)
    regim.rgm()
