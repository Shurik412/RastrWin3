# -*- coding: utf-8 -*-
from prettytable import PrettyTable

from RastrWinLib.operation.Variable import FindNextSelection
from RastrWinLib.AstraRastr import RASTR


class ExportDataRUSTab(FindNextSelection):
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
        super().__init__(rastr_win=RASTR)
        self.table_name = table
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)
        self.switch_command_line = switch_command_line

    def __bool__(self):
        return self.switch_command_lin

    def get_array(self,
                  column: str,
                  key: str):
        """
        :param column: колонка (столбец) RastrWin3;
        :param key: выборка для получения порядкового номера ("Num=21312312");
        :return: возвращает массив параметра (column) и времени (f=Par(t));
        """
        # self.table.SetSel(key)
        row_id = FindNextSelection.row(self, key=key)
        if row_id != (-1):
            result = self.rastr_win.GetChainedGraphSnapshot(self.table.Name, column, row_id, 0)
        else:
            result = (-1)

        if self.switch_command_line:
            pt = PrettyTable()
            pt.title = 'Вывод результатов расчетов'
            pt.field_names = ['Таблица', 'Параметр', 'Выборка']
            pt.add_row([self.table_name, column, key])
            print(pt)
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
        pt = PrettyTable()
        pt.title = 'Вывод результатов расчетов из RUSTab'
        pt.field_names = ['Таблица', 'Параметр', 'Выборка']
        pt.add_row([self.table_name, column, key])
        print(pt)
    return result_


if __name__ == '__main__':
    from RastrWinLib.Load import load_file
    from RastrWinLib.calculation.dynamic import Dynamic
    from pandas import DataFrame
    import numpy as np
    import matplotlib.pyplot as plt

    load_file(rastr_win=RASTR,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
              shabl='сценарий',
              switch_command_line=True)

    load_file(rastr_win=RASTR,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
              shabl='динамика',
              switch_command_line=True)

    calc = Dynamic(rastr_win=RASTR,
                   calc_time=50.0,
                   snap_max_count=1,
                   switch_command_line=True)
    calc.change_calc_time()
    calc.change_snap_max_count()

    export = ExportDataRUSTab(rastr_win=RASTR, table='Generator',
                              switch_command_line=True)
    for _ in range(0, 3):
        calc.run()
        # data = (get_array(column="P", key='Num=2', table='Generator', rastr_win=RASTR, switch_command_line=False))
        data = export.get_array(column='P', key='Num=2')
        df2 = DataFrame(np.array(data), columns=['P', 't'])
        x = df2['t'].values
        y = df2['P'].values

        plt.plot(x, y)
        plt.show()
