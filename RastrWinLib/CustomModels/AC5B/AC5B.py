# -*- coding: utf-8 -*-
#  ---------------- Модель AC5B ----------------
# Модель системы возбуждения типа AC5B,
# реализованная в ПК RUSTab, состоит одного макроблока.
# Параметры системы возбуждения AC5B.xmldev заносятся в ПК RUSTab в таблицу «ВозбудителиIEEE».

from RastrWinLib.tables.Dynamic.DFWIEEE421 import DFWIEEE421
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.log_tools.tools import separator_two
from RastrWinLib.variables.variable_parametrs import Variable


class Parameters:
    """
    #  ----------- Типовые параметры от НТЦ для модели AC5B ----------------
    # Модель системы возбуждения типа AC5B, реализованная в ПК RUSTab, состоит одного макроблока.
    # Параметры системы возбуждения AC5B.xmldev заносятся в ПК RUSTab в таблицу «ВозбудителиIEEE».
    # Типовые значение параметров настройки, приняты экспертно НТЦ.
    """
    Kpr: float = 26.55  # Коэффициент усиления дифференциального звена
    Tb: float = 0.2  # Постоянная времени дифференциального звена
    Ka: float = 30.0  # Пропорциональный коэффициент усиления регулятора напряжения
    Vrmax: float = 999.0  # Максимальное ограничение интегрального звена
    Vrmin: float = -999.0  # Минимальное ограничение интегрального звена
    Te: float = 0.2  # Постоянная времени интегратора возбудителя
    Aex: float = 0.098  # Коэффициент экспоненты (задание насыщения)
    Bex: float = 0.346  # Степень экспоненты (задание насыщения)


def change_parameters_AC5B(
        Id=None,
        row_id=None,
        Kpr=Parameters.Kpr,
        Tb=Parameters.Tb,
        Ka=Parameters.Ka,
        Vrmax=Parameters.Vrmax,
        Vrmin=Parameters.Vrmin,
        Te=Parameters.Te,
        Aex=Parameters.Aex,
        Bex=Parameters.Bex,
        rastr_win=RASTR,
        switch_command_line: bool = False):
    """

    :param Id: номер возбудителя;
    :param row_id: порядковый номер в таблице (от 0 до [max.count]);
    :param Kpr: Коэффициент усиления дифференциального звена;
    :param Tb: Постоянная времени дифференциального звена;
    :param Ka: Пропорциональный коэффициент усиления регулятора напряжения;
    :param Vrmax: Максимальное ограничение интегрального звена;
    :param Vrmin: Минимальное ограничение интегрального звена;
    :param Te: Постоянная времени интегратора возбудителя;
    :param Aex: Коэффициент экспоненты (задание насыщения);
    :param Bex: Степень экспоненты (задание насыщения);
    :param switch_command_line: True/False - вывод сообщений в протакол;
    :param rastr_win: COM - объект Rastr.Astra (win32com);
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

        # Tb
        if switch_command_line is not None:
            tb_before = get_.get_cell_id(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Tb,
                                         Id=Id)
        else:
            tb_before = None

        variable_.make_changes_setsel(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Tb,
                                      key=f'{DFWIEEE421.Id}={Id}',
                                      value=Tb)

        if switch_command_line is not None:
            tb_after = get_.get_cell_id(table=DFWIEEE421.table,
                                        column=DFWIEEE421.Tb,
                                        Id=Id)
        else:
            tb_after = None

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

        if switch_command_line is not False:
            print(
                f'{separator_two}\n'
                f' Внесены изменения в таблицу {DFWIEEE421.table_name}:\n'
                f'- Id: Номер возбудителя: {Id};\n'
                f'- row_id: порядковый номер в таблице (от 0 до [max.count]): {row_id};\n'
                f'- Kpr: Коэффициент усиления дифференциального звена: до {kpr_before}; после {kpr_after};\n'
                f'- Tb: Постоянная времени дифференциального звена: до {tb_before}; после {tb_after};\n'
                f'- Ka: Пропорциональный коэффициент усиления регулятора напряжения: до {ka_before}; после {ka_after};\n'
                f'- Vrmax: Максимальное ограничение интегрального звена: до {vrmax_before}; после {vrmax_after};\n'
                f'- Vrmin: Минимальное ограничение интегрального звена: до {vrmin_before}; после {vrmin_after};\n'
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
            f'- Kpr: Коэффициент усиления дифференциального звена: до {kpr_before}; после {kpr_after};\n'
            f'- Tb: Постоянная времени дифференциального звена: до {tb_before}; после {tb_after};\n'
            f'- Ka: Пропорциональный коэффициент усиления регулятора напряжения: до {ka_before}; после {ka_after};\n'
            f'- Vrmax: Максимальное ограничение интегрального звена: до {vrmax_before}; после {vrmax_after};\n'
            f'- Vrmin: Минимальное ограничение интегрального звена: до {vrmin_before}; после {vrmin_after};\n'
            f'- Te: Постоянная времени интегратора возбудителя: до {te_before}; после {te_after};\n'
            f'- Aex: Коэффициент экспоненты (задание насыщения): до {aex_before}; после {aex_after};\n'
            f'- Bex: Степень экспоненты (задание насыщения): до {bex_before}; после {bex_after};\n'
            f'{separator_two}\n'
        )

    if row_id is not None and Id is None:
        # Kpr
        if switch_command_line is not False:
            kpr_before = get_.get_cell_row(table=DFWIEEE421.table,
                                           column=DFWIEEE421.Kpr,
                                           row_id=row_id)
        else:
            kpr_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Kpr,
                                   row_id=row_id,
                                   value=Kpr)

        if switch_command_line is not False:
            kpr_after = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Kpr,
                                          row_id=row_id)
        else:
            kpr_after = None

        # Tb
        if switch_command_line is not False:
            tb_before = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Tb,
                                          row_id=row_id)
        else:
            tb_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Tb,
                                   row_id=row_id,
                                   value=Tb)

        if switch_command_line is not False:
            tb_after = get_.get_cell_row(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Tb,
                                         row_id=row_id)
        else:
            tb_after = None

        # Ka
        if switch_command_line is not False:
            ka_before = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Ka,
                                          row_id=row_id)
        else:
            ka_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Ka,
                                   row_id=row_id,
                                   value=Ka)

        if switch_command_line is not False:
            ka_after = get_.get_cell_row(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Ka,
                                         row_id=row_id)
        else:
            ka_after = None

        # Vrmax
        if switch_command_line is not False:
            vrmax_before = get_.get_cell_row(table=DFWIEEE421.table,
                                             column=DFWIEEE421.Vrmax,
                                             row_id=row_id)
        else:
            vrmax_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Vrmax,
                                   row_id=row_id,
                                   value=Vrmax)

        if switch_command_line is not False:
            vrmax_after = get_.get_cell_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Vrmax,
                                            row_id=row_id)
        else:
            vrmax_after = None

        # Vrmin
        if switch_command_line is not False:
            vrmin_before = get_.get_cell_row(table=DFWIEEE421.table,
                                             column=DFWIEEE421.Vrmin,
                                             row_id=row_id)
        else:
            vrmin_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Vrmin,
                                   row_id=row_id,
                                   value=Vrmin)

        if switch_command_line is not False:
            vrmin_after = get_.get_cell_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Vrmin,
                                            row_id=row_id)
        else:
            vrmin_after = None

        # Te
        if switch_command_line is not False:
            te_before = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Te,
                                          row_id=row_id)
        else:
            te_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Te,
                                   row_id=row_id,
                                   value=Te)

        if switch_command_line is not False:
            te_after = get_.get_cell_row(table=DFWIEEE421.table,
                                         column=DFWIEEE421.Te,
                                         row_id=row_id)
        else:
            te_after = None

        # Aex
        if switch_command_line is not False:
            aex_before = get_.get_cell_row(table=DFWIEEE421.table,
                                           column=DFWIEEE421.Aex,
                                           row_id=row_id)
        else:
            aex_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Aex,
                                   row_id=row_id,
                                   value=Aex)

        if switch_command_line is not False:
            aex_after = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Aex,
                                          row_id=row_id)
        else:
            aex_after = None

        # Bex
        if switch_command_line is not False:
            bex_before = get_.get_cell_row(table=DFWIEEE421.table,
                                           column=DFWIEEE421.Bex,
                                           row_id=row_id)
        else:
            bex_before = None

        variable_.make_changes_row(table=DFWIEEE421.table,
                                   column=DFWIEEE421.Bex,
                                   row_id=row_id,
                                   value=Bex)

        if switch_command_line is not False:
            bex_after = get_.get_cell_row(table=DFWIEEE421.table,
                                          column=DFWIEEE421.Bex,
                                          row_id=row_id)
        else:
            bex_after = None

        if switch_command_line is not False:
            print(
                f'{separator_two}\n'
                f' Внесены изменения в таблицу {DFWIEEE421.table_name}:\n'
                f'- Id: Номер возбудителя: {Id};\n'
                f'- row_id: порядковый номер в таблице (от 0 до [max.count]): {row_id};\n'
                f'- Kpr: Коэффициент усиления дифференциального звена: до {kpr_before}; после {kpr_after};\n'
                f'- Tb: Постоянная времени дифференциального звена: до {tb_before}; после {tb_after};\n'
                f'- Ka: Пропорциональный коэффициент усиления регулятора напряжения: до {ka_before}; после {ka_after};\n'
                f'- Vrmax: Максимальное ограничение интегрального звена: до {vrmax_before}; после {vrmax_after};\n'
                f'- Vrmin: Минимальное ограничение интегрального звена: до {vrmin_before}; после {vrmin_after};\n'
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
            f'- Kpr: Коэффициент усиления дифференциального звена: до {kpr_before}; после {kpr_after};\n'
            f'- Tb: Постоянная времени дифференциального звена: до {tb_before}; после {tb_after};\n'
            f'- Ka: Пропорциональный коэффициент усиления регулятора напряжения: до {ka_before}; после {ka_after};\n'
            f'- Vrmax: Максимальное ограничение интегрального звена: до {vrmax_before}; после {vrmax_after};\n'
            f'- Vrmin: Минимальное ограничение интегрального звена: до {vrmin_before}; после {vrmin_after};\n'
            f'- Te: Постоянная времени интегратора возбудителя: до {te_before}; после {te_after};\n'
            f'- Aex: Коэффициент экспоненты (задание насыщения): до {aex_before}; после {aex_after};\n'
            f'- Bex: Степень экспоненты (задание насыщения): до {bex_before}; после {bex_after};\n'
            f'{separator_two}\n'
        )
    if Id is None and row_id is None:
        print(f'{separator_two}'
              f'Не задано значение Id и/или row_id!'
              f'{separator_two}')
