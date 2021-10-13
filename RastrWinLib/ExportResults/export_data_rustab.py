# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tools.tools import Tools


class ExportDataRUSTab:
    """
    Класс предназанчен для получения параметров после расчета ЭМПП.
    """

    def __init__(self,
                 table: str,
                 rastr_win=RASTR,
                 switch_command_line: bool = False):
        f"""
        :param table: название таблицы;
        :param rastr_win: ;
        :param switch_command_line: True/False - вывод сообщений в протокол;
        """
        self.table_name = table
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)
        self.switch_command_line = switch_command_line

    def get_array(self,
                  column: str,
                  key: str):
        """
        :param column: колонка (столбец) RastrWin3;
        :param key: выборка для получения порядкового номера ("Num=21312312");
        :return: возвращает массив параметра (column) и времени (f=Par(t));
        """
        self.table.SetSel(key)
        row_id = self.table.FindNextSel(-1)
        if row_id != (-1):
            result = self.rastr_win.GetChainedGraphSnapshot(self.table.Name, column, row_id, 0)
        else:
            result = -1
            print(f'row_id = -1.')

        if self.switch_command_line is not False:
            print(Tools.separator_noun)
            print(f'Получены результаты расчета: \n'
                  f'\t\t- из таблицы: "{self.table_name}", параметра "{column}" => "{key}"')
            print(Tools.separator_noun)
        return result


def get_array(column: str,
              key: str,
              table: str,
              rastr_win=RASTR,
              switch_command_line=False):
    """
    :param switch_command_line:
    :param rastr_win:
    :param table: таблицпа RastrWin;
    :param column: колонка (столбец) RastrWin3;
    :param key: выборка для получения порядкового номера ("Num=21312312");
    :return: возвращает массив параметра (column) и времени (f=Par(t));
    """
    table_name = table
    rastr_win = rastr_win
    table_ = rastr_win.Tables(table)
    switch_command_line = switch_command_line
    table_.SetSel(key)
    row_id = table_.FindNextSel(-1)

    if row_id != (-1):
        result_ = rastr_win.GetChainedGraphSnapshot(table_name, column, row_id, 0)
    else:
        result_ = -1

    if switch_command_line is not False:
        print(Tools.separator_noun)
        print(f'Получены результаты расчета: \n'
              f'\t\t- из таблицы: "{table_name}", параметра "{column}" => "{key}"')
        print(Tools.separator_noun)
    return result_
