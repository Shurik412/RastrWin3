# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
import RastrWinLib.tables.vetv as vetv
import RastrWinLib.tables.node as node
import RastrWinLib.tables.Generator as Generator


class Error:

    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line: bool = False):
        """

        :param rastr_win: com - объект RastrWin3;
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def name_is_not_table(self,
                          table: str = None):
        """

        :param table: название таблицы.
        """

        print(
            f''
        )
