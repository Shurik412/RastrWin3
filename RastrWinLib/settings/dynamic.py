# -*- coding: utf-8 -*-
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.log_tools.tools import separator_noun
from RastrWinLib.tables.tables_attributes import com_dynamics_table, com_dynamics_attributes_list
from RastrWinLib.variables.variable_parametrs import Variable


def set_dynamic(
        t_ras=5.0,
        h_int=0.01,
        h_min=0.01,
        h_max=0.01,
        h_out=0.01,
        mint=0,
        smint=0,
        int_epsilon=0.0001,
        inform_on_step_change=0,
        tf=0.02,
        dEf=0.001,
        npf=10,
        valid=0,
        dempfrec=0,
        corrT=0,
        is_demp=0,
        frSXNtoY=0.3,
        SXNTolerance='',
        SnapPath='c:\\tmp\\',
        MaxResultFiles=0,
        SnapTemplate='<count>.sna',
        SnapAutoLoad=1,
        SnapMaxCount=6,
        TripGeneratorOnSpeed=0,
        PickupDropout=0,
        RealtimeCSV=0,
        PeriodAngle=0,
        ResultFlowDirection=0,
        TreatWarningsAsErrors=0,
        EventProcess=0,
        switch_command_line=False):
    """
    Параметры настройки "Общие данные для расчета динамики" (таблица "Динамика": com_dynamics):

    :param switch_command_line:
    :param t_ras: Время расчета (Tras)
    :param h_int: Начальный шаг интегрирования (H_инт)
    :param h_min: Минимальный шаг интегрирования (H_мин)
    :param h_max: Максимальный шаг интегрирования (H_макс)
    :param h_out: Шаг печати (H_печ)
    :param mint: Основной метод интегрирования (Осн.Метод)
    :param smint: Стартовый метод интегрирования (Старт.Метод)
    :param int_epsilon: Точность шага интегрирования (dInt)
    :param inform_on_step_change: Информировать об изменении шага (Выводить шаг)
    :param tf: Постоянная сглаживания угловой скорости (частоты) узла (Tf)
    :param dEf: Точность балансировки эдс при учете явнополюсности (dEf)
    :param npf: Макс число пересчетов УР на шаге при учете явнополюсности (Ит)
    :param valid: Контроль входных параметров (Контр.)
    :param dempfrec: Демпфирование в уравнениях движения (Демпф)
    :param corrT: Корректировать Т в парковских моделях (Корр Т)
    :param is_demp: Учет демп. момента в моделях с демп контурами (Уч Демп)
    :param frSXNtoY: Напряжения перехода с СХН на шунт (V_минСХРН)
    :param SXNTolerance: Допустимый небаланс СХН (SXNTol)
    :param SnapPath: Выходной каталог файлов результатов (Кат. результатов)
    :param MaxResultFiles: Максимальное кол-во файлов результатов (Макс. файлов)
    :param SnapTemplate: Шаблон имени выходного файла (Шаблон имени)
    :param SnapAutoLoad: Автозагрузка последнего результата (Автозагрузка)
    :param SnapMaxCount: Максимальное кол-во слотов результатов (Макс. рез-тов)
    :param TripGeneratorOnSpeed: Отключать генератор при превышении скорости % (Уставка автоматов безопасности)
    :param PickupDropout: Информировать о пуске/возврате автоматики (Информировать о пуске/возврате автоматики)
    :param RealtimeCSV: Выводить контролируемые величины в CSV (Выводить контролируемые величины в CSV)
    :param PeriodAngle: Отображать углы в диапазоне +/-180 (Отображать углы в диапазоне +/-180)
    :param ResultFlowDirection: Положительное направление результатов (Положительное направление результатов)
    :param TreatWarningsAsErrors: Считать предупреждения ошибками (Предупреждение=Ошибка)
    :param EventProcess: Метод обработки дискретных изменений (Дискретные изменения)
    :return True
    """
    variable_def_rowid = Variable(rastr_win=RASTR,
                                  switch_command_line=False)
    get_param_ = GettingParameter()

    get_t_ras = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[0],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[0],
                                        row_id=0,
                                        value=float(t_ras))
    get_t_ras_after = get_param_.get_cell(table=com_dynamics_table,
                                          column=com_dynamics_attributes_list[0],
                                          row_id=0)

    get_h_int = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[1],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[1],
                                        row_id=0,
                                        value=float(h_int))
    get_h_int_after = get_param_.get_cell(table=com_dynamics_table,
                                          column=com_dynamics_attributes_list[1],
                                          row_id=0)

    get_h_min = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[2],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[2],
                                        row_id=0,
                                        value=float(h_min))
    get_h_min_after = get_param_.get_cell(table=com_dynamics_table,
                                          column=com_dynamics_attributes_list[2],
                                          row_id=0)

    get_h_max = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[3],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[3],
                                        row_id=0,
                                        value=float(h_max))
    get_h_max_after = get_param_.get_cell(table=com_dynamics_table,
                                          column=com_dynamics_attributes_list[3],
                                          row_id=0)

    get_h_out = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[4],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[4],
                                        row_id=0,
                                        value=float(h_out))
    get_h_out_after = get_param_.get_cell(table=com_dynamics_table,
                                          column=com_dynamics_attributes_list[4],
                                          row_id=0)

    get_mint = get_param_.get_cell(table=com_dynamics_table,
                                   column=com_dynamics_attributes_list[5],
                                   row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[5],
                                        row_id=0,
                                        value=int(mint))
    get_mint_after = get_param_.get_cell(table=com_dynamics_table,
                                         column=com_dynamics_attributes_list[5],
                                         row_id=0)

    get_smint = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[6],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[6],
                                        row_id=0,
                                        value=int(smint))
    get_smint_after = get_param_.get_cell(table=com_dynamics_table,
                                          column=com_dynamics_attributes_list[6],
                                          row_id=0)

    get_int_epsilon = get_param_.get_cell(table=com_dynamics_table,
                                          column=com_dynamics_attributes_list[7],
                                          row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[7],
                                        row_id=0,
                                        value=float(int_epsilon))
    get_int_epsilon_after = get_param_.get_cell(table=com_dynamics_table,
                                                column=com_dynamics_attributes_list[7],
                                                row_id=0)

    get_inform_on_step_change = get_param_.get_cell(table=com_dynamics_table,
                                                    column=com_dynamics_attributes_list[8],
                                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[8],
                                        row_id=0,
                                        value=float(inform_on_step_change))
    get_inform_on_step_change_after = get_param_.get_cell(table=com_dynamics_table,
                                                          column=com_dynamics_attributes_list[8],
                                                          row_id=0)

    get_tf = get_param_.get_cell(table=com_dynamics_table,
                                 column=com_dynamics_attributes_list[9],
                                 row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[9],
                                        row_id=0,
                                        value=float(tf))
    get_tf_after = get_param_.get_cell(table=com_dynamics_table,
                                       column=com_dynamics_attributes_list[9],
                                       row_id=0)

    get_def = get_param_.get_cell(table=com_dynamics_table,
                                  column=com_dynamics_attributes_list[10],
                                  row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[10],
                                        row_id=0,
                                        value=float(dEf))
    get_def_after = get_param_.get_cell(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[10],
                                        row_id=0)

    get_npf = get_param_.get_cell(table=com_dynamics_table,
                                  column=com_dynamics_attributes_list[11],
                                  row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[11],
                                        row_id=0,
                                        value=float(npf))
    get_npf_after = get_param_.get_cell(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[11],
                                        row_id=0)

    get_valid = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[12],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[12],
                                        row_id=0,
                                        value=float(valid))
    get_valid_after = get_param_.get_cell(table=com_dynamics_table,
                                          column=com_dynamics_attributes_list[12],
                                          row_id=0)

    get_dempfrec = get_param_.get_cell(table=com_dynamics_table,
                                       column=com_dynamics_attributes_list[13],
                                       row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[13],
                                        row_id=0,
                                        value=float(dempfrec))
    get_dempfrec_after = get_param_.get_cell(table=com_dynamics_table,
                                             column=com_dynamics_attributes_list[13],
                                             row_id=0)

    get_corr_t = get_param_.get_cell(table=com_dynamics_table,
                                     column=com_dynamics_attributes_list[14],
                                     row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[14],
                                        row_id=0,
                                        value=float(corrT))
    get_corr_t_after = get_param_.get_cell(table=com_dynamics_table,
                                           column=com_dynamics_attributes_list[14],
                                           row_id=0)

    get_is_demp = get_param_.get_cell(table=com_dynamics_table,
                                      column=com_dynamics_attributes_list[15],
                                      row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[15],
                                        row_id=0,
                                        value=float(is_demp))
    get_is_demp_after = get_param_.get_cell(table=com_dynamics_table,
                                            column=com_dynamics_attributes_list[15],
                                            row_id=0)

    get_frsxntoy = get_param_.get_cell(table=com_dynamics_table,
                                       column=com_dynamics_attributes_list[16],
                                       row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[16],
                                        row_id=0,
                                        value=float(frSXNtoY))
    get_frsxntoy_after = get_param_.get_cell(table=com_dynamics_table,
                                             column=com_dynamics_attributes_list[16],
                                             row_id=0)

    get_sxntolerance = get_param_.get_cell(table=com_dynamics_table,
                                           column=com_dynamics_attributes_list[17],
                                           row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[17],
                                        row_id=0,
                                        value=SXNTolerance)
    get_sxntolerance_after = get_param_.get_cell(table=com_dynamics_table,
                                                 column=com_dynamics_attributes_list[17],
                                                 row_id=0)

    get_snap_path = get_param_.get_cell(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[18],
                                        row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[18],
                                        row_id=0,
                                        value=str(SnapPath))
    get_snap_path_after = get_param_.get_cell(table=com_dynamics_table,
                                              column=com_dynamics_attributes_list[18],
                                              row_id=0)

    get_max_result_files = get_param_.get_cell(table=com_dynamics_table,
                                               column=com_dynamics_attributes_list[19],
                                               row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[19],
                                        row_id=0,
                                        value=MaxResultFiles)
    get_max_result_files_after = get_param_.get_cell(table=com_dynamics_table,
                                                     column=com_dynamics_attributes_list[19],
                                                     row_id=0)

    get_snap_template = get_param_.get_cell(table=com_dynamics_table,
                                            column=com_dynamics_attributes_list[20],
                                            row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[20],
                                        row_id=0,
                                        value=str(SnapTemplate))
    get_snap_template_after = get_param_.get_cell(table=com_dynamics_table,
                                                  column=com_dynamics_attributes_list[20],
                                                  row_id=0)

    get_snap_auto_load = get_param_.get_cell(table=com_dynamics_table,
                                             column=com_dynamics_attributes_list[21],
                                             row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[21],
                                        row_id=0,
                                        value=float(SnapAutoLoad))
    get_snap_auto_load_after = get_param_.get_cell(table=com_dynamics_table,
                                                   column=com_dynamics_attributes_list[21],
                                                   row_id=0)

    get_snap_max_count = get_param_.get_cell(table=com_dynamics_table,
                                             column=com_dynamics_attributes_list[22],
                                             row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[22],
                                        row_id=0,
                                        value=float(SnapMaxCount))
    get_snap_max_count_after = get_param_.get_cell(table=com_dynamics_table,
                                                   column=com_dynamics_attributes_list[22],
                                                   row_id=0)

    get_trip_generator_on_speed = get_param_.get_cell(table=com_dynamics_table,
                                                      column=com_dynamics_attributes_list[23],
                                                      row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[23],
                                        row_id=0,
                                        value=TripGeneratorOnSpeed)
    get_trip_generator_on_speed_after = get_param_.get_cell(table=com_dynamics_table,
                                                            column=com_dynamics_attributes_list[23],
                                                            row_id=0)

    get_pickup_dropout = get_param_.get_cell(table=com_dynamics_table,
                                             column=com_dynamics_attributes_list[24],
                                             row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[24],
                                        row_id=0,
                                        value=PickupDropout)
    get_pickup_dropout_after = get_param_.get_cell(table=com_dynamics_table,
                                                   column=com_dynamics_attributes_list[24],
                                                   row_id=0)

    get_realtime_csv = get_param_.get_cell(table=com_dynamics_table,
                                           column=com_dynamics_attributes_list[25],
                                           row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[25],
                                        row_id=0,
                                        value=RealtimeCSV)
    get_realtime_csv_after = get_param_.get_cell(table=com_dynamics_table,
                                                 column=com_dynamics_attributes_list[25],
                                                 row_id=0)

    get_period_angle = get_param_.get_cell(table=com_dynamics_table,
                                           column=com_dynamics_attributes_list[26],
                                           row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[26],
                                        row_id=0,
                                        value=float(PeriodAngle))
    get_period_angle_after = get_param_.get_cell(table=com_dynamics_table,
                                                 column=com_dynamics_attributes_list[26],
                                                 row_id=0)

    get_result_flow_direction = get_param_.get_cell(table=com_dynamics_table,
                                                    column=com_dynamics_attributes_list[27],
                                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[27],
                                        row_id=0,
                                        value=float(ResultFlowDirection))
    get_result_flow_direction_after = get_param_.get_cell(table=com_dynamics_table,
                                                          column=com_dynamics_attributes_list[27],
                                                          row_id=0)

    get_treat_warnings_as_errors = get_param_.get_cell(table=com_dynamics_table,
                                                       column=com_dynamics_attributes_list[28],
                                                       row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[28],
                                        row_id=0,
                                        value=float(TreatWarningsAsErrors))
    get_treat_warnings_as_errors_after = get_param_.get_cell(table=com_dynamics_table,
                                                             column=com_dynamics_attributes_list[28],
                                                             row_id=0)

    get_event_process = get_param_.get_cell(table=com_dynamics_table,
                                            column=com_dynamics_attributes_list[29],
                                            row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[29],
                                        row_id=0,
                                        value=float(EventProcess))
    get_event_process_after = get_param_.get_cell(table=com_dynamics_table,
                                                  column=com_dynamics_attributes_list[29],
                                                  row_id=0)

    if switch_command_line is not False:
        print(separator_noun)
        print(
            f' Параметры настройки "Общие данные для расчета динамики" (таблица "Динамика": com_dynamics):\n'
            f'- t_ras: Время расчета: Tras до = {get_t_ras}; Tras "после" = {get_t_ras_after};\n'
            f'- h_int: Начальный шаг интегрирования: H_инт "до" = {get_h_int}; H_инт "после" = {get_h_int_after};\n'
            f'- h_min: Минимальный шаг интегрирования: H_мин "до" = {get_h_min}; H_мин "после" = {get_h_min_after};\n'
            f'- h_max: Максимальный шаг интегрирования: H_макс "до" = {get_h_max}; H_макс "после" = {get_h_max_after};\n'
            f'- h_out: Шаг печати: H_печ до = {get_h_out}; H_печ "после" = {get_h_out_after};\n'
            f'- mint: Основной метод интегрирования: Осн.Метод "до" = {get_mint}; Осн.Метод "после" = {get_mint_after};\n'
            f'- smint: Стартовый метод интегрирования: Старт.Метод "до" = {get_smint}; Старт.Метод "после" = {get_smint_after};\n'
            f'- int_epsilon: Точность шага интегрирования: dInt "до" = {get_int_epsilon}; dInt "после" = {get_int_epsilon_after};\n'
            f'- inform_on_step_change: Информировать об изменении шага: Выводить шаг "до" = {get_inform_on_step_change}; Выводить шаг "после" = {get_inform_on_step_change_after};\n'
            f'- tf: Постоянная сглаживания угловой скорости (частоты) узла: Tf "до" = {get_tf}; Tf "после" = {get_tf_after};\n'
            f'- dEf: Точность балансировки эдс при учете явнополюсности: dEf "до" = {get_def}; dEf "после" = {get_def_after};\n'
            f'- npf: Макс число пересчетов УР на шаге при учете явнополюсности: Ит "до" = {get_npf}; Ит "после" = {get_npf_after};\n'
            f'- valid: Контроль входных параметров: Контр. "до" = {get_valid}; Контр. "после" = {get_valid_after};\n'
            f'- dempfrec: Демпфирование в уравнениях движения: Демпф "до" = {get_dempfrec}; Демпф "после" = {get_dempfrec_after};\n'
            f'- corrT: Корректировать Т в парковских моделях: Корр Т "до" = {get_corr_t}; Корр Т "после" = {get_corr_t_after};\n'
            f'- is_demp: Учет демп. момента в моделях с демп контурами: Уч Демп "до" = {get_is_demp}; Уч Демп "после" = {get_is_demp_after};\n'
            f'- frSXNtoY: Напряжения перехода с СХН на шунт: V_минСХРН "до" = {get_frsxntoy}; V_минСХРН "после" = {get_frsxntoy_after};\n'
            f'- SXNTolerance: Допустимый небаланс СХН: SXNTol "до" = {get_sxntolerance}; SXNTol "после" = {get_sxntolerance_after};\n'
            f'- SnapPath: Выходной каталог файлов результатов: Кат. результатов "до" = {get_snap_path}; Кат. результатов "после" = {get_snap_path_after};\n'
            f'- MaxResultFiles: Максимальное кол-во файлов результатов: Макс. файлов "до" = {get_max_result_files}; Макс. файлов "после" = {get_max_result_files_after};\n'
            f'- SnapTemplate: Шаблон имени выходного файла: Шаблон имени "до" = {get_snap_template}; Шаблон имени "после" = {get_snap_template_after};\n'
            f'- SnapAutoLoad: Автозагрузка последнего результата: Автозагрузка "до" = {get_snap_auto_load}; Автозагрузка "после" = {get_snap_auto_load_after};\n'
            f'- SnapMaxCount: Максимальное кол-во слотов результатов: Макс. рез-тов "до" = {get_snap_max_count}; Макс. рез-тов "после" = {get_snap_max_count_after};\n'
            f'- TripGeneratorOnSpeed: Отключать генератор при превышении скорости %: Уставка автоматов безопасности "до" = {get_trip_generator_on_speed}; Уставка автоматов безопасности "после" = {get_trip_generator_on_speed_after};\n'
            f'- PickupDropout: Информировать о пуске/возврате автоматики: Информировать о пуске/возврате автоматики "до" = {get_pickup_dropout}; Информировать о пуске/возврате автоматики "после" = {get_pickup_dropout_after};\n'
            f'- RealtimeCSV: Выводить контролируемые величины в CSV: Выводить контролируемые величины в CSV "до" = {get_realtime_csv}; Выводить контролируемые величины в CSV "после" = {get_realtime_csv_after};\n'
            f'- PeriodAngle: Отображать углы в диапазоне +/-180: Отображать углы в диапазоне +/-180 "до" = {get_period_angle}; Отображать углы в диапазоне +/-180 "после" = {get_period_angle_after};\n'
            f'- ResultFlowDirection: Положительное направление результатов: Положительное направление результатов "до" = {get_result_flow_direction}; Положительное направление результатов "после" = {get_result_flow_direction_after};\n'
            f'- TreatWarningsAsErrors: Считать предупреждения ошибками: Предупреждение=Ошибка "до" = {get_treat_warnings_as_errors}; Предупреждение=Ошибка "после" = {get_treat_warnings_as_errors_after};\n'
            f'- EventProcess: Метод обработки дискретных изменений: Дискретные изменения "до" = {get_event_process}; Дискретные изменения "после" = {get_event_process_after};\n'
        )
        print(separator_noun)
    return True


if __name__ == '__main__':
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.loading.shablon import shablon_file_dynamic

    load_file(file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
              shablon=shablon_file_dynamic,
              switch_command_line=False)

    set_dynamic(
        t_ras=5.0,
        h_int=0.01,
        h_min=0.01,
        h_max=0.01,
        h_out=0.01,
        mint=0,
        smint=0,
        int_epsilon=0.0001,
        inform_on_step_change=0,
        tf=0.02,
        dEf=0.001,
        npf=10,
        valid=0,
        dempfrec=0,
        corrT=0,
        is_demp=0,
        frSXNtoY=0.3,
        SXNTolerance='',
        SnapPath='c:\\tmp\\',
        MaxResultFiles=1,
        SnapTemplate='<count>.sna',
        SnapAutoLoad=1,
        SnapMaxCount=6,
        TripGeneratorOnSpeed='',
        PickupDropout=0,
        RealtimeCSV=0,
        PeriodAngle=0,
        ResultFlowDirection=0,
        TreatWarningsAsErrors=0,
        EventProcess=0,
        switch_command_line=True)
