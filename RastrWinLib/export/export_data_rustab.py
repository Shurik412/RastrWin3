# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.log_tools.tools import separator_noun


class ExportDataRUSTab:
    """
    Класс предназанчен для получения параметров после расчета ЭМПП.
    """

    def __init__(self, table, rastr_win=RASTR, switch_command_line=False):
        """
        :param table: название таблицы;
        :param rastr_win: com - объект RastrWin3;
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        self.table_name = table
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)
        self.switch_command_line = switch_command_line

    def get_array(self, column, key):
        """
        :param column: колонка (столбец) RastrWin3;
        :param key: выборка для получения порядкового номера ("Num=21312312");
        :return: возвращает массив параметра (column) и времени (f=Par(t))
        """
        self.table.SetSel(key)
        row_id = self.table.FindNextSel(-1)
        if self.switch_command_line is not False:
            print(separator_noun)
            print(f'Получены результаты расчета: \n'
                  f'\t\t- из таблицы: "{self.table_name}", параметра "{column}" => "{key}"')
            print(separator_noun)
        return self.rastr_win.GetChainedGraphSnapshot(self.table.Name, column, row_id, 0)
