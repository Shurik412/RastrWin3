# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Стабилизаторы IEEE 1-3" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.ActionsObject.Variable import Variable


def filling_DFWIEEE421PSS13(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        CustomModel: str = None,
        Input1Type: str = None,
        Input2Type: str = None,
        Ks1: float = None,
        Ks2: float = None,
        Ks3: float = None,
        T1: float = None,
        T2: float = None,
        T3: float = None,
        T4: float = None,
        T5: float = None,
        T6: float = None,
        T7: float = None,
        T8: float = None,
        T9: float = None,
        T10: float = None,
        T11: float = None,
        T12: float = None,
        T13: float = None,
        Tw1: float = None,
        Tw2: float = None,
        Tw3: float = None,
        Tw4: float = None,
        A1: float = None,
        A2: float = None,
        A3: float = None,
        A4: float = None,
        A5: float = None,
        A6: float = None,
        A7: float = None,
        A8: float = None,
        M: float = None,
        N: float = None,
        Vstmax: float = None,
        Vstmin: float = None,
        Vsi1max: float = None,
        Vsi1min: float = None,
        Vsi2max: float = None,
        Vsi2min: float = None,
        switch_command_line: bool = False):
    """
    Функция filling_DFWIEEE421PSS13 - вносит изменения в таблицу "Стабилизатор IEEE 1-3".

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице: возвращается функцией FindNexSel;
    :param sel: Отметка [O];
    :param sta: Состояние стабилизатора [S];
    :param Id: Номер стабилизатора [N стаб];
    :param Name: Название стабилизатора [Название];
    :param ModelType: Модель стабилизатора [Модель];
    :param Brand: Марка стабилизатора [Марка];
    :param CustomModel: Модель в конструкторе [Конструктор];
    :param Input1Type: Тип параметра на входе 1 [Вход 1];
    :param Input2Type: Тип параметра на входе 2 [Вход 2];
    :param Ks1: Ks1 [Ks1];
    :param Ks2: Ks2 [Ks2];
    :param Ks3: Ks3 [Ks3];
    :param T1: T1 [T1];
    :param T2: T2 [T2];
    :param T3: T3 [T3];
    :param T4: T4 [T4];
    :param T5: T5 [T5];
    :param T6: T6 [T6];
    :param T7: T7 [T7];
    :param T8: T8 [T8];
    :param T9: T9 [T9];
    :param T10: T10 [T10];
    :param T11: T11 [T11];
    :param T12: T12 [T12];
    :param T13: T13 [T13];
    :param Tw1: Tw1 [Tw1];
    :param Tw2: Tw2 [Tw2];
    :param Tw3: Tw3 [Tw3];
    :param Tw4: Tw4 [Tw4];
    :param A1: A1 [A1];
    :param A2: A2 [A2];
    :param A3: A3 [A3];
    :param A4: A4 [A4];
    :param A5: A5 [A5];
    :param A6: A6 [A6];
    :param A7: A7 [A7];
    :param A8: A8 [A8];
    :param M: M [M];
    :param N: N [N];
    :param Vstmax: Максимальное ограничение выхода стабилизатора [Vstmax];
    :param Vstmin: Минимальное ограничение выхода стабилизатора [Vstmin];
    :param Vsi1max: Максимальное ограничение 1-го входа стабилизатора [Vsi1max];
    :param Vsi1min: Минимальное ограничение 1-го входа стабилизатора [Vsi1min];
    :param Vsi2max: Максимальное ограничение 2-го входа стабилизатора [Vsi2max];
    :param Vsi2min: Минимальное ограничение 2-го входа стабилизатора [Vsi2min];
    :param switch_command_line: True/False - вывод сообщений в протокол;
    :return: Noting return.
    """
    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.sel,
                                       row_id=row_id,
                                       value=sel)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.sta,
                                       row_id=row_id,
                                       value=sta)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Id,
                                       row_id=row_id,
                                       value=Id)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Name,
                                       row_id=row_id,
                                       value=Name)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.ModelType,
                                       row_id=row_id,
                                       value=ModelType)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Brand,
                                       row_id=row_id,
                                       value=Brand)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.CustomModel,
                                       row_id=row_id,
                                       value=CustomModel)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Input1Type,
                                       row_id=row_id,
                                       value=Input1Type)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Input2Type,
                                       row_id=row_id,
                                       value=Input2Type)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Ks1,
                                       row_id=row_id,
                                       value=Ks1)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Ks2,
                                       row_id=row_id,
                                       value=Ks2)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Ks3,
                                       row_id=row_id,
                                       value=Ks3)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T1,
                                       row_id=row_id,
                                       value=T1)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T2,
                                       row_id=row_id,
                                       value=T2)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T3,
                                       row_id=row_id,
                                       value=T3)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T4,
                                       row_id=row_id,
                                       value=T4)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T5,
                                       row_id=row_id,
                                       value=T5)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T6,
                                       row_id=row_id,
                                       value=T6)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T7,
                                       row_id=row_id,
                                       value=T7)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T8,
                                       row_id=row_id,
                                       value=T8)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T9,
                                       row_id=row_id,
                                       value=T9)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T10,
                                       row_id=row_id,
                                       value=T10)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T11,
                                       row_id=row_id,
                                       value=T11)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T12,
                                       row_id=row_id,
                                       value=T12)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.T13,
                                       row_id=row_id,
                                       value=T13)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Tw1,
                                       row_id=row_id,
                                       value=Tw1)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Tw2,
                                       row_id=row_id,
                                       value=Tw2)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Tw3,
                                       row_id=row_id,
                                       value=Tw3)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Tw4,
                                       row_id=row_id,
                                       value=Tw4)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.A1,
                                       row_id=row_id,
                                       value=A1)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.A2,
                                       row_id=row_id,
                                       value=A2)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.A3,
                                       row_id=row_id,
                                       value=A3)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.A4,
                                       row_id=row_id,
                                       value=A4)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.A5,
                                       row_id=row_id,
                                       value=A5)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.A6,
                                       row_id=row_id,
                                       value=A6)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.A7,
                                       row_id=row_id,
                                       value=A7)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.A8,
                                       row_id=row_id,
                                       value=A8)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.M,
                                       row_id=row_id,
                                       value=M)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.N,
                                       row_id=row_id,
                                       value=N)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Vstmax,
                                       row_id=row_id,
                                       value=Vstmax)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Vstmin,
                                       row_id=row_id,
                                       value=Vstmin)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Vsi1max,
                                       row_id=row_id,
                                       value=Vsi1max)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Vsi1min,
                                       row_id=row_id,
                                       value=Vsi1min)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Vsi2max,
                                       row_id=row_id,
                                       value=Vsi2max)

    variable_.make_changes_filling_row(table=DFWIEEE421PSS13.table,
                                       column=DFWIEEE421PSS13.Vsi2min,
                                       row_id=row_id,
                                       value=Vsi2min)


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.Load import load_file
    from RastrWinLib.Load.save import save_file
    from RastrWinLib.Load.shablon import Shabl
    from RastrWinLib.Tables.Dynamic.DFWIEEE421PSS13 import DFWIEEE421PSS13

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test.rst',
              shabl=Shabl.shablon_file_dynamic)

    load_file(rastr_win=RASTR,
              file_path=r'',
              shabl=Shabl.shablon_file_automation)

    table_ = RASTR.Tables(DFWIEEE421PSS13.table)

    for i in range(0, 10):
        table_.AddRow()

        filling_DFWIEEE421PSS13(
            rastr_win=RASTR,
            row_id=i,
            sel=None,
            sta=None,
            Id=123456789,
            Name=f'Генератор {i}',
            ModelType=None,
            Brand=None,
            CustomModel=None,
            Input1Type=None,
            Input2Type=None,
            Ks1=0.123456,
            Ks2=0.123456,
            Ks3=0.123456,
            T1=0.123456,
            T2=0.123456,
            T3=0.123456,
            T4=0.123456,
            T5=0.123456,
            T6=0.123456,
            T7=0.123456,
            T8=0.123456,
            T9=0.123456,
            T10=0.123456,
            T11=0.123456,
            T12=0.123456,
            T13=0.123456,
            Tw1=0.123456,
            Tw2=0.123456,
            Tw3=0.123456,
            Tw4=0.123456,
            A1=0.123456,
            A2=0.123456,
            A3=0.123456,
            A4=0.123456,
            A5=0.123456,
            A6=0.123456,
            A7=0.123456,
            A8=0.123456,
            M=0.123456,
            N=0.123456,
            Vstmax=0.123456,
            Vstmin=0.123456,
            Vsi1max=0.123456,
            Vsi1min=0.123456,
            Vsi2max=0.123456,
            Vsi2min=0.123456,
            switch_command_line=False)

    RASTR.rgm('')
    save_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test_DFWIEEE421PSS13.rst',
              shabl=Shabl.shablon_file_dynamic)
