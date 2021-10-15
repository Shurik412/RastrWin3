# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Getting.get import GettingParameter
from RastrWinLib.Tools.tools import Tools
from RastrWinLib.Tables.Settings.ut_common import UtCommon
from RastrWinLib.Variables.variable_parametrs import Variable


def set_ut_common(
        maxs: float = 5.0,
        maxv: float = 2.0,
        maxd: float = 2.0,
        maxa: float = 10.0,
        iter: int = 100,
        tip: str = 'Стандарт',
        f_ots: str = 'Нет',
        add_d: str = 'Нет',
        ekstr: str = 'Нет',
        kfc: float = 1.000,
        sum_kfc: float = 0.000,
        ds: str = 'Откл',
        it: int = 0,
        Status: str = 'Норма',
        KorrT: float = 25.000,
        KorrPer: float = 0.000,
        KorrVib: str = 0,
        enable_contr: bool = False,
        dis_v_contr: bool = False,
        dis_p_contr: bool = False,
        dis_i_contr: bool = False,
        ss_calc: str = 'Плоский старт',
        criterion: str = 'уст. реж.',
        no_crit_d_ba: bool = False,
        no_crit_d_coa: bool = False,
        no_crit_d_ga: bool = False,
        save_files_filter: str = 'Не сохранять',
        save_files_path: str = 'c:\\tmp\\',
        stop_u_n: bool = False,
        dyn_find_pred: bool = False,
        rastr_win: object = RASTR,
        switch_command_line: bool = False
):
    f"""
    Параметры настройки "Общие данные для утяжеления" (таблица "Утяжеление": ut_common):

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
    :param rastr_win: {Tools.RastrDoc};
    :param switch_command_line: {Tools.switch_command_line_doc};
    :return: Nothing returns
    """
    variable_ = Variable(rastr_win=rastr_win)
    get_ = GettingParameter(rastr_win=rastr_win)

    maxs_get_before = get_.get_cell_row(table=UtCommon.table,
                                        column=UtCommon.maxs,
                                        row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.maxs,
                               row_id=0,
                               value=maxs)
    maxs_get_after = get_.get_cell_row(table=UtCommon.table,
                                       column=UtCommon.maxs,
                                       row_id=0)

    maxv_get_before = get_.get_cell_row(table=UtCommon.table,
                                        column=UtCommon.maxv,
                                        row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.maxv,
                               row_id=0,
                               value=maxv)
    maxv_get_after = get_.get_cell_row(table=UtCommon.table,
                                       column=UtCommon.maxv,
                                       row_id=0)

    maxd_get_before = get_.get_cell_row(table=UtCommon.table,
                                        column=UtCommon.maxd,
                                        row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.maxd,
                               row_id=0,
                               value=maxd)
    maxd_get_after = get_.get_cell_row(table=UtCommon.table,
                                       column=UtCommon.maxd,
                                       row_id=0)

    maxa_get_before = get_.get_cell_row(table=UtCommon.table,
                                        column=UtCommon.maxa,
                                        row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.maxa,
                               row_id=0,
                               value=maxa)
    maxa_get_after = get_.get_cell_row(table=UtCommon.table,
                                       column=UtCommon.maxa,
                                       row_id=0)

    iter_get_before = get_.get_cell_row(table=UtCommon.table,
                                        column=UtCommon.iter,
                                        row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.maxa,
                               row_id=0,
                               value=iter)
    iter_get_after = get_.get_cell_row(table=UtCommon.table,
                                       column=UtCommon.iter,
                                       row_id=0)

    tip_get_before = get_.get_cell_row(table=UtCommon.table,
                                       column=UtCommon.tip,
                                       row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.tip,
                               row_id=0,
                               value=tip)
    tip_get_after = get_.get_cell_row(table=UtCommon.table,
                                      column=UtCommon.tip,
                                      row_id=0)

    f_ots_get_before = get_.get_cell_row(table=UtCommon.table,
                                         column=UtCommon.f_ots,
                                         row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.f_ots,
                               row_id=0,
                               value=f_ots)
    f_ots_get_after = get_.get_cell_row(table=UtCommon.table,
                                        column=UtCommon.f_ots,
                                        row_id=0)

    add_d_get_before = get_.get_cell_row(table=UtCommon.table,
                                         column=UtCommon.add_d,
                                         row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.add_d,
                               row_id=0,
                               value=add_d)
    add_d_get_after = get_.get_cell_row(table=UtCommon.table,
                                        column=UtCommon.add_d,
                                        row_id=0)

    ekstr_get_before = get_.get_cell_row(table=UtCommon.table,
                                         column=UtCommon.ekstr,
                                         row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.ekstr,
                               row_id=0,
                               value=ekstr)
    ekstr_get_after = get_.get_cell_row(table=UtCommon.table,
                                        column=UtCommon.ekstr,
                                        row_id=0)

    kfc_get_before = get_.get_cell_row(table=UtCommon.table,
                                       column=UtCommon.kfc,
                                       row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.kfc,
                               row_id=0,
                               value=kfc)
    kfc_get_after = get_.get_cell_row(table=UtCommon.table,
                                      column=UtCommon.kfc,
                                      row_id=0)

    sum_kfc_get_before = get_.get_cell_row(table=UtCommon.table,
                                           column=UtCommon.sum_kfc,
                                           row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.sum_kfc,
                               row_id=0,
                               value=sum_kfc)
    sum_kfc_get_after = get_.get_cell_row(table=UtCommon.table,
                                          column=UtCommon.sum_kfc,
                                          row_id=0)

    ds_get_before = get_.get_cell_row(table=UtCommon.table,
                                      column=UtCommon.ds,
                                      row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.ds,
                               row_id=0,
                               value=ds)
    ds_get_after = get_.get_cell_row(table=UtCommon.table,
                                     column=UtCommon.ds,
                                     row_id=0)

    it_get_before = get_.get_cell_row(table=UtCommon.table,
                                      column=UtCommon.it,
                                      row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.it,
                               row_id=0,
                               value=it)
    it_get_after = get_.get_cell_row(table=UtCommon.table,
                                     column=UtCommon.it,
                                     row_id=0)

    status_get_before = get_.get_cell_row(table=UtCommon.table,
                                          column=UtCommon.Status,
                                          row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.Status,
                               row_id=0,
                               value=Status)
    status_get_after = get_.get_cell_row(table=UtCommon.table,
                                         column=UtCommon.Status,
                                         row_id=0)

    korr_t_get_before = get_.get_cell_row(table=UtCommon.table,
                                          column=UtCommon.KorrT,
                                          row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.KorrT,
                               row_id=0,
                               value=KorrT)
    korr_t_get_after = get_.get_cell_row(table=UtCommon.table,
                                         column=UtCommon.KorrT,
                                         row_id=0)

    korr_per_get_before = get_.get_cell_row(table=UtCommon.table,
                                            column=UtCommon.KorrPer,
                                            row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.KorrPer,
                               row_id=0,
                               value=KorrPer)
    korr_per_get_after = get_.get_cell_row(table=UtCommon.table,
                                           column=UtCommon.KorrPer,
                                           row_id=0)

    korr_vib_get_before = get_.get_cell_row(table=UtCommon.table,
                                            column=UtCommon.KorrVib,
                                            row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.KorrVib,
                               row_id=0,
                               value=KorrVib)
    korr_vib_get_after = get_.get_cell_row(table=UtCommon.table,
                                           column=UtCommon.KorrVib,
                                           row_id=0)

    enable_contr_get_before = get_.get_cell_row(table=UtCommon.table,
                                                column=UtCommon.enable_contr,
                                                row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.enable_contr,
                               row_id=0,
                               value=enable_contr)
    enable_contr_get_after = get_.get_cell_row(table=UtCommon.table,
                                               column=UtCommon.enable_contr,
                                               row_id=0)

    dis_v_contr_get_before = get_.get_cell_row(table=UtCommon.table,
                                               column=UtCommon.dis_v_contr,
                                               row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.dis_v_contr,
                               row_id=0,
                               value=dis_v_contr)
    dis_v_contr_get_after = get_.get_cell_row(table=UtCommon.table,
                                              column=UtCommon.dis_v_contr,
                                              row_id=0)

    dis_p_contr_get_before = get_.get_cell_row(table=UtCommon.table,
                                               column=UtCommon.dis_p_contr,
                                               row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.dis_p_contr,
                               row_id=0,
                               value=dis_p_contr)
    dis_p_contr_get_after = get_.get_cell_row(table=UtCommon.table,
                                              column=UtCommon.dis_p_contr,
                                              row_id=0)

    dis_i_contr_get_before = get_.get_cell_row(table=UtCommon.table,
                                               column=UtCommon.dis_i_contr,
                                               row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.dis_i_contr,
                               row_id=0,
                               value=dis_i_contr)
    dis_i_contr_get_after = get_.get_cell_row(table=UtCommon.table,
                                              column=UtCommon.dis_i_contr,
                                              row_id=0)

    ss_calc_get_before = get_.get_cell_row(table=UtCommon.table,
                                           column=UtCommon.ss_calc,
                                           row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.ss_calc,
                               row_id=0,
                               value=ss_calc)
    ss_calc_get_after = get_.get_cell_row(table=UtCommon.table,
                                          column=UtCommon.ss_calc,
                                          row_id=0)

    criterion_get_before = get_.get_cell_row(table=UtCommon.table,
                                             column=UtCommon.criterion,
                                             row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.criterion,
                               row_id=0,
                               value=criterion)
    criterion_get_after = get_.get_cell_row(table=UtCommon.table,
                                            column=UtCommon.criterion,
                                            row_id=0)

    no_crit_d_ba_get_before = get_.get_cell_row(table=UtCommon.table,
                                                column=UtCommon.no_crit_d_ba,
                                                row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.no_crit_d_ba,
                               row_id=0,
                               value=no_crit_d_ba)
    no_crit_d_ba_get_after = get_.get_cell_row(table=UtCommon.table,
                                               column=UtCommon.no_crit_d_ba,
                                               row_id=0)

    no_crit_d_coa_get_before = get_.get_cell_row(table=UtCommon.table,
                                                 column=UtCommon.no_crit_d_coa,
                                                 row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.no_crit_d_coa,
                               row_id=0,
                               value=no_crit_d_coa)
    no_crit_d_coa_get_after = get_.get_cell_row(table=UtCommon.table,
                                                column=UtCommon.no_crit_d_coa,
                                                row_id=0)

    no_crit_d_ga_get_before = get_.get_cell_row(table=UtCommon.table,
                                                column=UtCommon.no_crit_d_ga,
                                                row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.no_crit_d_ga,
                               row_id=0,
                               value=no_crit_d_ga)
    no_crit_d_ga_get_after = get_.get_cell_row(table=UtCommon.table,
                                               column=UtCommon.no_crit_d_ga,
                                               row_id=0)

    save_files_filter_get_before = get_.get_cell_row(table=UtCommon.table,
                                                     column=UtCommon.save_files_filter,
                                                     row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.save_files_filter,
                               row_id=0,
                               value=save_files_filter)
    save_files_filter_get_after = get_.get_cell_row(table=UtCommon.table,
                                                    column=UtCommon.save_files_filter,
                                                    row_id=0)

    save_files_path_get_before = get_.get_cell_row(table=UtCommon.table,
                                                   column=UtCommon.save_files_path,
                                                   row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.save_files_path,
                               row_id=0,
                               value=save_files_path)
    save_files_path_get_after = get_.get_cell_row(table=UtCommon.table,
                                                  column=UtCommon.save_files_path,
                                                  row_id=0)

    stop_u_n_get_before = get_.get_cell_row(table=UtCommon.table,
                                            column=UtCommon.stop_u_n,
                                            row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.stop_u_n,
                               row_id=0,
                               value=stop_u_n)
    stop_u_n_get_after = get_.get_cell_row(table=UtCommon.table,
                                           column=UtCommon.stop_u_n,
                                           row_id=0)

    dyn_find_pred_get_before = get_.get_cell_row(table=UtCommon.table,
                                                 column=UtCommon.dyn_find_pred,
                                                 row_id=0)
    variable_.make_changes_row(table=UtCommon.table,
                               column=UtCommon.dyn_find_pred,
                               row_id=0,
                               value=dyn_find_pred)
    dyn_find_pred_get_after = get_.get_cell_row(table=UtCommon.table,
                                                column=UtCommon.dyn_find_pred,
                                                row_id=0)

    if switch_command_line is not False:
        print(Tools.separator_noun)
        print(
            f'Таблица параметров (настройки) "Утяжеление":\n'
            f'- maxs: Точность P (Pmax): "до" = {maxs_get_before}; "после" = {maxs_get_after};\n'
            f'- maxv: Точность V (Vmax): "до" = {maxv_get_before}; "после" = {maxv_get_after};\n'
            f'- maxd: Точность угла (Dmax): "до" = {maxd_get_before}; "после" = {maxd_get_after};\n'
            f'- maxa: Точность P района (Amax): "до" = {maxa_get_before}; "после" = {maxa_get_after};\n'
            f'- iter: Макс число итераций (Imax): "до" = {iter_get_before}; "после" = {iter_get_after};\n'
            f'- tip: Тип утяжеления (Тип): "до" = {tip_get_before}; "после" = {tip_get_after};\n'
            f'- f_ots: Формировать описания контр. величин (ФормКВ): "до" = {f_ots_get_before}; "после" = {f_ots_get_after};\n'
            f'- add_d: Добавлять значения контр. величин после шага (ДобКЗ): "до" = {add_d_get_before}; "после" = {add_d_get_after};\n'
            f'- ekstr: Поиск экстремума по контролируемым величинам (Экстремум): "до" = {ekstr_get_before}; "после" = {ekstr_get_after};\n'
            f'- kfc: Текущий шаг (Шаг): "до" = {kfc_get_before}; "после" = {kfc_get_after};\n'
            f'- sum_kfc: Сумарный шаг (Шаг_Сумм): "до" = {sum_kfc_get_before}; "после" = {sum_kfc_get_after};\n'
            f'- ds: Деление шага (ДелШаг): "до" = {ds_get_before}; "после" = {ds_get_after};\n'
            f'- it: Текущая итерация (Итер): "до" = {it_get_before}; "после" = {it_get_after};\n'
            f'- Status: Состояние утяжеления (Статус): "до" = {status_get_before}; "после" = {status_get_after};\n'
            f'- KorrT: коррекция по температуре: температура, Гр. (KorrT): "до" = {korr_t_get_before}; "после" = {korr_t_get_after};\n'
            f'- KorrPer: коррекция по температуре: перегрузка % (KorrPer): "до" = {korr_per_get_before}; "после" = {korr_per_get_after};\n'
            f'- KorrVib: коррекция по температуре: выборка (KorrVib): "до" = {korr_vib_get_before}; "после" = {korr_vib_get_after};\n'
            f'- enable_contr: Включить контроль всех ограничений U,P,I (Включить контр. U,P,I): "до" = {enable_contr_get_before}; "после" = {enable_contr_get_after};\n'
            f'- dis_v_contr: Отключить контроль всех ограничений по напряжению U (Откл контр. U): "до" = {dis_v_contr_get_before}; "после" = {dis_v_contr_get_after};\n'
            f'- dis_p_contr: Отключить контроль всех ограничений по мощности P (Откл контр. P): "до" = {dis_p_contr_get_before}; "после" = {dis_p_contr_get_after};\n'
            f'- dis_i_contr: Отключить контроль всех ограничений по току I (Откл контр. I): "до" = {dis_i_contr_get_before}; "после" = {dis_i_contr_get_after};\n'
            f'- ss_calc: Как расчитывать УР при утяжелении (Расчет УР): "до" = {ss_calc_get_before}; "после" = {ss_calc_get_after};\n'
            f'- criterion: Критерий устойчивости (Критерий): "до" = {criterion_get_before}; "после" = {criterion_get_after};\n'
            f'- no_crit_d_ba: Динамика:не учет критерия разворота угла по ЛЭП (Нет критерия: угол по ЛЭП): "до" = {no_crit_d_ba_get_before}; "после" = {no_crit_d_ba_get_after};\n'
            f'- no_crit_d_coa: Динамика:не учет критерия угла генератора и COA (Нет критерия: угол по Генератору): "до" = {no_crit_d_coa_get_before}; "после" = {no_crit_d_coa_get_after};\n'
            f'- no_crit_d_ga: Динамика:не учет критерия срабатывания автомата безопасности генератора (Нет критерия: автомат безопасности ген.): "до" = {no_crit_d_ga_get_before}; "после" = {no_crit_d_ga_get_after};\n'
            f'- save_files_filter: Критерий сохранения файлов (Критерий): "до" = {save_files_filter_get_before}; "после" = {save_files_filter_get_after};\n'
            f'- save_files_path: Папка для сохранения файлов результатов (Путь): "до" = {save_files_path_get_before}; "после" = {save_files_path_get_after};\n'
            f'- stop_u_n: Остановить при переходе к устойчивому/неустойчивому (Остановить): "до" = {stop_u_n_get_before}; "после" = {stop_u_n_get_after};\n'
            f'- dyn_find_pred: Динамика: поиск предела (Динамика: поиск предела): "до" = {dyn_find_pred_get_before}; "после" = {dyn_find_pred_get_after};\n'
        )
        print(Tools.separator_noun)
