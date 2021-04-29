# -*- coding: utf-8 -*-
# Модель автоматического регулятора возбуждения типа ARV-REM, реализованная в ПК RUSTab, состоит из одного макроблока:
#   1.АРВ: ARV-REM.xmldev (таблица 11).
# Параметры модели ARV-REM.xmldev заносятся в таблицу «АРВ (ИД)».
# Модель автоматического регулятора возбуждения типа ARV-REM, реализованная в ПК RUSTab, состоит из одного макроблока:
#   1.АРВ: ARV-REM.xmldev (таблица 11).
# Параметры модели ARV-REM.xmldev заносятся в таблицу «АРВ (ИД)».
from RastrWinLib.tables.Dynamic.ExcControl import ExcControl


class Parameters:
    """

    """
    Ku: float = 5  # Коэффициент усиления пропорционального канала регулятора напряжения 5...200
    Trv: float = 0.1  # Постоянная времени регулятора 0.1 ... 5
    Ku1: float = 1  # Коэффициент усиления канала по производной напряжения 0 ... 10
    Kif1: float = 1  # Коэффициент усиления канала по производной тока ротора 0 ... 5
    Kf: float = 1  # Коэффициент усиления канала по частоте  0 ... 15
    Kf1: float = 1  # Коэффициент усиления канала по производной частоты 0 ... 7.5


def change_parameters_ARV_REM(
        Id=None,
        row_id=None,
        Ku=Parameters.Ku,
        Trv=Parameters.Trv,
        Ku1=Parameters.Ku1,
        Kif1=Parameters.Kif1,
        Kf=Parameters.Kf,
        Kf1=Parameters.Kf1,
        rastr_win=RASTR,
        switch_command_line: bool = False):
    """

    :param Id: номер возбудителя;
    :param row_id: порядковый номер в таблице (от 0 до [max.count]);
    :param Ku:
    :param Trv:
    :param Ku1:
    :param Kif1:
    :param Kf:
    :param Kf1:
    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param switch_command_line: True/False - вывод сообщений в протакол;
    :return:
    """

    variable_ = Variable(rastr_win=rastr_win)
    get_ = GettingParameter(rastr_win=rastr_win)

    if Id is not None and row_id is None:
        # Ku
        if switch_command_line is not None:
            ku_before = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Ku,
                                         Id=Id)
        else:
            ku_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Ku,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Ku)

        if switch_command_line is not None:
            ku_after = get_.get_cell_id(table=ExcControl.table,
                                        column=ExcControl.Ku,
                                        Id=Id)
        else:
            ku_after = None

        # Trv
        if switch_command_line is not None:
            trv_before = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.Trv,
                                          Id=Id)
        else:
            trv_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Trv,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Trv)

        if switch_command_line is not None:
            trv_after = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Trv,
                                         Id=Id)
        else:
            trv_after = None

        # Ku1
        if switch_command_line is not None:
            ku1_before = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.Ku1,
                                          Id=Id)
        else:
            ku1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Ku1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Ku1)

        if switch_command_line is not None:
            ku1_after = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Ku1,
                                         Id=Id)
        else:
            ku1_after = None

        # Kif1
        if switch_command_line is not None:
            kif1_before = get_.get_cell_id(table=ExcControl.table,
                                           column=ExcControl.Kif1,
                                           Id=Id)
        else:
            kif1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kif1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kif1)

        if switch_command_line is not None:
            kif1_after = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.Kif1,
                                          Id=Id)
        else:
            kif1_after = None

        # Kf
        if switch_command_line is not None:
            kf_before = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Kf,
                                         Id=Id)
        else:
            kf_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf)

        if switch_command_line is not None:
            kf_after = get_.get_cell_id(table=ExcControl.table,
                                        column=ExcControl.Kf,
                                        Id=Id)
        else:
            kf_after = None

        # Kf1
        if switch_command_line is not None:
            kf1_before = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.Kf1,
                                          Id=Id)
        else:
            kf1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf1)

        if switch_command_line is not None:
            kf1_after = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Kf1,
                                         Id=Id)
        else:
            kf1_after = None
