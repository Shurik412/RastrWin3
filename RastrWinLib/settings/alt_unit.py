# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.log_tools.tools import separator_noun
from RastrWinLib.variables.variable_parametrs import Variable


def set_alt_unit(
        row_id: int = 0,
        Active: bool = False,
        Unit: str = '',
        Alt: str = '',
        Formula: str = '',
        Prec: str = '',
        Tabl: str = '',
        rastr_win=RASTR,
        switch_command_line: bool = False, ):
    """
    Параметры настройки "Описание альтернативных единиц измерения" (таблица "Ед.Измерения": AltUnit):

    :param row_id: Порядковый номер в таблице "Ед. Измерения";
    :param Active: Активизация альтернативной ЕИ;
    :param Unit: Основная Единица Измерения;
    :param Alt: Альтернативная Единица Измерения;
    :param Formula: Формула для преобразования;
    :param Prec: Точность отображение Альт ЕИ;
    :param Tabl: Ограничитель по таблице;
    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param switch_command_line: True/False - вывод сообщений в протакол;
    :return: Nothing returns
    """

    variable_ = Variable(rastr_win=rastr_win)
    get_ = GettingParameter(rastr_win=rastr_win)

    # Active Активизация альтернативной ЕИ (A)
    active_get_before = get_.get_cell_row(table=AltUnit.table,
                                          column=AltUnit.Active,
                                          row_id=0)
    variable_.make_changes_row(table=AltUnit.table,
                               column=AltUnit.Active,
                               row_id=row_id,
                               value=Active)
    active_get_after = get_.get_cell_row(table=AltUnit.table,
                                         column=AltUnit.Active,
                                         row_id=0)

    # Unit Основная Единица Измерения (ЕИ)
    unit_get_before = get_.get_cell_row(table=AltUnit.table,
                                        column=AltUnit.Unit,
                                        row_id=0)
    variable_.make_changes_row(table=AltUnit.table,
                               column=AltUnit.Active,
                               row_id=row_id,
                               value=Unit)
    unit_get_after = get_.get_cell_row(table=AltUnit.table,
                                       column=AltUnit.Unit,
                                       row_id=0)

    # Alt Альтернативная Единица Измерения (Альт ЕИ)
    alt_get_before = get_.get_cell_row(table=AltUnit.table,
                                       column=AltUnit.Alt,
                                       row_id=0)
    variable_.make_changes_row(table=AltUnit.table,
                               column=AltUnit.Alt,
                               row_id=row_id,
                               value=Alt)
    alt_get_after = get_.get_cell_row(table=AltUnit.table,
                                      column=AltUnit.Alt,
                                      row_id=0)

    # Formula Формула для преобразования (Формула)
    formula_get_before = get_.get_cell_row(table=AltUnit.table,
                                           column=AltUnit.Formula,
                                           row_id=0)
    variable_.make_changes_row(table=AltUnit.table,
                               column=AltUnit.Formula,
                               row_id=row_id,
                               value=Formula)
    formula_get_after = get_.get_cell_row(table=AltUnit.table,
                                          column=AltUnit.Formula,
                                          row_id=0)

    # Prec Точность отображение Альт ЕИ (Точность)
    prec_get_before = get_.get_cell_row(table=AltUnit.table,
                                        column=AltUnit.Prec,
                                        row_id=0)
    variable_.make_changes_row(table=AltUnit.table,
                               column=AltUnit.Prec,
                               row_id=row_id,
                               value=Prec)
    prec_get_after = get_.get_cell_row(table=AltUnit.table,
                                       column=AltUnit.Prec,
                                       row_id=0)

    # Tabl Ограничитель по таблице (Табл)
    tabl_get_before = get_.get_cell_row(table=AltUnit.table,
                                        column=AltUnit.Tabl,
                                        row_id=0)
    variable_.make_changes_row(table=AltUnit.table,
                               column=AltUnit.Tabl,
                               row_id=row_id,
                               value=Tabl)
    tabl_get_after = get_.get_cell_row(table=AltUnit.table,
                                       column=AltUnit.Tabl,
                                       row_id=0)

    if switch_command_line is not False:
        print(
            f'{separator_noun}\n'
            f'Параметры альтернативных единиц измерений "Ед.Измерения":\n\n'
            f'- Active: Активизация альтернативной ЕИ (A): Active "до" = {active_get_before}; "после" = {active_get_after};\n'
            f'- Unit: Основная Единица Измерения (ЕИ): Unit "до" = {unit_get_before}; "после" = {unit_get_after};\n'
            f'- Alt: Альтернативная Единица Измерения (Альт ЕИ): Alt "до" = {alt_get_before}; "после" = {alt_get_after};\n'
            f'- Formula: Формула для преобразования (Формула): Formula "до" = {formula_get_before}; "после" = {formula_get_after};\n'
            f'- Prec: Точность отображение Альт ЕИ (Точность): Prec "до" = {prec_get_before}; "после" = {prec_get_after};\n'
            f'- Tabl: Ограничитель по таблице (Табл): Tabl "до" = {tabl_get_before}; "после" = {tabl_get_after};\n'
            f'{separator_noun}\n'
        )

    return (
        f'{separator_noun}\n'
        f'Параметры альтернативных единиц измерений "Ед.Измерения":\n\n'
        f'- Active: Активизация альтернативной ЕИ (A): Active "до" = {active_get_before}; "после" = {active_get_after};\n'
        f'- Unit: Основная Единица Измерения (ЕИ): Unit "до" = {unit_get_before}; "после" = {unit_get_after};\n'
        f'- Alt: Альтернативная Единица Измерения (Альт ЕИ): Alt "до" = {alt_get_before}; "после" = {alt_get_after};\n'
        f'- Formula: Формула для преобразования (Формула): Formula "до" = {formula_get_before}; "после" = {formula_get_after};\n'
        f'- Prec: Точность отображение Альт ЕИ (Точность): Prec "до" = {prec_get_before}; "после" = {prec_get_after};\n'
        f'- Tabl: Ограничитель по таблице (Табл): Tabl "до" = {tabl_get_before}; "после" = {tabl_get_after};\n'
        f'{separator_noun}\n'
    )
