# -*- coding: utf-8 -*-
import RastrWinLib.tables.com_regim as com_regim
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.log_tools.tools import separator_noun
from RastrWinLib.tables.tables_attributes import com_regim_table
from RastrWinLib.variables.variable_parametrs import Variable


def set_regim(neb_p: float = 1.000,
              it_max: int = 100,
              start: str = 'Да',
              flot: str = 'Нет',
              dv_min: float = 0.500,
              dv_max: float = 2.000,
              dd_max: float = 5157,
              status: str = 'Нормально',
              rr: str = 'Нет',
              wt: float = 0,
              gen_p: str = 'Да',
              method: str = 'Ньютон',
              method_ogr: str = 'Стандарт',
              print_mode: str = 'Мин',
              qmax: str = 'Нет',
              min_x: float = 0,
              calc_tr: str = 'Нет',
              nag_p: str = 'Нет',
              rem_breaker: str = 'Нет',
              gram: str = 'Нет',
              ctrl_baza: str = 'Нет',
              itz: int = 0,
              itz_ogr_max: int = 0,
              itz_ogr_min: int = 0,
              min_nodes_in_island: int = 0,
              rastr_win: object = RASTR,
              switch_command_line: bool = False):
    """
    Параметры настройки "Общие параметры режима" (таблица "Режим": com_regim):

    :param neb_p: Точность расчета (dP);
    :param it_max: Максимальное число итераций (It);
    :param start: Стартовый алгоритм (Start);
    :param flot: Плоский старт (Пл.старт);
    :param dv_min: Мин. допустимое снижение V (dV-);
    :param dv_max: Макс. допустимое превышение V (dV+);
    :param dd_max: Макс. допустимый угол по связи (dDelta);
    :param status: Состояние расчета режима (Статус);
    :param rr: Учет частоты: (W);
    :param wt: Отклонение частоты (dF);
    :param gen_p: Пересчитывать P/Q узла по P ген (Ген->P);
    :param method: Метод Расчета (Метод);
    :param method_ogr: Метод учета ограничений Q (Метод учета ограничений Q);
    :param print_mode: Уровень печати (Печать);
    :param qmax: Точный метод расчета Qmax (Qmax);
    :param min_x: Сопротивление выключателя (ое на 10-6) (Min_X);
    :param calc_tr: Пересчет АТ/3х обм. трансформаторов (Транс.);
    :param nag_p: Пересчитывать (P/Q) нагрузки узла по ВРДО (Наг->P);
    :param rem_breaker: Удаление выключателей из схемы: (Выкл);
    :param gram: Пересчет мощности генератора по ГРАМ: (Грам);
    :param ctrl_baza: Автоматическое создание БУ (БУ);
    :param itz: Стартовый метод: число итераций (Z_it);
    :param itz_ogr_max: Стартовый метод: Учет Qmax с итерации (Z_it_max);
    :param itz_ogr_min: Стартовый метод: Учет Qmin с итерации (Z_it_min);
    :param min_nodes_in_island: Минимальное число узлов в острове (Min_nodes);
    :param rastr_win: com - объект RastrWin3;
    :param switch_command_line: True/False - вывод сообщений в протакол;
    :return: Nothing returns
    """

    variable_ = Variable(rastr_win=rastr_win)
    get_ = GettingParameter(rastr_win=rastr_win)

    # Точность расчета (dP)
    neb_p_get_before = get_.get_cell(table=com_regim.table,
                                     column=com_regim.neb_p,
                                     row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.neb_p,
                               row_id=0,
                               value=neb_p)
    neb_p_get_after = get_.get_cell(table=com_regim.table,
                                    column=com_regim.neb_p,
                                    row_id=0)

    # Максимальное число итераций (It)
    it_max_get_before = get_.get_cell(table=com_regim.table,
                                      column=com_regim.it_max,
                                      row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.it_max,
                               row_id=0,
                               value=it_max)
    it_max_get_after = get_.get_cell(table=com_regim.table,
                                     column=com_regim.it_max,
                                     row_id=0)

    # Стартовый алгоритм (Start)
    start_get_before = get_.get_cell(table=com_regim.table,
                                     column=com_regim.start,
                                     row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.start,
                               row_id=0,
                               value=start)
    start_get_after = get_.get_cell(table=com_regim.table,
                                    column=com_regim.start,
                                    row_id=0)

    # Плоский старт (Пл.старт)
    flot_get_before = get_.get_cell(table=com_regim.table,
                                    column=com_regim.flot,
                                    row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.flot,
                               row_id=0,
                               value=flot)
    flot_get_after = get_.get_cell(table=com_regim.table,
                                   column=com_regim.flot,
                                   row_id=0)

    # Мин. допустимое снижение V (dV-)
    dv_min_get_before = get_.get_cell(table=com_regim.table,
                                      column=com_regim.dv_min,
                                      row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.dv_min,
                               row_id=0,
                               value=dv_min)
    dv_min_get_after = get_.get_cell(table=com_regim.table,
                                     column=com_regim.dv_min,
                                     row_id=0)

    # Макс. допустимое превышение V (dV+)
    dv_max_get_before = get_.get_cell(table=com_regim.table,
                                      column=com_regim.dv_max,
                                      row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.dv_max,
                               row_id=0,
                               value=dv_max)
    dv_max_get_after = get_.get_cell(table=com_regim.table,
                                     column=com_regim.dv_max,
                                     row_id=0)

    # Макс. допустимый угол по связи (dDelta)
    dd_max_get_before = get_.get_cell(table=com_regim.table,
                                      column=com_regim.dd_max,
                                      row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.dd_max,
                               row_id=0,
                               value=dd_max)
    dd_max_get_after = get_.get_cell(table=com_regim.table,
                                     column=com_regim.dd_max,
                                     row_id=0)

    # Состояние расчета режима (Статус)
    status_get_before = get_.get_cell(table=com_regim.table,
                                      column=com_regim.status,
                                      row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.status,
                               row_id=0,
                               value=status)
    status_get_after = get_.get_cell(table=com_regim.table,
                                     column=com_regim.status,
                                     row_id=0)

    # Учет частоты: (W)
    rr_get_before = get_.get_cell(table=com_regim.table,
                                  column=com_regim.rr,
                                  row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.rr,
                               row_id=0,
                               value=rr)
    rr_get_after = get_.get_cell(table=com_regim.table,
                                 column=com_regim.rr,
                                 row_id=0)

    # Отклонение частоты (dF)
    wt_get_before = get_.get_cell(table=com_regim.table,
                                  column=com_regim.wt,
                                  row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.wt,
                               row_id=0,
                               value=wt)
    wt_get_after = get_.get_cell(table=com_regim.table,
                                 column=com_regim.wt,
                                 row_id=0)

    # Пересчитывать P/Q узла по P ген (Ген->P)
    gen_p_get_before = get_.get_cell(table=com_regim.table,
                                     column=com_regim.gen_p,
                                     row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.gen_p,
                               row_id=0,
                               value=gen_p)
    gen_p_get_after = get_.get_cell(table=com_regim.table,
                                    column=com_regim.gen_p,
                                    row_id=0)

    # Метод Расчета (Метод)
    method_get_before = get_.get_cell(table=com_regim.table,
                                      column=com_regim.method,
                                      row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.method,
                               row_id=0,
                               value=method)
    method_get_after = get_.get_cell(table=com_regim.table,
                                     column=com_regim.method,
                                     row_id=0)

    # Метод учета ограничений Q (Метод учета ограничений Q)
    method_ogr_get_before = get_.get_cell(table=com_regim.table,
                                          column=com_regim.method,
                                          row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.method,
                               row_id=0,
                               value=method_ogr)
    method_ogr_get_after = get_.get_cell(table=com_regim.table,
                                         column=com_regim.method_ogr,
                                         row_id=0)

    # Уровень печати (Печать)
    print_mode_get_before = get_.get_cell(table=com_regim.table,
                                          column=com_regim.print_mode,
                                          row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.print_mode,
                               row_id=0,
                               value=print_mode)
    print_mode_get_after = get_.get_cell(table=com_regim.table,
                                         column=com_regim.print_mode,
                                         row_id=0)

    # Точный метод расчета Qmax (Qmax)
    qmax_get_before = get_.get_cell(table=com_regim.table,
                                    column=com_regim.qmax,
                                    row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.qmax,
                               row_id=0,
                               value=qmax)
    qmax_get_after = get_.get_cell(table=com_regim.table,
                                   column=com_regim.qmax,
                                   row_id=0)

    # Сопротивление выключателя (ое на 10-6) (Min_X)
    min_x_get_before = get_.get_cell(table=com_regim.table,
                                     column=com_regim.min_x,
                                     row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.min_x,
                               row_id=0,
                               value=min_x)
    min_x_get_after = get_.get_cell(table=com_regim.table,
                                    column=com_regim.min_x,
                                    row_id=0)

    # Пересчет АТ/3х обм. трансформаторов (Транс.)
    calc_tr_get_before = get_.get_cell(table=com_regim.table,
                                       column=com_regim.calc_tr,
                                       row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.calc_tr,
                               row_id=0,
                               value=calc_tr)
    calc_tr_get_after = get_.get_cell(table=com_regim.table,
                                      column=com_regim.calc_tr,
                                      row_id=0)

    # Пересчитывать (P/Q) нагрузки узла по ВРДО (Наг->P)
    nag_p_get_before = get_.get_cell(table=com_regim.table,
                                     column=com_regim.nag_p,
                                     row_id=0)
    variable_.make_changes_row(table=com_regim_table,
                               column=com_regim.nag_p,
                               row_id=0,
                               value=nag_p)
    nag_p_get_after = get_.get_cell(table=com_regim.table,
                                    column=com_regim.nag_p,
                                    row_id=0)

    # Удаление выключателей из схемы: (Выкл)
    rem_breaker_get_before = get_.get_cell(table=com_regim.table,
                                           column=com_regim.rem_breaker,
                                           row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.rem_breaker,
                               row_id=0,
                               value=rem_breaker)
    rem_breaker_get_after = get_.get_cell(table=com_regim.table,
                                          column=com_regim.rem_breaker,
                                          row_id=0)

    # Пересчет мощности генератора по ГРАМ: (Грам)
    gram_get_before = get_.get_cell(table=com_regim.table,
                                    column=com_regim.gram,
                                    row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.gram,
                               row_id=0,
                               value=gram)
    gram_get_after = get_.get_cell(table=com_regim.table,
                                   column=com_regim.gram,
                                   row_id=0)

    # Автоматическое создание БУ (БУ)
    ctrl_baza_get_before = get_.get_cell(table=com_regim.table,
                                         column=com_regim.ctrl_baza,
                                         row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.gram,
                               row_id=0,
                               value=ctrl_baza)
    ctrl_baza_get_after = get_.get_cell(table=com_regim.table,
                                        column=com_regim.ctrl_baza,
                                        row_id=0)

    # Стартовый метод: число итераций (Z_it)
    itz_get_before = get_.get_cell(table=com_regim.table,
                                   column=com_regim.itz,
                                   row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.itz,
                               row_id=0,
                               value=itz)
    itz_get_after = get_.get_cell(table=com_regim.table,
                                  column=com_regim.itz,
                                  row_id=0)

    # Стартовый метод: Учет Qmax с итерации (Z_it_max)
    itz_ogr_max_get_before = get_.get_cell(table=com_regim.table,
                                           column=com_regim.itz_ogr_max,
                                           row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.itz_ogr_max,
                               row_id=0,
                               value=itz_ogr_max)
    itz_ogr_max_get_after = get_.get_cell(table=com_regim.table,
                                          column=com_regim.itz_ogr_max,
                                          row_id=0)

    # Стартовый метод: Учет Qmin с итерации (Z_it_min)
    itz_ogr_min_get_before = get_.get_cell(table=com_regim.table,
                                           column=com_regim.itz_ogr_min,
                                           row_id=0)
    variable_.make_changes_row(table=com_regim_table,
                               column=com_regim.itz_ogr_min,
                               row_id=0,
                               value=itz_ogr_min)
    itz_ogr_min_get_after = get_.get_cell(table=com_regim.table,
                                          column=com_regim.itz_ogr_min,
                                          row_id=0)

    # Минимальное число узлов в острове (Min_nodes)
    min_nodes_in_island_get_before = get_.get_cell(table=com_regim.table,
                                                   column=com_regim.min_nodes_in_island,
                                                   row_id=0)
    variable_.make_changes_row(table=com_regim.table,
                               column=com_regim.min_nodes_in_island,
                               row_id=0,
                               value=min_nodes_in_island)
    min_nodes_in_island_get_after = get_.get_cell(table=com_regim.table,
                                                  column=com_regim.min_nodes_in_island,
                                                  row_id=0)

    if switch_command_line is not False:
        print(separator_noun)
        print(
            f'Таблица параметров (настройки) "Режим" - com_regim:\n'
            f'neb_p: Точность расчета (dP) "до" = {neb_p_get_before}; "после" = {neb_p_get_after};\n'
            f'it_max: Максимальное число итераций (It) "до" = {it_max_get_before}; "после" = {it_max_get_after};\n'
            f'start: Стартовый алгоритм (Start) "до" = {start_get_before}; "после" = {start_get_after};\n'
            f'flot: Плоский старт (Пл.старт) "до" = {flot_get_before}; "после" = {flot_get_after};\n'
            f'dv_min: Мин. допустимое снижение V (dV-) "до" = {dv_min_get_before}; "после" = {dv_min_get_after};\n'
            f'dv_max: Макс. допустимое превышение V (dV+) "до" = {dv_max_get_before}; "после" = {dv_max_get_after};\n'
            f'dd_max: Макс. допустимый угол по связи (dDelta) "до" = {dd_max_get_before}; "после" = {dd_max_get_after};\n'
            f'status: Состояние расчета режима (Статус) "до" = {status_get_before}; "после" = {status_get_after};\n'
            f'rr: Учет частоты: (W) "до" = {rr_get_before}; "после" = {rr_get_after};\n'
            f'wt: Отклонение частоты (dF) "до" = {wt_get_before}; "после" = {wt_get_after};\n'
            f'gen_p: Пересчитывать P/Q узла по P ген (Ген->P) "до" = {gen_p_get_before}; "после" = {gen_p_get_after};\n'
            f'method: Метод Расчета (Метод) "до" = {method_get_before}; "после" = {method_get_after};\n'
            f'method_ogr: Метод учета ограничений Q (Метод учета ограничений Q) "до" = {method_ogr_get_before}; "после" = {method_ogr_get_after};\n'
            f'print_mode: Уровень печати (Печать) "до" = {print_mode_get_before}; "после" = {print_mode_get_after};\n'
            f'qmax: Точный метод расчета Qmax (Qmax) "до" = {qmax_get_before}; "после" = {qmax_get_after};\n'
            f'min_x: Сопротивление выключателя (ое на 10-6) (Min_X) "до" = {min_x_get_before}; "после" = {min_x_get_after};\n'
            f'calc_tr: Пересчет АТ/3х обм. трансформаторов (Транс.) "до" = {calc_tr_get_before}; "после" = {calc_tr_get_after};\n'
            f'nag_p: Пересчитывать (P/Q) нагрузки узла по ВРДО (Наг->P) "до" = {nag_p_get_before}; "после" = {nag_p_get_after};\n'
            f'rem_breaker: Удаление выключателей из схемы: (Выкл) "до" = {rem_breaker_get_before}; "после" = {rem_breaker_get_after};\n'
            f'gram: Пересчет мощности генератора по ГРАМ: (Грам) "до" = {gram_get_before}; "после" = {gram_get_after};\n'
            f'ctrl_baza: Автоматическое создание БУ (БУ) "до" = {ctrl_baza_get_before}; "после" = {ctrl_baza_get_after};\n'
            f'itz: Стартовый метод: число итераций (Z_it)  "до" = {itz_get_before}; "после" = {itz_get_after};\n'
            f'itz_ogr_max: Стартовый метод: Учет Qmax с итерации (Z_it_max) "до" = {itz_ogr_max_get_before}; "после" = {itz_ogr_max_get_after};\n'
            f'itz_ogr_min: Стартовый метод: Учет Qmin с итерации (Z_it_min) "до" = {itz_ogr_min_get_before}; "после" = {itz_ogr_min_get_after};\n'
            f'min_nodes_in_island: Минимальное число узлов в острове (Min_nodes) "до" = {min_nodes_in_island_get_before}; "после" = {min_nodes_in_island_get_after};'
        )
        print(separator_noun)
