# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
import RastrWinLib.tables.Dynamic.Generator as Generator


class SwitchGenerator:

    def __init__(self,
                 rastr_win=RASTR,
                 table: str = Generator.table,
                 switch_command_line: bool = False):
        """
        Класс включает и отключает заданный генератора.
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param table: название таблицы RastrWin3;
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        self.rastr_win = rastr_win
        self.table = table
        self.switch_command_line = switch_command_line

