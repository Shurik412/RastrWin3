# -*- coding: utf-8 -*-
# Модель автоматического регулятора возбуждения типа ARV-REM, реализованная в ПК RUSTab, состоит из одного макроблока:
#   1.АРВ: ARV-REM.xmldev (таблица 11).
# Параметры модели ARV-REM.xmldev заносятся в таблицу «АРВ (ИД)».
# Модель автоматического регулятора возбуждения типа ARV-REM, реализованная в ПК RUSTab, состоит из одного макроблока:
#   1.АРВ: ARV-REM.xmldev (таблица 11).
# Параметры модели ARV-REM.xmldev заносятся в таблицу «АРВ (ИД)».
from RastrWinLib.ActionsObject.Get import GettingParameter
from RastrWinLib.Tables.Dynamic.ExcControl import ExcControl
from RastrWinLib.ActionsObject.Variable import Variable


class Parameters:
    """
    Модель автоматического регулятора возбуждения типа ARV-REM, реализованная в ПК RUSTab, состоит из одного макроблока:
    1.АРВ: ARV-REM.xmldev (таблица 11).
    Параметры модели ARV-REM.xmldev заносятся в таблицу «АРВ (ИД)».
    Модель автоматического регулятора возбуждения типа ARV-REM, реализованная в ПК RUSTab, состоит из одного макроблока:
    1.АРВ: ARV-REM.xmldev (таблица 11).
    Параметры модели ARV-REM.xmldev заносятся в таблицу «АРВ (ИД)».
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
    :param Ku: Коэффициент усиления пропорционального канала регулятора напряжения 5...200
    :param Trv: Постоянная времени регулятора 0.1 ... 5
    :param Ku1: Коэффициент усиления канала по производной напряжения 0 ... 10
    :param Kif1: Коэффициент усиления канала по производной тока ротора 0 ... 5
    :param Kf: Коэффициент усиления канала по частоте  0 ... 15
    :param Kf1: Коэффициент усиления канала по производной частоты 0 ... 7.5
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

    elif row_id is not None and Id is None:
        # Ku
        if switch_command_line is not None:
            ku_before = get_.get_cell_row(table=ExcControl.table,
                                          column=ExcControl.Ku,
                                          row_id=row_id)
        else:
            ku_before = None

        variable_.make_changes_row(table=ExcControl.table,
                                   column=ExcControl.Ku,
                                   row_id=row_id,
                                   value=Ku)

        if switch_command_line is not None:
            ku_after = get_.get_cell_id(table=ExcControl.table,
                                        column=ExcControl.Ku,
                                        Id=Id)
        else:
            ku_after = None

        # Trv
        if switch_command_line is not None:
            trv_before = get_.get_cell_row(table=ExcControl.table,
                                           column=ExcControl.Trv,
                                           row_id=row_id)
        else:
            trv_before = None

        variable_.make_changes_row(table=ExcControl.table,
                                   column=ExcControl.Trv,
                                   row_id=row_id,
                                   value=Trv)

        if switch_command_line is not None:
            trv_after = get_.get_cell_row(table=ExcControl.table,
                                          column=ExcControl.Trv,
                                          row_id=row_id)
        else:
            trv_after = None

        # Ku1
        if switch_command_line is not None:
            ku1_before = get_.get_cell_row(table=ExcControl.table,
                                           column=ExcControl.Ku1,
                                           row_id=row_id)
        else:
            ku1_before = None

        variable_.make_changes_row(table=ExcControl.table,
                                   column=ExcControl.Ku1,
                                   row_id=row_id,
                                   value=Ku1)

        if switch_command_line is not None:
            ku1_after = get_.get_cell_row(table=ExcControl.table,
                                          column=ExcControl.Ku1,
                                          row_id=row_id)
        else:
            ku1_after = None

        # Kif1
        if switch_command_line is not None:
            kif1_before = get_.get_cell_row(table=ExcControl.table,
                                            column=ExcControl.Kif1,
                                            row_id=row_id)
        else:
            kif1_before = None

        variable_.make_changes_row(table=ExcControl.table,
                                   column=ExcControl.Kif1,
                                   row_id=row_id,
                                   value=Kif1)

        if switch_command_line is not None:
            kif1_after = get_.get_cell_row(table=ExcControl.table,
                                           column=ExcControl.Kif1,
                                           row_id=row_id)
        else:
            kif1_after = None

        # Kf
        if switch_command_line is not None:
            kf_before = get_.get_cell_row(table=ExcControl.table,
                                          column=ExcControl.Kf,
                                          row_id=row_id)
        else:
            kf_before = None

        variable_.make_changes_row(table=ExcControl.table,
                                   column=ExcControl.Kf,
                                   row_id=row_id,
                                   value=Kf)

        if switch_command_line is not None:
            kf_after = get_.get_cell_row(table=ExcControl.table,
                                         column=ExcControl.Kf,
                                         row_id=row_id)
        else:
            kf_after = None

        # Kf1
        if switch_command_line is not None:
            kf1_before = get_.get_cell_row(table=ExcControl.table,
                                           column=ExcControl.Kf1,
                                           row_id=row_id)
        else:
            kf1_before = None

        variable_.make_changes_row(table=ExcControl.table,
                                   column=ExcControl.Kf1,
                                   row_id=row_id,
                                   value=Kf1)

        if switch_command_line is not None:
            kf1_after = get_.get_cell_row(table=ExcControl.table,
                                          column=ExcControl.Kf1,
                                          row_id=row_id)
        else:
            kf1_after = None

    else:
        Id = None
        row_id = None
        ku_before, ku_after = None, None
        trv_before, trv_after = None, None
        ku1_before, ku1_after = None, None
        kif1_before, kif1_after = None, None
        kf_before, kf_after = None, None
        kf1_before, kf1_after = None, None

    if row_id is not None or Id is not None:
        if switch_command_line is not False:
            print(
                f'{separator_two}\n'
                f' Внесены изменения в таблицу {ExcControl.table_name}:\n'
                f'- Id: Номер возбудителя: {Id};\n'
                f'- row_id: порядковый номер в таблице (от 0 до [max.count]): {row_id};\n'
                f'- Ku: Коэффициент усиления пропорционального канала регулятора напряжения 5...200: до {ku_before}; после {ku_after};\n'
                f'- Trv: Постоянная времени регулятора 0.1 ...5: до {trv_before}; после {trv_after};\n'
                f'- Ku1: Коэффициент усиления канала по производной напряжения 0...10: до {ku1_before}; после {ku1_after};\n'
                f'- Kif1: Коэффициент усиления канала по производной тока ротора 0...5: до {kif1_before}; после {kif1_after};\n'
                f'- Kf: Коэффициент усиления канала по частоте  0...15: до {kf_before}; после {kf_after};\n'
                f'- Kf1: Коэффициент усиления канала по производной частоты 0... 7.5: до {kf1_before}; после {kf1_after};\n'
                f'{separator_two}\n'
            )
        return (
            f'{separator_two}\n'
            f' Внесены изменения в таблицу {ExcControl.table_name}:\n'
            f'- Id: Номер возбудителя: {Id};\n'
            f'- row_id: порядковый номер в таблице (от 0 до [max.count]): {row_id};\n'
            f'- Ku: Коэффициент усиления пропорционального канала регулятора напряжения 5...200: до {ku_before}; после {ku_after};\n'
            f'- Trv: Постоянная времени регулятора 0.1...5: до {trv_before}; после {trv_after};\n'
            f'- Ku1: Коэффициент усиления канала по производной напряжения 0...10: до {ku1_before}; после {ku1_after};\n'
            f'- Kif1: Коэффициент усиления канала по производной тока ротора 0...5: до {kif1_before}; после {kif1_after};\n'
            f'- Kf: Коэффициент усиления канала по частоте  0...15: до {kf_before}; после {kf_after};\n'
            f'- Kf1: Коэффициент усиления канала по производной частоты 0...7.5: до {kf1_before}; после {kf1_after};\n'
            f'{separator_two}\n'
        )
    else:
        print('')
