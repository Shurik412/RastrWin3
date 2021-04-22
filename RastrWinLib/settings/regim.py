# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.log_tools.tools import separator_noun
from RastrWinLib.tables.tables_attributes import com_regim_table, com_regim_attributes_list
from RastrWinLib.variables.variable_parametrs import Variable


def set_regim(neb_p=1.000,
              it_max=100,
              start=0,
              flot=1,
              dv_min=0.5,
              dv_max=2.000,
              dd_max=5157,
              status=0,
              rr=0,
              wt=0,
              gen_p=0,
              method=0,
              method_ogr=0,
              print_mode=0,
              qmax=0,
              min_x=0,
              calc_tr=0,
              nag_p=0,
              rem_breaker=0,
              gram=0,
              ctrl_baza=0,
              itz=0,
              itz_ogr_max=0,
              itz_ogr_min=0,
              min_nodes_in_island=0,
              switch_command_line=False):
    """
    Параметры настройки "Общие параметры режима" (таблица "Режим": com_regim):

    :param switch_command_line:
    :param neb_p: Точность расчета (dP)
    :param it_max: Максимальное число итераций (It)
    :param start: Стартовый алгоритм (Start)
    :param flot: Плоский старт (Пл.старт)
    :param dv_min: Мин. допустимое снижение V (dV-)
    :param dv_max: Макс. допустимое превышение V (dV+)
    :param dd_max: Макс. допустимый угол по связи (dDelta)
    :param status: Состояние расчета режима (Статус)
    :param rr: Учет частоты: (W)
    :param wt: Отклонение частоты (dF)
    :param gen_p: Пересчитывать P/Q узла по P ген (Ген->P)
    :param method: Метод Расчета (Метод)
    :param method_ogr: Метод учета ограничений Q (Метод учета ограничений Q)
    :param print_mode: Уровень печати (Печать)
    :param qmax: Точный метод расчета Qmax (Qmax)
    :param min_x: Сопротивление выключателя (ое на 10-6) (Min_X)
    :param calc_tr: Пересчет АТ/3х обм. трансформаторов (Транс.)
    :param nag_p: Пересчитывать (P/Q) нагрузки узла по ВРДО (Наг->P)
    :param rem_breaker: Удаление выключателей из схемы: (Выкл)
    :param gram: Пересчет мощности генератора по ГРАМ: (Грам)
    :param ctrl_baza: Автоматическое создание БУ (БУ)
    :param itz: Стартовый метод: число итераций (Z_it)
    :param itz_ogr_max: Стартовый метод: Учет Qmax с итерации (Z_it_max)
    :param itz_ogr_min: Стартовый метод: Учет Qmin с итерации (Z_it_min)
    :param min_nodes_in_island: Минимальное число узлов в острове (Min_nodes)
    """

    variable_def_rowid = Variable(rastr_win=RASTR,
                                  switch_command_line=False)
    get_ = GettingParameter(rastr_win=RASTR)

    get_neb_p = get_.get_cell(table=com_regim_table,
                              column=com_regim_attributes_list[0],
                              row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[0],
                                        row_id=0,
                                        value=float(neb_p))
    get_neb_p_after = get_.get_cell(table=com_regim_table,
                                    column=com_regim_attributes_list[0],
                                    row_id=0)

    get_it_max = get_.get_cell(table=com_regim_table,
                               column=com_regim_attributes_list[1],
                               row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[1],
                                        row_id=0,
                                        value=it_max)
    get_it_max_after = get_.get_cell(table=com_regim_table,
                                     column=com_regim_attributes_list[1],
                                     row_id=0)

    get_start = get_.get_cell(table=com_regim_table,
                              column=com_regim_attributes_list[2],
                              row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[2],
                                        row_id=0,
                                        value=start)
    get_start_after = get_.get_cell(table=com_regim_table,
                                    column=com_regim_attributes_list[2],
                                    row_id=0)

    get_flot = get_.get_cell(table=com_regim_table,
                             column=com_regim_attributes_list[3],
                             row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[3],
                                        row_id=0,
                                        value=flot)
    get_flot_after = get_.get_cell(table=com_regim_table,
                                   column=com_regim_attributes_list[3],
                                   row_id=0)

    get_dv_min = get_.get_cell(table=com_regim_table,
                               column=com_regim_attributes_list[4],
                               row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[4],
                                        row_id=0,
                                        value=float(dv_min))
    get_dv_min_after = get_.get_cell(table=com_regim_table,
                                     column=com_regim_attributes_list[4],
                                     row_id=0)

    get_dv_max = get_.get_cell(table=com_regim_table,
                               column=com_regim_attributes_list[5],
                               row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[5],
                                        row_id=0,
                                        value=float(dv_max))
    get_dv_max_after = get_.get_cell(table=com_regim_table,
                                     column=com_regim_attributes_list[5],
                                     row_id=0)

    get_dd_max = get_.get_cell(table=com_regim_table,
                               column=com_regim_attributes_list[6],
                               row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[6],
                                        row_id=0,
                                        value=dd_max)
    get_dd_max_after = get_.get_cell(table=com_regim_table,
                                     column=com_regim_attributes_list[6],
                                     row_id=0)

    get_status = get_.get_cell(table=com_regim_table,
                               column=com_regim_attributes_list[7],
                               row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[7],
                                        row_id=0,
                                        value=status)
    get_status_after = get_.get_cell(table=com_regim_table,
                                     column=com_regim_attributes_list[7],
                                     row_id=0)

    get_rr = get_.get_cell(table=com_regim_table,
                           column=com_regim_attributes_list[8],
                           row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[8],
                                        row_id=0,
                                        value=rr)
    get_rr_after = get_.get_cell(table=com_regim_table,
                                 column=com_regim_attributes_list[8],
                                 row_id=0)

    get_wt = get_.get_cell(table=com_regim_table,
                           column=com_regim_attributes_list[9],
                           row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[9],
                                        row_id=0,
                                        value=wt)
    get_wt_after = get_.get_cell(table=com_regim_table,
                                 column=com_regim_attributes_list[9],
                                 row_id=0)

    get_gen_p = get_.get_cell(table=com_regim_table,
                              column=com_regim_attributes_list[10],
                              row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[10],
                                        row_id=0,
                                        value=gen_p)
    get_gen_p_after = get_.get_cell(table=com_regim_table,
                                    column=com_regim_attributes_list[10],
                                    row_id=0)

    get_method = get_.get_cell(table=com_regim_table,
                               column=com_regim_attributes_list[11],
                               row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[11],
                                        row_id=0,
                                        value=method)
    get_method_after = get_.get_cell(table=com_regim_table,
                                     column=com_regim_attributes_list[11],
                                     row_id=0)

    get_method_ogr = get_.get_cell(table=com_regim_table,
                                   column=com_regim_attributes_list[12],
                                   row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[12],
                                        row_id=0,
                                        value=method_ogr)
    get_method_ogr_after = get_.get_cell(table=com_regim_table,
                                         column=com_regim_attributes_list[12],
                                         row_id=0)

    get_print_mode = get_.get_cell(table=com_regim_table,
                                   column=com_regim_attributes_list[13],
                                   row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[13],
                                        row_id=0,
                                        value=print_mode)
    get_print_mode_after = get_.get_cell(table=com_regim_table,
                                         column=com_regim_attributes_list[13],
                                         row_id=0)

    get_qmax = get_.get_cell(table=com_regim_table,
                             column=com_regim_attributes_list[14],
                             row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[14],
                                        row_id=0,
                                        value=qmax)
    get_qmax_after = get_.get_cell(table=com_regim_table,
                                   column=com_regim_attributes_list[14],
                                   row_id=0)

    get_min_x = get_.get_cell(table=com_regim_table,
                              column=com_regim_attributes_list[15],
                              row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[15],
                                        row_id=0,
                                        value=min_x)
    get_min_x_after = get_.get_cell(table=com_regim_table,
                                    column=com_regim_attributes_list[15],
                                    row_id=0)

    get_calc_tr = get_.get_cell(table=com_regim_table,
                                column=com_regim_attributes_list[16],
                                row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[16],
                                        row_id=0,
                                        value=calc_tr)
    get_calc_tr_after = get_.get_cell(table=com_regim_table,
                                      column=com_regim_attributes_list[16],
                                      row_id=0)

    get_nag_p = get_.get_cell(table=com_regim_table,
                              column=com_regim_attributes_list[17],
                              row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[17],
                                        row_id=0,
                                        value=nag_p)
    get_nag_p_after = get_.get_cell(table=com_regim_table,
                                    column=com_regim_attributes_list[17],
                                    row_id=0)

    get_rem_breaker = get_.get_cell(table=com_regim_table,
                                    column=com_regim_attributes_list[18],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[18],
                                        row_id=0,
                                        value=rem_breaker)
    get_rem_breaker_after = get_.get_cell(table=com_regim_table,
                                          column=com_regim_attributes_list[18],
                                          row_id=0)

    get_gram = get_.get_cell(table=com_regim_table,
                             column=com_regim_attributes_list[19],
                             row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[19],
                                        row_id=0,
                                        value=gram)
    get_gram_after = get_.get_cell(table=com_regim_table,
                                   column=com_regim_attributes_list[19],
                                   row_id=0)

    get_ctrl_baza = get_.get_cell(table=com_regim_table,
                                  column=com_regim_attributes_list[20],
                                  row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[20],
                                        row_id=0,
                                        value=ctrl_baza)
    get_ctrl_baza_after = get_.get_cell(table=com_regim_table,
                                        column=com_regim_attributes_list[20],
                                        row_id=0)

    get_itz = get_.get_cell(table=com_regim_table,
                            column=com_regim_attributes_list[21],
                            row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[21],
                                        row_id=0,
                                        value=itz)
    get_itz_after = get_.get_cell(table=com_regim_table,
                                  column=com_regim_attributes_list[21],
                                  row_id=0)

    get_itz_ogr_max = get_.get_cell(table=com_regim_table,
                                    column=com_regim_attributes_list[22],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[22],
                                        row_id=0,
                                        value=itz_ogr_max)
    get_itz_ogr_max_after = get_.get_cell(table=com_regim_table,
                                          column=com_regim_attributes_list[22],
                                          row_id=0)

    get_itz_ogr_min = get_.get_cell(table=com_regim_table,
                                    column=com_regim_attributes_list[23],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[23],
                                        row_id=0,
                                        value=itz_ogr_min)
    get_itz_ogr_min_after = get_.get_cell(table=com_regim_table,
                                          column=com_regim_attributes_list[23],
                                          row_id=0)

    get_min_nodes_in_island = get_.get_cell(table=com_regim_table,
                                            column=com_regim_attributes_list[24],
                                            row_id=0)
    variable_def_rowid.make_changes_row(table=com_regim_table,
                                        column=com_regim_attributes_list[24],
                                        row_id=0,
                                        value=min_nodes_in_island)
    get_min_nodes_in_island_after = get_.get_cell(table=com_regim_table,
                                                  column=com_regim_attributes_list[24],
                                                  row_id=0)

    if switch_command_line is not False:
        print(separator_noun)
        print(
            f'Таблица параметров (настройки) "Режим" - com_regim:\n'
            f'neb_p: Точность расчета (dP) "до" = {get_neb_p}; "после" = {get_neb_p_after};\n'
            f'it_max: Максимальное число итераций (It) "до" = {get_it_max}; "после" = {get_it_max_after};\n'
            f'start: Стартовый алгоритм (Start) "до" = {get_start}; "после" = {get_start_after};\n'
            f'flot: Плоский старт (Пл.старт) "до" = {get_flot}; "после" = {get_flot_after};\n'
            f'dv_min: Мин. допустимое снижение V (dV-) "до" = {get_dv_min}; "после" = {get_dv_min_after};\n'
            f'dv_max: Макс. допустимое превышение V (dV+) "до" = {get_dv_max}; "после" = {get_dv_max_after};\n'
            f'dd_max: Макс. допустимый угол по связи (dDelta) "до" = {get_dd_max}; "после" = {get_dd_max_after};\n'
            f'status: Состояние расчета режима (Статус) "до" = {get_status}; "после" = {get_status_after};\n'
            f'rr: Учет частоты: (W) "до" = {get_rr}; "после" = {get_rr_after};\n'
            f'wt: Отклонение частоты (dF) "до" = {get_wt}; "после" = {get_wt_after};\n'
            f'gen_p: Пересчитывать P/Q узла по P ген (Ген->P) "до" = {get_gen_p}; "после" = {get_gen_p_after};\n'
            f'method: Метод Расчета (Метод) "до" = {get_method}; "после" = {get_method_after};\n'
            f'method_ogr: Метод учета ограничений Q (Метод учета ограничений Q) "до" = {get_method_ogr}; "после" = {get_method_ogr_after};\n'
            f'print_mode: Уровень печати (Печать) "до" = {get_print_mode}; "после" = {get_print_mode_after};\n'
            f'qmax: Точный метод расчета Qmax (Qmax) "до" = {get_qmax}; "после" = {get_qmax_after};\n'
            f'min_x: Сопротивление выключателя (ое на 10-6) (Min_X) "до" = {get_min_x}; "после" = {get_min_x_after};\n'
            f'calc_tr: Пересчет АТ/3х обм. трансформаторов (Транс.) "до" = {get_calc_tr}; "после" = {get_calc_tr_after};\n'
            f'nag_p: Пересчитывать (P/Q) нагрузки узла по ВРДО (Наг->P) "до" = {get_nag_p}; "после" = {get_nag_p_after};\n'
            f'rem_breaker: Удаление выключателей из схемы: (Выкл) "до" = {get_rem_breaker}; "после" = {get_rem_breaker_after};\n'
            f'gram: Пересчет мощности генератора по ГРАМ: (Грам) "до" = {get_gram}; "после" = {get_gram_after};\n'
            f'ctrl_baza: Автоматическое создание БУ (БУ) "до" = {get_ctrl_baza}; "после" = {get_ctrl_baza_after};\n'
            f'itz: Стартовый метод: число итераций (Z_it)  "до" = {get_itz}; "после" = {get_itz_after};\n'
            f'itz_ogr_max: Стартовый метод: Учет Qmax с итерации (Z_it_max) "до" = {get_itz_ogr_max}; "после" = {get_itz_ogr_max_after};\n'
            f'itz_ogr_min: Стартовый метод: Учет Qmin с итерации (Z_it_min) "до" = {get_itz_ogr_min}; "после" = {get_itz_ogr_min_after};\n'
            f'min_nodes_in_island: Минимальное число узлов в острове (Min_nodes) "до" = {get_min_nodes_in_island}; "после" = {get_min_nodes_in_island_after};'
        )
        print(separator_noun)
