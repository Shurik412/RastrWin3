# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "АРС (ИД)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.Governor import Governor
from RastrWinLib.variables.variable_parametrs import Variable


def filling_Governor(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        CustomModel: str = None,
        Brand: str or int = None,
        strs: float = None,
        zn: float = None,
        Tr: float = None,
        otmax: float = None,
        otmin: float = None,
        CVmin: float = None,
        CVmax: float = None,
        T1: float = None,
        K1: float = None,
        K2: float = None,
        BoilerId: int = None,
        switch_command_line: bool = False
):
    """
    Функция filling_Governor - вносит изменения в таблицу "Регулятор скорости".

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице: возвращается функцией FindNexSel;
    :param sel: Отметка [O];
    :param sta: Состояние регулятора скорости;
    :param Id: Номер регулятора скорости [N арс];
    :param Name: Название регулятора скорости [Название];
    :param ModelType: Модель регулятора скорости [Модель];
    :param CustomModel: Модель в конструкторе [Конструктор];
    :param Brand: Марка регулятора скорости [Марка];
    :param strs: Статизм регулятора скорости турбины [Статизм];
    :param zn: Зона нечувствительности [З_неч];
    :param Tr: Постоянная времени регулятора [Трег];
    :param otmax: Максимальная мощность турбины [Pt_max];
    :param otmin: Минимальная мощность турбины [Pt_min];
    :param CVmin: Минимальная скорость перемещения клапана [CVmin];
    :param CVmax: Максимальная скорость перемещения клапана [CVmax];
    :param T1: Постоянная ОС [Т1];
    :param K1: K1 ОС [K1];
    :param K2: K2 ОС [K2];
    :param BoilerId: Номер котла [N котла];
    :param switch_command_line: True/False - вывод сообщений в протокол;
    :return: Noting return.
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.sel,
                                       row_id=row_id,
                                       value=sel)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.sta,
                                       row_id=row_id,
                                       value=sta)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.Id,
                                       row_id=row_id,
                                       value=Id)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.Name,
                                       row_id=row_id,
                                       value=Name)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.ModelType,
                                       row_id=row_id,
                                       value=ModelType)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.CustomModel,
                                       row_id=row_id,
                                       value=CustomModel)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.Brand,
                                       row_id=row_id,
                                       value=Brand)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.strs,
                                       row_id=row_id,
                                       value=strs)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.zn,
                                       row_id=row_id,
                                       value=zn)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.Tr,
                                       row_id=row_id,
                                       value=Tr)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.otmax,
                                       row_id=row_id,
                                       value=otmax)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.otmin,
                                       row_id=row_id,
                                       value=otmin)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.CVmin,
                                       row_id=row_id,
                                       value=CVmin)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.CVmax,
                                       row_id=row_id,
                                       value=CVmax)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.T1,
                                       row_id=row_id,
                                       value=T1)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.K1,
                                       row_id=row_id,
                                       value=K1)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.K2,
                                       row_id=row_id,
                                       value=K2)

    variable_.make_changes_filling_row(table=Governor.table,
                                       column=Governor.BoilerId,
                                       row_id=row_id,
                                       value=BoilerId)


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.save import save_file
    from RastrWinLib.loading.shablon import Shabl
    from RastrWinLib.tables.Dynamic.Governor import Governor

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test.rst',
              shabl=Shabl.shablon_file_dynamic)

    table_ = RASTR.Tables(Governor.table)

    for i in range(0, 100):
        table_.AddRow()

        filling_Governor(
            rastr_win=RASTR,
            row_id=i,
            sel=None,
            sta=None,
            Id=123456789,
            Name=f'Генератор {i}',
            ModelType=None,
            CustomModel=None,
            Brand=None,
            strs=0.123,
            zn=0.123,
            Tr=0.123,
            otmax=0.123,
            otmin=0.123,
            CVmin=0.123,
            CVmax=0.123,
            T1=0.123,
            K1=0.123,
            K2=0.123,
            BoilerId=123456789,
            switch_command_line=False)

    save_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test_Governor.rst',
              shabl=Shabl.shablon_file_dynamic)
