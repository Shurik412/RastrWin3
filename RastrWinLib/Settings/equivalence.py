# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.operation.get import GettingParameter
from RastrWinLib.Tools.tools import Tools
from RastrWinLib.Tables.Settings.com_ekviv import ComEkviv
from RastrWinLib.operation.Variable import Variable


def set_com_ekviv(selekv=0,
                  met_ekv=0,
                  tip_ekv=0,
                  ekvgen=0,
                  tip_gen=1,
                  kfc_x=0,
                  pot_gen=0,
                  kpn=0,
                  tip_sxn=0,
                  smart=0,
                  zmax=1000,
                  otm_n=0,
                  rastr_win=RASTR,
                  switch_command_line=False):
    f"""
    Параметры настройки "Общие параметры эквивалентирования" (таблица "Эквивалент": com_ekviv):

    :param selekv: Отмеченные узлы: (Отмеч);
    :param met_ekv: Метод эквивалентирования: (Мет Экв);
    :param tip_ekv: Тип эквивалентирования: (Тип Экв);
    :param ekvgen: Эквивалент узлов с фикс V: (фиксV);
    :param tip_gen: Тип эквивалентирования генераторов: (Тип Ген);
    :param kfc_x: Коэффициент для Xg_ген: (К_X_Ген);
    :param pot_gen: Учет потерь при разносе генерации: (dP_Ген);
    :param kpn: Доля нагрузки, пересчитываемая в шунт: (d_наг);
    :param tip_sxn: Учитывать СХН при эквивалентировании: (СХН);
    :param smart: "Умное" эквивалентирование: (Smart);
    :param zmax: Удаление ветвей с сопротивлением большим: (Z_max);
    :param otm_n: Отмечать узлы после эквивалентирования: (Отм);
    :param rastr_win: {Tools.RastrDoc};
    :param switch_command_line: {Tools.switch_command_line_doc};
    :return: Nothing returns
    """

    variable_ = Variable(rastr_win=rastr_win,
                         switch_command_line=False)
    get_ = GettingParameter(rastr_win=rastr_win)

    # selekv Отмеченные узлы: (Отмеч)
    selekv_get_before = get_.get_cell_row(table=ComEkviv.table,
                                          column=ComEkviv.selekv,
                                          row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.selekv,
                               row_id=0,
                               value=selekv)
    selekv_get_after = get_.get_cell_row(table=ComEkviv.table,
                                         column=ComEkviv.selekv,
                                         row_id=0)

    # met_ekv Метод эквивалентирования (Мет Экв)
    met_ekv_get_before = get_.get_cell_row(table=ComEkviv.table,
                                           column=ComEkviv.met_ekv,
                                           row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.met_ekv,
                               row_id=0,
                               value=met_ekv)
    met_ekv_get_after = get_.get_cell_row(table=ComEkviv.table,
                                          column=ComEkviv.met_ekv,
                                          row_id=0)

    # tip_ekv Тип эквивалентирования (Тип Экв)
    tip_ekv_get_before = get_.get_cell_row(table=ComEkviv.table,
                                           column=ComEkviv.tip_ekv,
                                           row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.tip_ekv,
                               row_id=0,
                               value=tip_ekv)
    tip_ekv_get_after = get_.get_cell_row(table=ComEkviv.table,
                                          column=ComEkviv.tip_ekv,
                                          row_id=0)

    # ekvgen Эквивалент узлов с фикс V (фиксV)
    ekvgen_get_before = get_.get_cell_row(table=ComEkviv.table,
                                          column=ComEkviv.ekvgen,
                                          row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.ekvgen,
                               row_id=0,
                               value=ekvgen)
    ekvgen_get_after = get_.get_cell_row(table=ComEkviv.table,
                                         column=ComEkviv.ekvgen,
                                         row_id=0)

    # tip_gen Тип эквивалентирования генераторов (Тип Ген)
    tip_gen_get_before = get_.get_cell_row(table=ComEkviv.table,
                                           column=ComEkviv.tip_gen,
                                           row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.tip_gen,
                               row_id=0,
                               value=tip_gen)
    tip_gen_get_after = get_.get_cell_row(table=ComEkviv.table,
                                          column=ComEkviv.tip_gen,
                                          row_id=0)

    # kfc_x Коэффициент для Xg_ген (К_X_ Ген)
    kfc_x_get_before = get_.get_cell_row(table=ComEkviv.table,
                                         column=ComEkviv.kfc_x,
                                         row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.kfc_x,
                               row_id=0,
                               value=kfc_x)
    kfc_x_get_after = get_.get_cell_row(table=ComEkviv.table,
                                        column=ComEkviv.kfc_x,
                                        row_id=0)

    # pot_gen Учет потерь при разносе генерации: (dP_Ген)
    pot_gen_get_before = get_.get_cell_row(table=ComEkviv.table,
                                           column=ComEkviv.pot_gen,
                                           row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.pot_gen,
                               row_id=0,
                               value=pot_gen)
    pot_gen_get_after = get_.get_cell_row(table=ComEkviv.table,
                                          column=ComEkviv.pot_gen,
                                          row_id=0)

    # kpn Доля нагрузки, пересчитываемая в шунт (d_наг)
    kpn_get_before = get_.get_cell_row(table=ComEkviv.table,
                                       column=ComEkviv.kpn,
                                       row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.kpn,
                               row_id=0,
                               value=kpn)
    kpn_get_after = get_.get_cell_row(table=ComEkviv.table,
                                      column=ComEkviv.kpn,
                                      row_id=0)

    # tip_sxn Учитывать СХН при эквивалентировании (СХН)
    tip_sxn_get_before = get_.get_cell_row(table=ComEkviv.table,
                                           column=ComEkviv.tip_sxn,
                                           row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.tip_sxn,
                               row_id=0,
                               value=tip_sxn)
    tip_sxn_get_after = get_.get_cell_row(table=ComEkviv.table,
                                          column=ComEkviv.tip_sxn,
                                          row_id=0)

    # smart "Умное" эквивалентирование : (Smart)
    smart_get_before = get_.get_cell_row(table=ComEkviv.table,
                                         column=ComEkviv.smart,
                                         row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.smart,
                               row_id=0,
                               value=smart)
    smart_get_after = get_.get_cell_row(table=ComEkviv.table,
                                        column=ComEkviv.smart,
                                        row_id=0)

    # zmax Удаление ветвей с сопротивлением большим: (Z_max)
    zmax_get_before = get_.get_cell_row(table=ComEkviv.table,
                                        column=ComEkviv.zmax,
                                        row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.zmax,
                               row_id=0,
                               value=zmax)
    zmax_get_after = get_.get_cell_row(table=ComEkviv.table,
                                       column=ComEkviv.zmax,
                                       row_id=0)

    # otm_n Отмечать узлы после эквивалентирования (Отм)
    otm_n_get_before = get_.get_cell_row(table=ComEkviv.table,
                                         column=ComEkviv.otm_n,
                                         row_id=0)
    variable_.make_changes_row(table=ComEkviv.table,
                               column=ComEkviv.otm_n,
                               row_id=0,
                               value=otm_n)
    otm_n_get_after = get_.get_cell_row(table=ComEkviv.table,
                                        column=ComEkviv.otm_n,
                                        row_id=0)

    if switch_command_line is not False:
        print(
            f'{Tools.separator_noun}\n'
            f'Параметры настройки "Общие параметры эквивалентирования" (таблица "Эквивалент": com_ekviv):\n\n'
            f'selekv: Отмеченные узлы: (Отмеч) "до" = {selekv_get_before}; "после" = {selekv_get_after};\n'
            f'met_ekv: Метод эквивалентирования: (Мет Экв) "до" = {met_ekv_get_before}; "после" = {met_ekv_get_after};\n'
            f'tip_ekv: Тип эквивалентирования: (Тип Экв) "до" = {tip_ekv_get_before}; "после" = {tip_ekv_get_after};\n'
            f'ekvgen: Эквивалент узлов с фикс V: (фиксV) "до" = {ekvgen_get_before}; "после" = {ekvgen_get_after};\n'
            f'tip_gen: Тип эквивалентирования генераторов: (Тип Ген) "до" = {tip_gen_get_before}; "после" = {tip_gen_get_after};\n'
            f'kfc_x: Коэффициент для Xg_ген: (К_X_Ген) "до" = {kfc_x_get_before}; "после" = {kfc_x_get_after};\n'
            f'pot_gen: Учет потерь при разносе генерации: (dP_Ген) "до" = {pot_gen_get_before}; "после" = {pot_gen_get_after};\n'
            f'kpn: Доля нагрузки, пересчитываемая в шунт: (d_наг) "до" = {kpn_get_before}; "после" = {kpn_get_after};\n'
            f'tip_sxn: Учитывать СХН при эквивалентировании: (СХН) "до" = {tip_sxn_get_before}; "после" = {tip_sxn_get_after};\n'
            f'smart: "Умное" эквивалентирование: (Smart) "до" = {smart_get_before}; "после" = {smart_get_after};\n'
            f'zmax: Удаление ветвей с сопротивлением большим: (Z_max) "до" = {zmax_get_before}; "после" = {zmax_get_after};\n'
            f'otm_n: Отмечать узлы после эквивалентирования: (Отм) "до" = {otm_n_get_before}; "после" = {otm_n_get_after}.'
            f'{Tools.separator_noun}\n'
        )
    return (
        f'{Tools.separator_noun}\n'
        f'Параметры настройки "Общие параметры эквивалентирования" (таблица "Эквивалент": com_ekviv):\n'
        f'selekv: Отмеченные узлы: (Отмеч) "до" = {selekv_get_before}; "после" = {selekv_get_after};\n'
        f'met_ekv: Метод эквивалентирования: (Мет Экв) "до" = {met_ekv_get_before}; "после" = {met_ekv_get_after};\n'
        f'tip_ekv: Тип эквивалентирования: (Тип Экв) "до" = {tip_ekv_get_before}; "после" = {tip_ekv_get_after};\n'
        f'ekvgen: Эквивалент узлов с фикс V: (фиксV) "до" = {ekvgen_get_before}; "после" = {ekvgen_get_after};\n'
        f'tip_gen: Тип эквивалентирования генераторов: (Тип Ген) "до" = {tip_gen_get_before}; "после" = {tip_gen_get_after};\n'
        f'kfc_x: Коэффициент для Xg_ген: (К_X_Ген) "до" = {kfc_x_get_before}; "после" = {kfc_x_get_after};\n'
        f'pot_gen: Учет потерь при разносе генерации: (dP_Ген) "до" = {pot_gen_get_before}; "после" = {pot_gen_get_after};\n'
        f'kpn: Доля нагрузки, пересчитываемая в шунт: (d_наг) "до" = {kpn_get_before}; "после" = {kpn_get_after};\n'
        f'tip_sxn: Учитывать СХН при эквивалентировании: (СХН) "до" = {tip_sxn_get_before}; "после" = {tip_sxn_get_after};\n'
        f'smart: "Умное" эквивалентирование: (Smart) "до" = {smart_get_before}; "после" = {smart_get_after};\n'
        f'zmax: Удаление ветвей с сопротивлением большим: (Z_max) "до" = {zmax_get_before}; "после" = {zmax_get_after};\n'
        f'otm_n: Отмечать узлы после эквивалентирования: (Отм) "до" = {otm_n_get_before}; "после" = {otm_n_get_after}.'
        f'{Tools.separator_noun}\n'
    )
