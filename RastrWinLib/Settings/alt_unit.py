# -*- coding: utf-8 -*-
from prettytable import PrettyTable

from RastrWinLib.ActionsObject.Get import GettingParameter
from RastrWinLib.ActionsObject.Variable import Variable
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Tables.Settings.AltUnit import AltUnit
from RastrWinLib.Tools.tools import Tools


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
    f"""
    Параметры настройки "Описание альтернативных единиц измерения" (таблица "Ед.Измерения": AltUnit):

    :param row_id: Порядковый номер в таблице "Ед. Измерения";
    :param Active: Активизация альтернативной ЕИ;
    :param Unit: Основная Единица Измерения;
    :param Alt: Альтернативная Единица Измерения;
    :param Formula: Формула для преобразования;
    :param Prec: Точность отображение Альт ЕИ;
    :param Tabl: Ограничитель по таблице;
    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param switch_command_line: True/False - вывод сообщений в протокол;
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
    if switch_command_line:
        pt = PrettyTable()
        pt.title = 'Параметры альтернативных единиц измерений "Ед.Измерения":'
        pt.field_names = ['Название параметра', '"ДО"', '"ПОСЛЕ"']
        pt.add_row(['- Active: Активизация альтернативной ЕИ (A)', active_get_before, active_get_after])
        pt.add_row(['- Unit: Основная Единица Измерения (ЕИ)', unit_get_before, unit_get_after])
        pt.add_row(['- Alt: Альтернативная Единица Измерения (Альт ЕИ)', alt_get_before, alt_get_after])
        pt.add_row(['- Formula: Формула для преобразования (Формула)', formula_get_before, formula_get_after])
        pt.add_row(['- Prec: Точность отображение Альт ЕИ (Точность)', prec_get_before, prec_get_after])
        pt.add_row(['- Tabl: Ограничитель по таблице (Табл)', tabl_get_before, tabl_get_after])
        print(pt)
