# -*- coding: utf-8 -*-

#  ---------------- Модель AC8B ----------------
# Модель системы возбуждения типа AC8B, реализованная в ПК RUSTab, состоит одного макроблока:
# Система возбуждения: AC8B.xmldev.
# Параметры системы возбуждения AC8B.xmldev заносятся в таблицу «ВозбудителиIEEE».

from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.tables.Dynamic.DFWIEEE421 import DFWIEEE421
from RastrWinLib.variables.variable_parametrs import Variable


class Parameters:
    """
    #  ----------- Типовые параметры от НТЦ для модели AC8B ----------------
    # Модель системы возбуждения типа AC8B, реализованная в ПК RUSTab, состоит одного макроблока.
    # Параметры системы возбуждения AC8B.xmldev заносятся в ПК RUSTab в таблицу «ВозбудителиIEEE».
    # Типовые значение параметров настройки, приняты экспертно НТЦ.
    """
    Kpr: float = 24.35  # Пропорциональный коэффициент усиления ПИД-регулятора
    Kir: float = 2.326  # Интегральный коэффициент усиления ПИД-регулятора
    Kdr: float = 6.7  # Дифференциальный коэффициент усиления ПИД-регулятора
    Tdr: float = 0.29  # Постоянная времени дифференциального канала ПИД-регулятора
    Ka: float = 1.0  # Коэффициент усиления регулятора напряжения
    Ta: float = 0.001  # Постоянная времени регулятора напряжения
    Vrmax: float = 5.0  # Максимальное ограничение регулятора напряжения
    Vrmin: float = 0.0  # Минимальное ограничение регулятора напряжения
    Te: float = 0.6  # Постоянная времени интегратора возбудителя
    Aex: float = 0.0007  # Коэффициент экспоненты (задание насыщения)
    Bex: float = 0.921  # Степень экспоненты (задание насыщения)


def change_parameters_AC8B(
        Id=None,
        row_id=None,
        Kpr: float = Parameters.Kpr,
        Kir: float = Parameters.Kir,
        Kdr: float = Parameters.Kdr,
        Tdr: float = Parameters.Tdr,
        Ka: float = Parameters.Ka,
        Ta: float = Parameters.Ta,
        Vrmax: float = Parameters.Vrmax,
        Vrmin: float = Parameters.Vrmin,
        Te: float = Parameters.Te,
        Aex: float = Parameters.Aex,
        Bex: float = Parameters.Bex,
        switch_command_line: bool = False):
    """

    :param Id: номер возбудителя;
    :param row_id: порядковый номер в таблице (от 0 до [max.count]);
    :param Kpr: Пропорциональный коэффициент усиления ПИД-регулятора;
    :param Kir: Интегральный коэффициент усиления ПИД-регулятора;
    :param Kdr: Дифференциальный коэффициент усиления ПИД-регулятора;
    :param Tdr: Постоянная времени дифференциального канала ПИД-регулятора;
    :param Ka: Коэффициент усиления регулятора напряжения;
    :param Ta: Постоянная времени регулятора напряжения;
    :param Vrmax: Максимальное ограничение регулятора напряжения;
    :param Vrmin: Минимальное ограничение регулятора напряжения;
    :param Te: Постоянная времени интегратора возбудителя;
    :param Aex: Коэффициент экспоненты (задание насыщения);
    :param Bex: Степень экспоненты (задание насыщения);
    :param switch_command_line: True/False - вывод сообщений в протакол;
    :return:
    """

    variable_ = Variable(rastr_win=rastr_win)
    get_ = GettingParameter(rastr_win=rastr_win)

    if Id is not None and row_id is None:
        # Kpr
        if switch_command_line is not None:
            kpr_before = get_.get_cell_id(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Kpr,
                                          Id=Id)
        else:
            kpr_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Kpr,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Kpr)

        if switch_command_line is not None:
            kpr_after = get_.get_cell_id(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Kpr,
                                         Id=Id)
        else:
            kpr_after = None

        # Kir
        if switch_command_line is not None:
            kir_before = get_.get_cell_id(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Kir,
                                          Id=Id)
        else:
            kir_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Kir,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Kir)

        if switch_command_line is not None:
            kir_after = get_.get_cell_id(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Kir,
                                         Id=Id)
        else:
            kir_after = None

            # Kdr
        if switch_command_line is not None:
            kdr_before = get_.get_cell_id(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Kdr,
                                          Id=Id)
        else:
            kdr_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Kdr,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Kdr)

        if switch_command_line is not None:
            kdr_after = get_.get_cell_id(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Kdr,
                                         Id=Id)
        else:
            kdr_after = None

            # Tdr
        if switch_command_line is not None:
            tdr_before = get_.get_cell_id(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Tdr,
                                          Id=Id)
        else:
            tdr_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Tdr,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Tdr)

        if switch_command_line is not None:
            tdr_after = get_.get_cell_id(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Tdr,
                                         Id=Id)
        else:
            tdr_after = None

        # Ka
        if switch_command_line is not None:
            ka_before = get_.get_cell_id(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Ka,
                                         Id=Id)
        else:
            ka_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Ka,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Ka)

        if switch_command_line is not None:
            ka_after = get_.get_cell_id(table=DFWIEEE421.table,
                                        column=DFWIEEE421.Ka,
                                        Id=Id)
        else:
            ka_after = None

        # Ta
        if switch_command_line is not None:
            ta_before = get_.get_cell_id(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Ta,
                                         Id=Id)
        else:
            ta_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Ta,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Ta)

        if switch_command_line is not None:
            ta_after = get_.get_cell_id(table=DFWIEEE421.table,
                                        column=DFWIEEE421.Ta,
                                        Id=Id)
        else:
            ta_after = None

        # Vrmax
        if switch_command_line is not None:
            vrmax_before = get_.get_cell_id(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Vrmax,
                                            Id=Id)
        else:
            vrmax_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Vrmax,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Vrmax)

        if switch_command_line is not None:
            vrmax_after = get_.get_cell_id(table=DFWIEEE421.table,
                                           column=DFWIEEE421.Vrmax,
                                           Id=Id)
        else:
            vrmax_after = None

        # Vrmin
        if switch_command_line is not None:
            vrmin_before = get_.get_cell_id(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Vrmin,
                                            Id=Id)
        else:
            vrmin_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Vrmin,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Vrmin)

        if switch_command_line is not None:
            vrmin_after = get_.get_cell_id(table=DFWIEEE421.table,
                                           column=DFWIEEE421.Vrmin,
                                           Id=Id)
        else:
            vrmin_after = None

        # Te
        if switch_command_line is not None:
            te_before = get_.get_cell_id(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Te,
                                         Id=Id)
        else:
            te_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Te,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Te)

        if switch_command_line is not None:
            te_after = get_.get_cell_id(table=DFWIEEE421.table,
                                        column=DFWIEEE421.Te,
                                        Id=Id)
        else:
            te_after = None

        # Aex
        if switch_command_line is not None:
            aex_before = get_.get_cell_id(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Aex,
                                          Id=Id)
        else:
            aex_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Aex,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Aex)

        if switch_command_line is not None:
            aex_after = get_.get_cell_id(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Aex,
                                         Id=Id)
        else:
            aex_after = None

        # Bex
        if switch_command_line is not None:
            bex_before = get_.get_cell_id(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Bex,
                                          Id=Id)
        else:
            bex_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Bex,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Bex)

        if switch_command_line is not None:
            bex_after = get_.get_cell_id(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Bex,
                                         Id=Id)
        else:
            bex_after = None

    elif row_id is not None and Id is None:
        # Kpr
        if switch_command_line is not None:
            kpr_before = get_.get_cell_row(table=DFWIEEE421.table,
                                           column=DFWIEEE421.Kpr,
                                           row_id=row_id)
        else:
            kpr_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Kpr,
                                   row_id=row_id,
                                   value=Kpr)

        if switch_command_line is not None:
            kpr_after = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Kpr,
                                          row_id=row_id)
        else:
            kpr_after = None

        # Kir
        if switch_command_line is not None:
            kir_before = get_.get_cell_row(table=DFWIEEE421.table,
                                           column=DFWIEEE421.Kir,
                                           row_id=row_id)
        else:
            kir_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Kir,
                                   row_id=row_id,
                                   value=Kir)

        if switch_command_line is not None:
            kir_after = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Kir,
                                          row_id=row_id)
        else:
            kir_after = None

            # Kdr
        if switch_command_line is not None:
            kdr_before = get_.get_cell_row(table=DFWIEEE421.table,
                                           column=DFWIEEE421.Kdr,
                                           row_id=row_id)
        else:
            kdr_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Kdr,
                                   row_id=row_id,
                                   value=Kdr)

        if switch_command_line is not None:
            kdr_after = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Kdr,
                                          row_id=row_id)
        else:
            kdr_after = None

            # Tdr
        if switch_command_line is not None:
            tdr_before = get_.get_cell_row(table=DFWIEEE421.table,
                                           column=DFWIEEE421.Tdr,
                                           row_id=row_id)
        else:
            tdr_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Tdr,
                                   row_id=row_id,
                                   value=Tdr)

        if switch_command_line is not None:
            tdr_after = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Tdr,
                                          row_id=row_id)
        else:
            tdr_after = None

        # Ka
        if switch_command_line is not None:
            ka_before = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Ka,
                                          row_id=row_id)
        else:
            ka_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Ka,
                                   row_id=row_id,
                                   value=Ka)

        if switch_command_line is not None:
            ka_after = get_.get_cell_row(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Ka,
                                         row_id=row_id)
        else:
            ka_after = None

        # Ta
        if switch_command_line is not None:
            ta_before = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Ta,
                                          row_id=row_id)
        else:
            ta_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Ta,
                                   row_id=row_id,
                                   value=Ta)

        if switch_command_line is not None:
            ta_after = get_.get_cell_row(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Ta,
                                         row_id=row_id)
        else:
            ta_after = None

        # Vrmax
        if switch_command_line is not None:
            vrmax_before = get_.get_cell_row(table=DFWIEEE421.table,
                                             column=DFWIEEE421.Vrmax,
                                             row_id=row_id)
        else:
            vrmax_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Vrmax,
                                   row_id=row_id,
                                   value=Vrmax)

        if switch_command_line is not None:
            vrmax_after = get_.get_cell_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Vrmax,
                                            row_id=row_id)
        else:
            vrmax_after = None

        # Vrmin
        if switch_command_line is not None:
            vrmin_before = get_.get_cell_row(table=DFWIEEE421.table,
                                             column=DFWIEEE421.Vrmin,
                                             row_id=row_id)
        else:
            vrmin_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Vrmin,
                                   row_id=row_id,
                                   value=Vrmin)

        if switch_command_line is not None:
            vrmin_after = get_.get_cell_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Vrmin,
                                            row_id=row_id)
        else:
            vrmin_after = None

        # Te
        if switch_command_line is not None:
            te_before = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Te,
                                          row_id=row_id)
        else:
            te_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Te,
                                   row_id=row_id,
                                   value=Te)

        if switch_command_line is not None:
            te_after = get_.get_cell_row(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Te,
                                         row_id=row_id)
        else:
            te_after = None

        # Aex
        if switch_command_line is not None:
            aex_before = get_.get_cell_row(table=DFWIEEE421.table,
                                           column=DFWIEEE421.Aex,
                                           row_id=row_id)
        else:
            aex_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Aex,
                                   row_id=row_id,
                                   value=Aex)

        if switch_command_line is not None:
            aex_after = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Aex,
                                          row_id=row_id)
        else:
            aex_after = None

        # Bex
        if switch_command_line is not None:
            bex_before = get_.get_cell_row(table=DFWIEEE421.table,
                                           column=DFWIEEE421.Bex,
                                           row_id=row_id)
        else:
            bex_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Bex,
                                   row_id=row_id,
                                   value=Bex)

        if switch_command_line is not None:
            bex_after = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Bex,
                                          row_id=row_id)
        else:
            bex_after = None

    else:
        kpr_before, kpr_after = None, None
        kir_before, kir_after = None, None
        kdr_before, kdr_after = None, None
        tdr_before, tdr_after = None, None
        ka_before, ka_after = None, None
        ta_before, ta_after = None, None
        vrmax_before, vrmax_after = None, None
        vrmin_before, vrmin_after = None, None
        te_before, te_after = None, None
        aex_before, aex_after = None, None
        bex_before, bex_after = None, None

    if switch_command_line is not False:
        print(
            f'{separator_two}\n'
            f' Внесены изменения в таблицу {DFWIEEE421.table_name}:\n'
            f'- Id: Номер возбудителя: {Id};\n'
            f'- row_id: порядковый номер в таблице (от 0 до [max.count]): {row_id};\n'
            f'- Kpr: Пропорциональный коэффициент усиления ПИД-регулятора: до {kpr_before}; после {kpr_after};\n'
            f'- Kir: Интегральный коэффициент усиления ПИД-регулятора: до {kir_before}; после {kir_after};\n'
            f'- Kdr: Дифференциальный коэффициент усиления ПИД-регулятора: до {kdr_before}; после {kdr_after};\n'
            f'- Tdr: Постоянная времени дифференциального канала ПИД-регулятора: до {tdr_before}; после {tdr_after};\n'
            f'- Ka: Коэффициент усиления регулятора напряжения: до {ka_before}; после {ka_after};\n'
            f'- Ta: Постоянная времени регулятора напряжения: до {ta_before}; после {ta_after};\n'
            f'- Vrmax: Максимальное ограничение регулятора напряжения: до {vrmax_before}; после {vrmax_after};\n'
            f'- Vrmin: Минимальное ограничение регулятора напряжения: до {vrmin_before}; после {vrmin_after};\n'
            f'- Te: Постоянная времени интегратора возбудителя: до {te_before}; после {te_after};\n'
            f'- Aex: Коэффициент экспоненты (задание насыщения): до {aex_before}; после {aex_after};\n'
            f'- Bex: Степень экспоненты (задание насыщения): до {bex_before}; после {bex_after};\n'
            f'{separator_two}\n'
        )
    return (
        f'{separator_two}\n'
        f' Внесены изменения в таблицу {DFWIEEE421.table_name}:\n'
        f'- Id: Номер возбудителя: {Id};\n'
        f'- row_id: порядковый номер в таблице (от 0 до [max.count]): {row_id};\n'
        f'- Kpr: Пропорциональный коэффициент усиления ПИД-регулятора: до {kpr_before}; после {kpr_after};\n'
        f'- Kir: Интегральный коэффициент усиления ПИД-регулятора: до {kir_before}; после {kir_after};\n'
        f'- Kdr: Дифференциальный коэффициент усиления ПИД-регулятора: до {kdr_before}; после {kdr_after};\n'
        f'- Tdr: Постоянная времени дифференциального канала ПИД-регулятора: до {tdr_before}; после {tdr_after};\n'
        f'- Ka: Коэффициент усиления регулятора напряжения: до {ka_before}; после {ka_after};\n'
        f'- Ta: Постоянная времени регулятора напряжения: до {ta_before}; после {ta_after};\n'
        f'- Vrmax: Максимальное ограничение регулятора напряжения: до {vrmax_before}; после {vrmax_after};\n'
        f'- Vrmin: Минимальное ограничение регулятора напряжения: до {vrmin_before}; после {vrmin_after};\n'
        f'- Te: Постоянная времени интегратора возбудителя: до {te_before}; после {te_after};\n'
        f'- Aex: Коэффициент экспоненты (задание насыщения): до {aex_before}; после {aex_after};\n'
        f'- Bex: Степень экспоненты (задание насыщения): до {bex_before}; после {bex_after};\n'
        f'{separator_two}\n'
    )
