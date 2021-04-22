# -*- coding: utf-8 -*-

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.log_tools.tools import separator_noun
from RastrWinLib.tables.tables_attributes import com_ekviv_table, com_ekviv_attributes_list
from RastrWinLib.variables.variable_parametrs import Variable


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
                  switch_command_line=False):
    """
    Параметры настройки "Общие параметры эквивалентирования" (таблица "Эквивалент": com_ekviv):

    :param switch_command_line: True/False - вывод сообщений в протакол;
    :param selekv: Отмеченные узлы: (Отмеч);
    :param met_ekv: Метод эквивалентирования (Мет Экв);
    :param tip_ekv: Тип эквивалентирования (Тип Экв);
    :param ekvgen: Эквивалент узлов с фикс V (фиксV);
    :param tip_gen: Тип эквивалентирования генераторов (Тип Ген);
    :param kfc_x: Коэффициент для Xg_ген (К_X_Ген);
    :param pot_gen: Учет потерь при разносе генерации: (dP_Ген);
    :param kpn: Доля нагрузки, пересчитываемая в шунт (d_наг);
    :param tip_sxn: Учитывать СХН при эквивалентировании (СХН);
    :param smart: "Умное" эквивалентирование : (Smart);
    :param zmax: Удаление ветвей с сопротивлением большим: (Z_max);
    :param otm_n: Отмечать узлы после эквивалентирования (Отм);
    """

    variable_ = Variable(rastr_win=RASTR,
                         switch_command_line=False)
    get_ = GettingParameter()

    get_selekv = get_.get_cell(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[0],
                               row_id=0)
    variable_.make_changes_row(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[0],
                               row_id=0,
                               value=selekv)
    get_selekv_after = get_.get_cell(table=com_ekviv_table,
                                     column=com_ekviv_attributes_list[0],
                                     row_id=0)

    get_met_ekv = get_.get_cell(table=com_ekviv_table,
                                column=com_ekviv_attributes_list[1],
                                row_id=0)
    variable_.make_changes_row(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[1],
                               row_id=0,
                               value=met_ekv)
    get_met_ekv_after = get_.get_cell(table=com_ekviv_table,
                                      column=com_ekviv_attributes_list[1],
                                      row_id=0)

    get_tip_ekv = get_.get_cell(table=com_ekviv_table,
                                column=com_ekviv_attributes_list[2],
                                row_id=0)
    variable_.make_changes_row(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[2],
                               row_id=0,
                               value=tip_ekv)
    get_tip_ekv_after = get_.get_cell(table=com_ekviv_table,
                                      column=com_ekviv_attributes_list[2],
                                      row_id=0)

    get_ekvgen = get_.get_cell(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[3],
                               row_id=0)
    variable_.make_changes_row(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[3],
                               row_id=0,
                               value=ekvgen)
    get_ekvgen_after = get_.get_cell(table=com_ekviv_table,
                                     column=com_ekviv_attributes_list[3],
                                     row_id=0)

    get_tip_gen = get_.get_cell(table=com_ekviv_table,
                                column=com_ekviv_attributes_list[4],
                                row_id=0)
    variable_.make_changes_row(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[4],
                               row_id=0,
                               value=tip_gen)
    get_tip_gen_after = get_.get_cell(table=com_ekviv_table,
                                      column=com_ekviv_attributes_list[4],
                                      row_id=0)

    get_kfc_x = get_.get_cell(table=com_ekviv_table,
                              column=com_ekviv_attributes_list[5],
                              row_id=0)
    variable_.make_changes_row(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[5],
                               row_id=0,
                               value=kfc_x)
    get_kfc_x_after = get_.get_cell(table=com_ekviv_table,
                                    column=com_ekviv_attributes_list[5],
                                    row_id=0)

    get_pot_gen = get_.get_cell(table=com_ekviv_table,
                                column=com_ekviv_attributes_list[6],
                                row_id=0)
    variable_.make_changes_row(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[6],
                               row_id=0,
                               value=pot_gen)
    get_pot_gen_after = get_.get_cell(table=com_ekviv_table,
                                      column=com_ekviv_attributes_list[6],
                                      row_id=0)

    get_kpn = get_.get_cell(table=com_ekviv_table,
                            column=com_ekviv_attributes_list[7],
                            row_id=0)
    variable_.make_changes_row(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[7],
                               row_id=0,
                               value=kpn)
    get_kpn_after = get_.get_cell(table=com_ekviv_table,
                                  column=com_ekviv_attributes_list[7],
                                  row_id=0)

    get_tip_sxn = get_.get_cell(table=com_ekviv_table,
                                column=com_ekviv_attributes_list[8],
                                row_id=0)
    variable_.make_changes_row(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[8],
                               row_id=0,
                               value=tip_sxn)
    get_tip_sxn_after = get_.get_cell(table=com_ekviv_table,
                                      column=com_ekviv_attributes_list[8],
                                      row_id=0)

    get_smart = get_.get_cell(table=com_ekviv_table,
                              column=com_ekviv_attributes_list[9],
                              row_id=0)
    variable_.make_changes_row(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[9],
                               row_id=0,
                               value=smart)
    get_smart_after = get_.get_cell(table=com_ekviv_table,
                                    column=com_ekviv_attributes_list[9],
                                    row_id=0)

    get_zmax = get_.get_cell(table=com_ekviv_table,
                             column=com_ekviv_attributes_list[10],
                             row_id=0)
    variable_.make_changes_row(table=com_ekviv_table, column=com_ekviv_attributes_list[10],
                               row_id=0,
                               value=zmax)
    get_zmax_after = get_.get_cell(table=com_ekviv_table,
                                   column=com_ekviv_attributes_list[10],
                                   row_id=0)

    get_otm_n = get_.get_cell(table=com_ekviv_table,
                              column=com_ekviv_attributes_list[11],
                              row_id=0)
    variable_.make_changes_row(table=com_ekviv_table,
                               column=com_ekviv_attributes_list[11],
                               row_id=0,
                               value=otm_n)
    get_otm_n_after = get_.get_cell(table=com_ekviv_table,
                                    column=com_ekviv_attributes_list[11],
                                    row_id=0)

    if switch_command_line is not False:
        print(separator_noun)
        print(
            f'Параметры настройки "Общие параметры эквивалентирования" (таблица "Эквивалент": com_ekviv):\n'
            f'selekv: Отмеченные узлы: (Отмеч) "до" = {get_selekv}; "после" = {get_selekv_after};\n'
            f'met_ekv: Метод эквивалентирования (Мет Экв) "до" = {get_met_ekv}; "после" = {get_met_ekv_after};\n'
            f'tip_ekv: Тип эквивалентирования (Тип Экв) "до" = {get_tip_ekv}; "после" = {get_tip_ekv_after};\n'
            f'ekvgen: Эквивалент узлов с фикс V (фиксV) "до" = {get_ekvgen}; "после" = {get_ekvgen_after};\n'
            f'tip_gen: Тип эквивалентирования генераторов (Тип Ген) "до" = {get_tip_gen}; "после" = {get_tip_gen_after};\n'
            f'kfc_x: Коэффициент для Xg_ген (К_X_Ген) "до" = {get_kfc_x}; "после" = {get_kfc_x_after};\n'
            f'pot_gen: Учет потерь при разносе генерации: (dP_Ген) "до" = {get_pot_gen}; "после" = {get_pot_gen_after};\n'
            f'kpn: Доля нагрузки, пересчитываемая в шунт (d_наг) "до" = {get_kpn}; "после" = {get_kpn_after};\n'
            f'tip_sxn: Учитывать СХН при эквивалентировании (СХН) "до" = {get_tip_sxn}; "после" = {get_tip_sxn_after};\n'
            f'smart: "Умное" эквивалентирование : (Smart) "до" = {get_smart}; "после" = {get_smart_after};\n'
            f'zmax: Удаление ветвей с сопротивлением большим: (Z_max) "до" = {get_zmax}; "после" = {get_zmax_after};\n'
            f'otm_n: Отмечать узлы после эквивалентирования (Отм) "до" = {get_otm_n}; "после" = {get_otm_n_after}.'
        )
        print(separator_noun)
