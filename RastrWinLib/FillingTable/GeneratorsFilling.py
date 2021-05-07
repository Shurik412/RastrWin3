# -*- coding: utf-8 -*-

from RastrWinLib.AstraRastr import RASTR, RastrDoc
from RastrWinLib.tables.Dynamic.Generator import Generator, GeneratorsDescription
from RastrWinLib.tools.tools import Tools
from RastrWinLib.variables.variable_parametrs import Variable


def filling_generators(
        rastr_win=RASTR,
        row_id: int = None,
        sta: bool = None,
        Num: int = None,
        Name: str = None,
        Node: int = None,
        ModelType=None,
        Brand=None,
        NumBrand: int = None,
        ExciterId: int = None,
        ARSId: int = None,
        Pnom: float = None,
        Ugnom: float = None,
        cosFi: float = None,
        Demp: float = None,
        Mj: float = None,
        xd1: float = None,
        xd: float = None,
        xq: float = None,
        xd2: float = None,
        xq2: float = None,
        td01: float = None,
        td02: float = None,
        tq02: float = None,
        xq1: float = None,
        xl: float = None,
        x2: float = None,
        x0: float = None,
        tq01: float = None,
        switch_command_line: bool = False
):
    f"""
    Функция для заполнения таблицы Генераторы(ИД)
    
    :param row_id: Порядковый номер в таблице Генераторы(ИД): возвращается функцией FindNexSel;
    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param sta: Состояние генератора [S];
    :param Num: Номер генератора [N];
    :param Name: Название генератора [Название];
    :param Node: Номер узла [N узла];
    :param ModelType: Модель генератора [Модель];
    :param Brand: Марка генератора [Марка];
    :param NumBrand: Число генераторов одного типа [K_ген];
    :param ExciterId: N_возбудителя [N_взб];
    :param ARSId: N турб [N турб];
    :param Pnom: Номинальная мощность генератора [P_ном];
    :param Ugnom: Номинальное напряжение генератора [Uг_ном];
    :param cosFi: Номинальный коэффициент мощности [COS(Ф)_ном];
    :param Demp: Коэффициент демпфирования [К_демп];
    :param Mj: Механическая постоянная инерции генератора вместе с турбиной [Mj];
    :param xd1: Переходное реактивное сопротивление по продольной оси [X'd];
    :param xd: Синхронное реактивное сопротивление по продольной оси [Xd];
    :param xq: Синхронное реактивное сопротивление по поперечной оси [Xq];
    :param xd2: Сверхпереходное реактивное сопротивление по продольной оси [X"d];
    :param xq2: Сверхпереходное реактивное сопротивление по поперечной оси [X"q];
    :param td01: Переходная постоянная времени по продольной оси при разомкнутой обмотке статора [T'd0];
    :param td02: Сверхпереходная постоянная времени по продольной оси при разомкнутой обмотке статора [T"d0];
    :param tq02: Сверхпереходная постоянная времени по поперечной оси при разомкнутой обмотке статора [T"q0];
    :param xq1: Переходное реактивное сопротивление по поперечной оси [X'q];
    :param xl: Реактивное сопротивление рассеивания [X_l];
    :param x2: Реактивное сопротивление сопротивление обратной последовательности [X2];
    :param x0: Реактивное сопротивление сопротивление нулевой последовательности [X0];
    :param tq01: Переходная постоянная времени по поперечной оси при разомкнутой обмотке статора [T'q0];
    :param switch_command_line: True/False - вывод сообщений в протокол;
    :return: 
    """
    variable_ = Variable(rastr_win=rastr_win)

    # ModelType
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.ModelType,
                               row_id=row_id,
                               value=ModelType)
    # Ugnom
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.Ugnom,
                               row_id=row_id,
                               value=Ugnom)
    # cosFi
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.cosFi,
                               row_id=row_id,
                               value=cosFi)
    # Demp
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.Demp,
                               row_id=row_id,
                               value=Demp)
    # Mj
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.Mj,
                               row_id=row_id,
                               value=Mj)
    # xd1
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xd1,
                               row_id=row_id,
                               value=xd1)
    # xd
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xd,
                               row_id=row_id,
                               value=xd)
    # xq
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xq,
                               row_id=row_id,
                               value=xq)
    # xd2
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xd2,
                               row_id=row_id,
                               value=xd2)
    # xq2
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xq2,
                               row_id=row_id,
                               value=xq2)
    # td01
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.td01,
                               row_id=row_id,
                               value=td01)
    # td02
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.td02,
                               row_id=row_id,
                               value=td02)
    # tq02
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.tq02,
                               row_id=row_id,
                               value=tq02)
    # xq1
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xq1,
                               row_id=row_id,
                               value=xq1)
    # xl
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.xl,
                               row_id=row_id,
                               value=xl)
    # x2
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.x2,
                               row_id=row_id,
                               value=x2)
    # x0
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.x0,
                               row_id=row_id,
                               value=x0)
    # tq01
    variable_.make_changes_row(table=Generator.table,
                               column=Generator.tq01,
                               row_id=row_id,
                               value=tq01)
