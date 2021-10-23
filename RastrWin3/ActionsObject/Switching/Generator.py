# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Tables.Dynamic.Generator import Generator
from RastrWinLib.Tools.tools import Tools


class SwitchGenerator:

    def __init__(self,
                 rastr_win=RASTR,
                 table: str = Generator.table,
                 switch_command_line: bool = False):
        f"""
        Класс включает и отключает заданный генератора.

        :param rastr_win: {Tools.RastrDoc};
        :param table: название таблицы RastrWin3;
        :param switch_command_line: {Tools.switch_command_line_doc};
        """
        self.rastr_win = rastr_win
        self.table = table
        self.switch_command_line = switch_command_line
