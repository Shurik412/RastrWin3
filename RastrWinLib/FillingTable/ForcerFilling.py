# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Форсировка (ИД)" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.ActionsObject.Variable import Variable


def filling_Forcer(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        CustomModel: str = None,
        Ubf: float = None,
        Uef: float = None,
        Ubrf: float = None,
        Uerf: float = None,
        Ufors: float = None,
        Rf: float = None,
        Rrf: float = None,
        Texc_f: float = None,
        Tz_in: float = None,
        Tz_out: float = None,
        Texc_rf: float = None,
        switch_command_line: bool = False
):
    """
    Функция filling_Forcer - вносит изменения в таблицу "Форсировка".

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице: возвращается функцией FindNexSel;
    :param sel: Отметка [O];
    :param sta: Состояние форсировки [S];
    :param Id: Номер форсировки [N];
    :param Name: Название форсировки [Название];
    :param ModelType: Модель форсировки [Модель];
    :param Brand: Марка форсировки [Марка];
    :param CustomModel: Модель в конструкторе [Конструктор];
    :param Ubf: Напряжение ввода форсировки [U_ввф];
    :param Uef: Напряжение снятия форсировки [U_снф];
    :param Ubrf: Напряжение ввода расфорсировки [U_вврф];
    :param Uerf: Напряжение снятия расфорсировки [U_снрф];
    :param Ufors: Выход форсировки [Ufors];
    :param Rf: Кратность форсировки [К_ф];
    :param Rrf: Кратность расфорсировки [К_рф];
    :param Texc_f: Постоянная времени возбудит. при форсировке [Т_ф];
    :param Tz_in: Задержка времени возбудит. при форсировке [Тз_ввод];
    :param Tz_out: Задержка времени возбудит. при расфорсировке [Тз_снятия];
    :param Texc_rf: Постоянная времени возбудит. при расфорсировке
    :param switch_command_line: True/False - вывод сообщений в протокол;
    :return: Noting return.
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.sel,
                                       row_id=row_id,
                                       value=sel)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.sta,
                                       row_id=row_id,
                                       value=sta)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Id,
                                       row_id=row_id,
                                       value=Id)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Name,
                                       row_id=row_id,
                                       value=Name)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.ModelType,
                                       row_id=row_id,
                                       value=ModelType)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Brand,
                                       row_id=row_id,
                                       value=Brand)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.CustomModel,
                                       row_id=row_id,
                                       value=CustomModel)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Ubf,
                                       row_id=row_id,
                                       value=Ubf)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Uef,
                                       row_id=row_id,
                                       value=Uef)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Ubrf,
                                       row_id=row_id,
                                       value=Ubrf)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Uerf,
                                       row_id=row_id,
                                       value=Uerf)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Ufors,
                                       row_id=row_id,
                                       value=Ufors)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Rf,
                                       row_id=row_id,
                                       value=Rf)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Rrf,
                                       row_id=row_id,
                                       value=Rrf)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Texc_f,
                                       row_id=row_id,
                                       value=Texc_f)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Tz_in,
                                       row_id=row_id,
                                       value=Tz_in)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Tz_out,
                                       row_id=row_id,
                                       value=Tz_out)

    variable_.make_changes_filling_row(table=Forcer.table,
                                       column=Forcer.Texc_rf,
                                       row_id=row_id,
                                       value=Texc_rf)


if __name__ == '__main__':
    from RastrWinLib.Load import load_file
    from RastrWinLib.Load.save import save_file
    from RastrWinLib.Load.shablon import Shabl
    from RastrWinLib.Tables.Dynamic.Forcer import Forcer

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test.rst',
              shabl=Shabl.shablon_file_dynamic)

    table_ = RASTR.Tables(Forcer.table)

    for i in range(0, 100):
        table_.AddRow()

        filling_Forcer(
            rastr_win=RASTR,
            row_id=i,
            sel=None,
            sta=None,
            Id=123456789,
            Name=f'Генератор {i}',
            ModelType=None,
            Brand=None,
            CustomModel=None,
            Ubf=0.123456789,
            Uef=123456789,
            Ubrf=123456789,
            Uerf=123456789,
            Ufors=123456789,
            Rf=123456789,
            Rrf=123456789,
            Texc_f=123456789,
            Tz_in=123456789,
            Tz_out=123456789,
            Texc_rf=123456789,
            switch_command_line=False)

    save_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test_Forcer.rst',
              shabl=Shabl.shablon_file_dynamic)
