# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.tables.tables_attributes import ut_common_table, ut_common_attributes_list
from RastrWinLib.variables.variable_parametrs import Variable


def ut_common(
        maxs=5,
        maxv=2,
        maxd=2,
        maxa=10,
        iter=100,
        tip=0,
        f_ots=0,
        add_d=0,
        ekstr=0,
        kfc=1.000,
        sum_kfc=0,
        ds=0,
        it=0,
        Status=0,
        KorrT=25,
        KorrPer=0,
        KorrVib=0,
        enable_contr=0,
        dis_v_contr=0,
        dis_p_contr=0,
        dis_i_contr=0,
        ss_calc=0,
        criterion=0,
        no_crit_d_ba=0,
        no_crit_d_coa=0,
        no_crit_d_ga=0,
        save_files_filter=0,
        save_files_path=0,
        stop_u_n=0,
        dyn_find_pred=0,
        switch_command_line=False,
):
    """

    :param maxs: Точность P (Pmax);
    :param maxv: Точность V (Vmax);
    :param maxd: Точность угла (Dmax);
    :param maxa: Точность P района (Amax);
    :param iter: Макс число итераций (Imax);
    :param tip: Тип утяжеления (Тип);
    :param f_ots: Формировать описания контр. величин: (ФормКВ:);
    :param add_d: Добавлять значения контр. величин после шага (ДобКЗ);
    :param ekstr: Поиск экстремума по контролируемым величинам (Экстремум);
    :param kfc: Текущий шаг (Шаг);
    :param sum_kfc: Сумарный шаг (Шаг_Сумм);
    :param ds: Деление шага (ДелШаг);
    :param it: Текущая итерация (Итер);
    :param Status: Состояние утяжеления (Статус);
    :param KorrT: коррекция по температуре: температура, Гр. (KorrT);
    :param KorrPer: коррекция по температуре: перегрузка % (KorrPer);
    :param KorrVib: коррекция по температуре: выборка (KorrVib);
    :param enable_contr: Включить контроль всех ограничений U,P,I (Включить контр. U,P,I);
    :param dis_v_contr: Отключить контроль всех ограничений по напряжению U (Откл контр. U);
    :param dis_p_contr: Отключить контроль всех ограничений по мощности P (Откл контр. P);
    :param dis_i_contr: Отключить контроль всех ограничений по току I (Откл контр. I);
    :param ss_calc: Как расчитывать УР при утяжелении (Расчет УР);
    :param criterion: Критерий устойчивости (Критерий);
    :param no_crit_d_ba: Динамика:не учет критерия разворота угла по ЛЭП (Нет критерия: угол по ЛЭП);
    :param no_crit_d_coa: Динамика:не учет критерия угла генератора и COA (Нет критерия: угол по Генератору);
    :param no_crit_d_ga: Динамика:не учет критерия срабатывания автомата безопасности генератора (Нет критерия: автомат безопасности ген.);
    :param save_files_filter: Критерий сохранения файлов (Критерий);
    :param save_files_path: Папка для сохранения файлов результатов (Путь);
    :param stop_u_n: Остановить при переходе к устойчивому/неустойчивому (Остановить);
    :param dyn_find_pred: Динамика: поиск предела (Динамика: поиск предела);
    :param switch_command_line: True/False - вывод сообщений в протокол;
    :return:
    """
    variable_def_rowid = Variable(rastr_win=RASTR,
                                  switch_command_line=switch_command_line)
    get_ = GettingParameter()

    get_maxs = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[0], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[0], row_id=0,
                                        value=float(maxs))
    get_maxs_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[0], row_id=0)

    get_maxv = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[1], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[1], row_id=0,
                                        value=float(maxv))
    get_maxv_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[1], row_id=0)

    get_maxd = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[2], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[2], row_id=0,
                                        value=float(maxd))
    get_maxd_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[2], row_id=0)

    get_maxa = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[3], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[3], row_id=0,
                                        value=float(maxa))
    get_maxa_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[3], row_id=0)

    get_iter = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[4], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[4], row_id=0,
                                        value=float(iter))
    get_iter_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[4], row_id=0)

    get_tip = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[5], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[5], row_id=0,
                                        value=float(tip))
    get_tip_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[5], row_id=0)

    get_f_ots = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[6], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[6], row_id=0,
                                        value=float(f_ots))
    get_f_ots_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[6], row_id=0)

    get_add_d = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[7], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[7], row_id=0,
                                        value=float(add_d))
    get_add_d_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[7], row_id=0)

    get_ekstr = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[8], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[8], row_id=0,
                                        value=float(ekstr))
    get_ekstr_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[8], row_id=0)

    get_kfc = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[9], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[9], row_id=0,
                                        value=float(kfc))
    get_kfc_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[9], row_id=0)

    get_sum_kfc = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[10], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[10], row_id=0,
                                        value=float(sum_kfc))
    get_sum_kfc_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[10], row_id=0)

    get_ds = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[11], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[11], row_id=0,
                                        value=float(ds))
    get_ds_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[11], row_id=0)

    get_it = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[12], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[12], row_id=0,
                                        value=float(it))
    get_it_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[12], row_id=0)

    get_status = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[13], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[13], row_id=0,
                                        value=float(Status))
    get_status_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[13], row_id=0)

    get_korr_t = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[14], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[14], row_id=0,
                                        value=float(KorrT))
    get_korr_t_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[14], row_id=0)

    get_korr_per = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[15], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[15], row_id=0,
                                        value=float(KorrPer))
    get_korr_per_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[15], row_id=0)

    get_korr_vib = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[16], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[16], row_id=0,
                                        value=float(KorrVib))
    get_korr_vib_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[16], row_id=0)

    get_enable_contr = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[17], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[17], row_id=0,
                                        value=float(enable_contr))
    get_enable_contr_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[17], row_id=0)

    get_dis_v_contr = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[18], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[18], row_id=0,
                                        value=float(dis_v_contr))
    get_dis_v_contr_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[18], row_id=0)

    get_dis_p_contr = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[19], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[19], row_id=0,
                                        value=float(dis_p_contr))
    get_dis_p_contr_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[19], row_id=0)

    get_dis_i_contr = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[20], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[20], row_id=0,
                                        value=float(dis_i_contr))
    get_dis_i_contr_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[20], row_id=0)

    get_ss_calc = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[21], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[21], row_id=0,
                                        value=float(ss_calc))
    get_ss_calc_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[21], row_id=0)

    get_criterion = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[22], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[22], row_id=0,
                                        value=float(criterion))
    get_criterion_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[22], row_id=0)

    get_no_crit_d_ba = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[23], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[23], row_id=0,
                                        value=float(no_crit_d_ba))
    get_no_crit_d_ba_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[23], row_id=0)

    get_no_crit_d_coa = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[24], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[24], row_id=0,
                                        value=float(no_crit_d_coa))
    get_no_crit_d_coa_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[24], row_id=0)

    get_no_crit_d_ga = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[25], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[25], row_id=0,
                                        value=float(no_crit_d_ga))
    get_no_crit_d_ga_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[25], row_id=0)

    get_save_files_filter = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[26], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[26], row_id=0,
                                        value=float(save_files_filter))
    get_save_files_filter_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[26], row_id=0)

    get_save_files_path = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[27], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[27], row_id=0,
                                        value=float(save_files_path))
    get_save_files_path_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[27], row_id=0)

    get_stop_u_n = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[28], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[28], row_id=0,
                                        value=float(stop_u_n))
    get_stop_u_n_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[28], row_id=0)

    get_dyn_find_pred = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[29], row_id=0)
    variable_def_rowid.make_changes_row(table=ut_common_table, column=ut_common_attributes_list[29], row_id=0,
                                        value=float(dyn_find_pred))
    get_dyn_find_pred_after = get_.get_cell(table=ut_common_table, column=ut_common_attributes_list[29], row_id=0)

    if switch_command_line is not False:
        print(' '
              f'maxs: Точность P (Pmax) "до" = {get_maxs}; "после" = {get_maxs_after};'
              f'maxv: Точность V (Vmax) "до" = {get_maxv}; "после" = {get_maxv_after};'
              f'maxd: Точность угла (Dmax) "до" = {get_maxd}; "после" = {get_maxd_after};'
              f'maxa: Точность P района (Amax) "до" = {get_maxa}; "после" = {get_maxa_after};'
              f'iter: Макс число итераций (Imax) "до" = {get_iter}; "после" = {get_iter_after};'
              f'tip: Тип утяжеления (Тип) "до" = {get_tip}; "после" = {get_tip_after};'
              f'f_ots: Формировать описания контр. величин: (ФормКВ:) "до" = {get_f_ots}; "после" = {get_f_ots_after};'
              f'add_d: Добавлять значения контр. величин после шага (ДобКЗ) "до" = {get_add_d}; "после" = {get_add_d_after};'
              f'ekstr: Поиск экстремума по контролируемым величинам (Экстремум) "до" = {get_ekstr}; "после" = {get_ekstr_after};'
              f'kfc: Текущий шаг (Шаг) "до" = {get_kfc}; "после" = {get_kfc_after};'
              f'sum_kfc: Сумарный шаг (Шаг_Сумм) "до" = {get_sum_kfc}; "после" = {get_sum_kfc_after};'
              f'ds: Деление шага (ДелШаг) "до" = {get_ds}; "после" = {get_ds_after};'
              f'it: Текущая итерация (Итер) "до" = {get_it}; "после" = {get_it_after};'
              f'Status: Состояние утяжеления (Статус) "до" = {get_status}; "после" = {get_status_after};'
              f'KorrT: коррекция по температуре: температура, Гр. (KorrT) "до" = {get_korr_t}; "после" = {get_korr_t_after};'
              f'KorrPer: коррекция по температуре: перегрузка % (KorrPer) "до" = {get_korr_per}; "после" = {get_korr_per_after};'
              f'KorrVib: коррекция по температуре: выборка (KorrVib) "до" = {get_korr_vib}; "после" = {get_korr_vib_after};'
              f'enable_contr: Включить контроль всех ограничений U,P,I (Включить контр. U,P,I) "до" = {get_enable_contr}; "после" = {get_enable_contr_after};'
              f'dis_v_contr: Отключить контроль всех ограничений по напряжению U (Откл контр. U) "до" = {get_dis_v_contr}; "после" = {get_dis_v_contr_after};'
              f'dis_p_contr: Отключить контроль всех ограничений по мощности P (Откл контр. P) "до" = {get_dis_p_contr}; "после" = {get_dis_p_contr_after};'
              f'dis_i_contr: Отключить контроль всех ограничений по току I (Откл контр. I) "до" = {get_dis_i_contr}; "после" = {get_dis_i_contr_after};'
              f'ss_calc: Как расчитывать УР при утяжелении (Расчет УР) "до" = {get_ss_calc}; "после" = {get_ss_calc_after};'
              f'criterion: Критерий устойчивости (Критерий) "до" = {get_criterion}; "после" = {get_criterion_after};'
              f'no_crit_d_ba: Динамика:не учет критерия разворота угла по ЛЭП (Нет критерия: угол по ЛЭП) "до" = {get_no_crit_d_ba}; "после" = {get_no_crit_d_ba_after};'
              f'no_crit_d_coa: Динамика:не учет критерия угла генератора и COA (Нет критерия: угол по Генератору) "до" = {get_no_crit_d_coa}; "после" = {get_no_crit_d_coa_after};'
              f'no_crit_d_ga: Динамика:не учет критерия срабатывания автомата безопасности генератора (Нет критерия: автомат безопасности ген.) "до" = {get_no_crit_d_ga}; "после" = {get_no_crit_d_ga_after};'
              f'save_files_filter: Критерий сохранения файлов (Критерий) "до" = {get_save_files_filter}; "после" = {get_save_files_filter_after};'
              f'save_files_path: Папка для сохранения файлов результатов (Путь) "до" = {get_save_files_path}; "после" = {get_save_files_path_after};'
              f'stop_u_n: Остановить при переходе к устойчивому/неустойчивому (Остановить) "до" = {get_stop_u_n}; "после" = {get_stop_u_n_after};'
              f'dyn_find_pred: Динамика: поиск предела (Динамика: поиск предела) "до" = {get_dyn_find_pred}; "после" = {get_dyn_find_pred_after};'
              f'switch_command_line: True/False - вывод сообщений в протокол;')
