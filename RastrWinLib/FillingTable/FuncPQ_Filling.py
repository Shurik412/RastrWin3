# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Зависимость Q(P)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.FuncPQ import FuncPQ, FuncPQ_Description
from RastrWinLib.variables.variable_parametrs import Variable


def filling_FuncPQ(
        rastr_win=RASTR,
        row_id: int = None,
        Id: int = None,
        P: float = None,
        Q: float = None,
        switch_command_line: bool = False
):
    """

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице: возвращается функцией FindNexSel;
    :param Id: Номер Х-ки [N];
    :param P: P [P];
    :param Q: Q [Q];
    :param switch_command_line: True/False - вывод сообщений в протокол;
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_filling_row(table=FuncPQ.table,
                                       column=FuncPQ.Id,
                                       row_id=row_id,
                                       value=Id)

    variable_.make_changes_filling_row(table=FuncPQ.table,
                                       column=FuncPQ.P,
                                       row_id=row_id,
                                       value=P)

    variable_.make_changes_filling_row(table=FuncPQ.table,
                                       column=FuncPQ.Q,
                                       row_id=row_id,
                                       value=Q)


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.save import save_file
    from RastrWinLib.loading.shablon import Shabl
    from RastrWinLib.tables.Dynamic.FuncPQ import FuncPQ

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test.rst',
              shabl=Shabl.shablon_file_dynamic)

    table_ = RASTR.Tables(FuncPQ.table)

    for i in range(0, 100):
        table_.AddRow()
        filling_FuncPQ(
            rastr_win=RASTR,
            row_id=i,
            Id=123123123,
            P=12,
            Q=14,
            switch_command_line=False)

    save_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test_FuncPQ.rst',
              shabl=Shabl.shablon_file_dynamic)
