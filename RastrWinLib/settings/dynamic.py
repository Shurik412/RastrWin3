# -*- coding: utf-8 -*-
from RastrWinLib.tables.Settings.com_dynamics import ComDynamics
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.log_tools.tools import separator_noun
from RastrWinLib.variables.variable_parametrs import Variable


def set_dynamic(
        t_ras: float = 10.0,
        h_int: float = 0.01,
        h_min: float = 0.01,
        h_max: float = 0.01,
        h_out: float = 0.01,
        mint='HH5',
        smint='КМ4',
        int_epsilon: float = 0.0001,
        inform_on_step_change=False,
        tf: float = 0.02,
        dEf: float = 0.001,
        npf=10,
        valid='По умолчанию',
        dempfrec='S',
        corrT='Да',
        is_demp='Нет',
        frSXNtoY: float = 0.3,
        SXNTolerance=0,
        SnapPath: str = 'c:\\tmp\\',
        MaxResultFiles=0,
        SnapTemplate: str = '<count>.sna',
        SnapAutoLoad=True,
        SnapMaxCount=6,
        TripGeneratorOnSpeed=0,
        PickupDropout=False,
        RealtimeCSV=False,
        PeriodAngle='Нет',
        ResultFlowDirection: str = 'RastrWin',
        TreatWarningsAsErrors='Нет',
        EventProcess: str = 'Стандартный',
        rastr_win=RASTR,
        switch_command_line=False):
    """
    Параметры настройки "Общие данные для расчета динамики" (таблица: com_dynamics):

    :param t_ras: Время расчета: (Tras);
    :param h_int: Начальный шаг интегрирования: (H_инт);
    :param h_min: Минимальный шаг интегрирования: (H_мин);
    :param h_max: Максимальный шаг интегрирования: (H_макс);
    :param h_out: Шаг печати: (H_печ);
    :param mint: Основной метод интегрирования: (Осн.Метод);
    :param smint: Стартовый метод интегрирования: (Старт.Метод);
    :param int_epsilon: Точность шага интегрирования: (dInt);
    :param inform_on_step_change: Информировать об изменении шага: (Выводить шаг);
    :param tf: Постоянная сглаживания угловой скорости (частоты) узла: (Tf);
    :param dEf: Точность балансировки эдс при учете явнополюсности: (dEf);
    :param npf: Макс число пересчетов УР на шаге при учете явнополюсности: (Ит);
    :param valid: Контроль входных параметров: (Контр.);
    :param dempfrec: Демпфирование в уравнениях движения: (Демпф);
    :param corrT: Корректировать Т в парковских моделях: (Корр Т);
    :param is_demp: Учет демп. момента в моделях с демп контурами: (Уч Демп);
    :param frSXNtoY: Напряжения перехода с СХН на шунт: (V_минСХРН);
    :param SXNTolerance: Допустимый небаланс СХН: (SXNTol);
    :param SnapPath: Выходной каталог файлов результатов: (Кат. результатов);
    :param MaxResultFiles: Максимальное кол-во файлов результатов: (Макс. файлов);
    :param SnapTemplate: Шаблон имени выходного файла: (Шаблон имени);
    :param SnapAutoLoad: Автозагрузка последнего результата: (Автозагрузка);
    :param SnapMaxCount: Максимальное кол-во слотов результатов: (Макс. рез-тов);
    :param TripGeneratorOnSpeed: Отключать генератор при превышении скорости %: (Уставка автоматов безопасности);
    :param PickupDropout: Информировать о пуске/возврате автоматики: (Информировать о пуске/возврате автоматики);
    :param RealtimeCSV: Выводить контролируемые величины в CSV: (Выводить контролируемые величины в CSV);
    :param PeriodAngle: Отображать углы в диапазоне +/-180: (Отображать углы в диапазоне +/-180);
    :param ResultFlowDirection: Положительное направление результатов: (Положительное направление результатов);
    :param TreatWarningsAsErrors: Считать предупреждения ошибками: (Предупреждение=Ошибка);
    :param EventProcess: Метод обработки дискретных изменений: (Дискретные изменения);
    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param switch_command_line: True/False - вывод сообщений в протакол;
    :return Nothing returns
    """
    variable_def_rowid = Variable(rastr_win=rastr_win)
    get_param_ = GettingParameter(rastr_win=rastr_win)

    # Время расчета (Tras)
    get_t_ras = get_param_.get_cell_row(table=ComDynamics.table,
                                        column=ComDynamics.Tras,
                                        row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.Tras,
                                        row_id=0,
                                        value=t_ras)
    get_t_ras_after = get_param_.get_cell_row(table=ComDynamics.table,
                                              column=ComDynamics.Tras,
                                              row_id=0)

    # Начальный шаг интегрирования (H_инт)
    get_h_int = get_param_.get_cell_row(table=ComDynamics.table,
                                        column=ComDynamics.Hint,
                                        row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.Hint,
                                        row_id=0,
                                        value=h_int)
    get_h_int_after = get_param_.get_cell_row(table=ComDynamics.table,
                                              column=ComDynamics.Hint,
                                              row_id=0)

    # Минимальный шаг интегрирования (H_мин)
    get_h_min = get_param_.get_cell_row(table=ComDynamics.table,
                                        column=ComDynamics.Hmin,
                                        row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.Hmin,
                                        row_id=0,
                                        value=h_min)
    get_h_min_after = get_param_.get_cell_row(table=ComDynamics.table,
                                              column=ComDynamics.Hmin,
                                              row_id=0)

    # Максимальный шаг интегрирования (H_макс)
    get_h_max = get_param_.get_cell_row(table=ComDynamics.table,
                                        column=ComDynamics.Hmax,
                                        row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.Hmax,
                                        row_id=0,
                                        value=h_max)
    get_h_max_after = get_param_.get_cell_row(table=ComDynamics.table,
                                              column=ComDynamics.Hmax,
                                              row_id=0)

    # Шаг печати (H_печ)
    get_h_out = get_param_.get_cell_row(table=ComDynamics.table,
                                        column=ComDynamics.Hout,
                                        row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.Hout,
                                        row_id=0,
                                        value=h_out)
    get_h_out_after = get_param_.get_cell_row(table=ComDynamics.table,
                                              column=ComDynamics.Hout,
                                              row_id=0)

    # Основной метод интегрирования (Осн.Метод)
    get_mint = get_param_.get_cell_row(table=ComDynamics.table,
                                       column=ComDynamics.Mint,
                                       row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.Mint,
                                        row_id=0,
                                        value=mint)
    get_mint_after = get_param_.get_cell_row(table=ComDynamics.table,
                                             column=ComDynamics.Mint,
                                             row_id=0)

    # Стартовый метод интегрирования (Старт.Метод)
    get_smint = get_param_.get_cell_row(table=ComDynamics.table,
                                        column=ComDynamics.SMint,
                                        row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.SMint,
                                        row_id=0,
                                        value=smint)
    get_smint_after = get_param_.get_cell_row(table=ComDynamics.table,
                                              column=ComDynamics.SMint,
                                              row_id=0)

    # Точность шага интегрирования (dInt)
    get_int_epsilon = get_param_.get_cell_row(table=ComDynamics.table,
                                              column=ComDynamics.IntEpsilon,
                                              row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.IntEpsilon,
                                        row_id=0,
                                        value=int_epsilon)
    get_int_epsilon_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                    column=ComDynamics.IntEpsilon,
                                                    row_id=0)

    # Информировать об изменении шага (Выводить шаг)
    get_inform_on_step_change = get_param_.get_cell_row(table=ComDynamics.table,
                                                        column=ComDynamics.InformOnStepChange,
                                                        row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.InformOnStepChange,
                                        row_id=0,
                                        value=inform_on_step_change)
    get_inform_on_step_change_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                              column=ComDynamics.InformOnStepChange,
                                                              row_id=0)

    # Постоянная сглаживания угловой скорости (частоты) узла (Tf)
    get_tf = get_param_.get_cell_row(table=ComDynamics.table,
                                     column=ComDynamics.Tf,
                                     row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.Tf,
                                        row_id=0,
                                        value=tf)
    get_tf_after = get_param_.get_cell_row(table=ComDynamics.table,
                                           column=ComDynamics.Tf,
                                           row_id=0)

    # Точность балансировки эдс при учете явнополюсности (dEf)
    get_def = get_param_.get_cell_row(table=ComDynamics.table,
                                      column=ComDynamics.dEf,
                                      row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.dEf,
                                        row_id=0,
                                        value=dEf)
    get_def_after = get_param_.get_cell_row(table=ComDynamics.table,
                                            column=ComDynamics.dEf,
                                            row_id=0)

    # Макс число пересчетов УР на шаге при учете явнополюсности (Ит)
    get_npf = get_param_.get_cell_row(table=ComDynamics.table,
                                      column=ComDynamics.Npf,
                                      row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.Npf,
                                        row_id=0,
                                        value=npf)
    get_npf_after = get_param_.get_cell_row(table=ComDynamics.table,
                                            column=ComDynamics.Npf,
                                            row_id=0)

    # Контроль входных параметров (Контр.)
    get_valid = get_param_.get_cell_row(table=ComDynamics.table,
                                        column=ComDynamics.Valid,
                                        row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.Valid,
                                        row_id=0,
                                        value=valid)
    get_valid_after = get_param_.get_cell_row(table=ComDynamics.table,
                                              column=ComDynamics.Valid,
                                              row_id=0)

    # Демпфирование в уравнениях движения (Демпф)
    get_dempfrec = get_param_.get_cell_row(table=ComDynamics.table,
                                           column=ComDynamics.dempfrec,
                                           row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.dempfrec,
                                        row_id=0,
                                        value=dempfrec)
    get_dempfrec_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                 column=ComDynamics.dempfrec,
                                                 row_id=0)

    # Корректировать Т в парковских моделях (Корр Т)
    get_corr_t = get_param_.get_cell_row(table=ComDynamics.table,
                                         column=ComDynamics.corrT,
                                         row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.corrT,
                                        row_id=0,
                                        value=corrT)
    get_corr_t_after = get_param_.get_cell_row(table=ComDynamics.table,
                                               column=ComDynamics.corrT,
                                               row_id=0)

    # Учет демп. момента в моделях с демп контурами (Уч Демп)
    get_is_demp = get_param_.get_cell_row(table=ComDynamics.table,
                                          column=ComDynamics.IsDemp,
                                          row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.IsDemp,
                                        row_id=0,
                                        value=is_demp)
    get_is_demp_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                column=ComDynamics.IsDemp,
                                                row_id=0)

    # Напряжения перехода с СХН на шунт (V_минСХРН)
    get_frsxntoy = get_param_.get_cell_row(table=ComDynamics.table,
                                           column=ComDynamics.frSXNtoY,
                                           row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.frSXNtoY,
                                        row_id=0,
                                        value=frSXNtoY)
    get_frsxntoy_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                 column=ComDynamics.frSXNtoY,
                                                 row_id=0)

    # Допустимый небаланс СХН (SXNTol)
    get_sxntolerance = get_param_.get_cell_row(table=ComDynamics.table,
                                               column=ComDynamics.frSXNtoY,
                                               row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.frSXNtoY,
                                        row_id=0,
                                        value=SXNTolerance)
    get_sxntolerance_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                     column=ComDynamics.frSXNtoY,
                                                     row_id=0)

    # Выходной каталог файлов результатов (Кат. результатов)
    get_snap_path = get_param_.get_cell_row(table=ComDynamics.table,
                                            column=ComDynamics.SnapPath,
                                            row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.SnapPath,
                                        row_id=0,
                                        value=SnapPath)
    get_snap_path_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                  column=ComDynamics.SnapPath,
                                                  row_id=0)

    # Максимальное кол-во файлов результатов (Макс. файлов)
    get_max_result_files = get_param_.get_cell_row(table=ComDynamics.table,
                                                   column=ComDynamics.MaxResultFiles,
                                                   row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.MaxResultFiles,
                                        row_id=0,
                                        value=MaxResultFiles)
    get_max_result_files_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                         column=ComDynamics.MaxResultFiles,
                                                         row_id=0)

    # Шаблон имени выходного файла (Шаблон имени)
    get_snap_template = get_param_.get_cell_row(table=ComDynamics.table,
                                                column=ComDynamics.SnapTemplate,
                                                row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.SnapTemplate,
                                        row_id=0,
                                        value=SnapTemplate)
    get_snap_template_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                      column=ComDynamics.SnapTemplate,
                                                      row_id=0)

    # Автозагрузка последнего результата (Автозагрузка)
    get_snap_auto_load = get_param_.get_cell_row(table=ComDynamics.table,
                                                 column=ComDynamics.SnapAutoLoad,
                                                 row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.SnapAutoLoad,
                                        row_id=0,
                                        value=SnapAutoLoad)
    get_snap_auto_load_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                       column=ComDynamics.SnapAutoLoad,
                                                       row_id=0)

    # Максимальное кол-во слотов результатов (Макс. рез-тов)
    get_snap_max_count = get_param_.get_cell_row(table=ComDynamics.table,
                                                 column=ComDynamics.SnapMaxCount,
                                                 row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.SnapMaxCount,
                                        row_id=0,
                                        value=SnapMaxCount)
    get_snap_max_count_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                       column=ComDynamics.SnapMaxCount,
                                                       row_id=0)

    # Отключать генератор при превышении скорости % (Уставка автоматов безопасности)
    get_trip_generator_on_speed = get_param_.get_cell_row(table=ComDynamics.table,
                                                          column=ComDynamics.TripGeneratorOnSpeed,
                                                          row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.TripGeneratorOnSpeed,
                                        row_id=0,
                                        value=TripGeneratorOnSpeed)
    get_trip_generator_on_speed_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                                column=ComDynamics.TripGeneratorOnSpeed,
                                                                row_id=0)

    # Информировать о пуске/возврате автоматики (Информировать о пуске/возврате автоматики)
    get_pickup_dropout = get_param_.get_cell_row(table=ComDynamics.table,
                                                 column=ComDynamics.PickupDropout,
                                                 row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.PickupDropout,
                                        row_id=0,
                                        value=PickupDropout)
    get_pickup_dropout_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                       column=ComDynamics.PickupDropout,
                                                       row_id=0)

    # Выводить контролируемые величины в CSV (Выводить контролируемые величины в CSV)
    get_realtime_csv = get_param_.get_cell_row(table=ComDynamics.table,
                                               column=ComDynamics.RealtimeCSV,
                                               row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.RealtimeCSV,
                                        row_id=0,
                                        value=RealtimeCSV)
    get_realtime_csv_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                     column=ComDynamics.RealtimeCSV,
                                                     row_id=0)

    # Отображать углы в диапазоне +/-180 (Отображать углы в диапазоне +/-180)
    get_period_angle = get_param_.get_cell_row(table=ComDynamics.table,
                                               column=ComDynamics.PeriodAngle,
                                               row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.PeriodAngle,
                                        row_id=0,
                                        value=PeriodAngle)
    get_period_angle_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                     column=ComDynamics.PeriodAngle,
                                                     row_id=0)

    # Положительное направление результатов (Положительное направление результатов)
    get_result_flow_direction = get_param_.get_cell_row(table=ComDynamics.table,
                                                        column=ComDynamics.ResultFlowDirection,
                                                        row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.ResultFlowDirection,
                                        row_id=0,
                                        value=ResultFlowDirection)
    get_result_flow_direction_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                              column=ComDynamics.ResultFlowDirection,
                                                              row_id=0)

    # Считать предупреждения ошибками (Предупреждение=Ошибка)
    get_treat_warnings_as_errors = get_param_.get_cell_row(table=ComDynamics.table,
                                                           column=ComDynamics.TreatWarningsAsErrors,
                                                           row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.TreatWarningsAsErrors,
                                        row_id=0,
                                        value=TreatWarningsAsErrors)
    get_treat_warnings_as_errors_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                                 column=ComDynamics.TreatWarningsAsErrors,
                                                                 row_id=0)

    # Метод обработки дискретных изменений (Дискретные изменения)
    get_event_process = get_param_.get_cell_row(table=ComDynamics.table,
                                                column=ComDynamics.EventProcess,
                                                row_id=0)
    variable_def_rowid.make_changes_row(table=ComDynamics.table,
                                        column=ComDynamics.EventProcess,
                                        row_id=0,
                                        value=EventProcess)
    get_event_process_after = get_param_.get_cell_row(table=ComDynamics.table,
                                                      column=ComDynamics.EventProcess,
                                                      row_id=0)

    if switch_command_line is not False:
        print(
            f'{separator_noun}\n'
            f' Параметры настройки "Общие данные для расчета динамики" (таблица: {ComDynamics.table}):\n\n'
            f'- t_ras: Время расчета: Tras "до" = {get_t_ras}; "после" = {get_t_ras_after};\n'
            f'- h_int: Начальный шаг интегрирования: H_инт "до" = {get_h_int}; "после" = {get_h_int_after};\n'
            f'- h_min: Минимальный шаг интегрирования: H_мин "до" = {get_h_min}; "после" = {get_h_min_after};\n'
            f'- h_max: Максимальный шаг интегрирования: H_макс "до" = {get_h_max}; "после" = {get_h_max_after};\n'
            f'- h_out: Шаг печати: H_печ до = {get_h_out}; "после" = {get_h_out_after};\n'
            f'- mint: Основной метод интегрирования: Осн.Метод "до" = {get_mint}; "после" = {get_mint_after};\n'
            f'- smint: Стартовый метод интегрирования: Старт.Метод "до" = {get_smint}; "после" = {get_smint_after};\n'
            f'- int_epsilon: Точность шага интегрирования: dInt "до" = {get_int_epsilon}; "после" = {get_int_epsilon_after};\n'
            f'- inform_on_step_change: Информировать об изменении шага: Выводить шаг "до" = {get_inform_on_step_change}; "после" = {get_inform_on_step_change_after};\n'
            f'- tf: Постоянная сглаживания угловой скорости (частоты) узла: Tf "до" = {get_tf}; "после" = {get_tf_after};\n'
            f'- dEf: Точность балансировки эдс при учете явнополюсности: dEf "до" = {get_def}; "после" = {get_def_after};\n'
            f'- npf: Макс число пересчетов УР на шаге при учете явнополюсности: Ит "до" = {get_npf}; "после" = {get_npf_after};\n'
            f'- valid: Контроль входных параметров: Контр. "до" = {get_valid}; "после" = {get_valid_after};\n'
            f'- dempfrec: Демпфирование в уравнениях движения: Демпф "до" = {get_dempfrec}; "после" = {get_dempfrec_after};\n'
            f'- corrT: Корректировать Т в парковских моделях: Корр Т "до" = {get_corr_t}; "после" = {get_corr_t_after};\n'
            f'- is_demp: Учет демп. момента в моделях с демп контурами: Уч Демп "до" = {get_is_demp}; "после" = {get_is_demp_after};\n'
            f'- frSXNtoY: Напряжения перехода с СХН на шунт: V_минСХРН "до" = {get_frsxntoy}; "после" = {get_frsxntoy_after};\n'
            f'- SXNTolerance: Допустимый небаланс СХН: SXNTol "до" = {get_sxntolerance}; "после" = {get_sxntolerance_after};\n'
            f'- SnapPath: Выходной каталог файлов результатов: Кат. результатов "до" = {get_snap_path}; "после" = {get_snap_path_after};\n'
            f'- MaxResultFiles: Максимальное кол-во файлов результатов: Макс. файлов "до" = {get_max_result_files}; "после" = {get_max_result_files_after};\n'
            f'- SnapTemplate: Шаблон имени выходного файла: Шаблон имени "до" = {get_snap_template}; "после" = {get_snap_template_after};\n'
            f'- SnapAutoLoad: Автозагрузка последнего результата: Автозагрузка "до" = {get_snap_auto_load}; "после" = {get_snap_auto_load_after};\n'
            f'- SnapMaxCount: Максимальное кол-во слотов результатов: Макс. рез-тов "до" = {get_snap_max_count}; "после" = {get_snap_max_count_after};\n'
            f'- TripGeneratorOnSpeed: Отключать генератор при превышении скорости %: Уставка автоматов безопасности "до" = {get_trip_generator_on_speed}; "после" = {get_trip_generator_on_speed_after};\n'
            f'- PickupDropout: Информировать о пуске/возврате автоматики: Информировать о пуске/возврате автоматики "до" = {get_pickup_dropout}; "после" = {get_pickup_dropout_after};\n'
            f'- RealtimeCSV: Выводить контролируемые величины в CSV: Выводить контролируемые величины в CSV "до" = {get_realtime_csv}; "после" = {get_realtime_csv_after};\n'
            f'- PeriodAngle: Отображать углы в диапазоне +/-180: Отображать углы в диапазоне +/-180 "до" = {get_period_angle}; "после" = {get_period_angle_after};\n'
            f'- ResultFlowDirection: Положительное направление результатов: Положительное направление результатов "до" = {get_result_flow_direction}; "после" = {get_result_flow_direction_after};\n'
            f'- TreatWarningsAsErrors: Считать предупреждения ошибками: Предупреждение=Ошибка "до" = {get_treat_warnings_as_errors}; "после" = {get_treat_warnings_as_errors_after};\n'
            f'- EventProcess: Метод обработки дискретных изменений: Дискретные изменения "до" = {get_event_process}; "после" = {get_event_process_after};\n'
            f'{separator_noun}\n'
        )
    return (
        f'{separator_noun}\n'
        f' Параметры настройки "Общие данные для расчета динамики" (таблица: {ComDynamics.table}):\n'
        f'- t_ras: Время расчета: Tras "до" = {get_t_ras}; "после" = {get_t_ras_after};\n'
        f'- h_int: Начальный шаг интегрирования: H_инт "до" = {get_h_int}; "после" = {get_h_int_after};\n'
        f'- h_min: Минимальный шаг интегрирования: H_мин "до" = {get_h_min}; "после" = {get_h_min_after};\n'
        f'- h_max: Максимальный шаг интегрирования: H_макс "до" = {get_h_max}; "после" = {get_h_max_after};\n'
        f'- h_out: Шаг печати: H_печ до = {get_h_out}; "после" = {get_h_out_after};\n'
        f'- mint: Основной метод интегрирования: Осн.Метод "до" = {get_mint}; "после" = {get_mint_after};\n'
        f'- smint: Стартовый метод интегрирования: Старт.Метод "до" = {get_smint}; "после" = {get_smint_after};\n'
        f'- int_epsilon: Точность шага интегрирования: dInt "до" = {get_int_epsilon}; "после" = {get_int_epsilon_after};\n'
        f'- inform_on_step_change: Информировать об изменении шага: Выводить шаг "до" = {get_inform_on_step_change}; "после" = {get_inform_on_step_change_after};\n'
        f'- tf: Постоянная сглаживания угловой скорости (частоты) узла: Tf "до" = {get_tf}; "после" = {get_tf_after};\n'
        f'- dEf: Точность балансировки эдс при учете явнополюсности: dEf "до" = {get_def}; "после" = {get_def_after};\n'
        f'- npf: Макс число пересчетов УР на шаге при учете явнополюсности: Ит "до" = {get_npf}; "после" = {get_npf_after};\n'
        f'- valid: Контроль входных параметров: Контр. "до" = {get_valid}; "после" = {get_valid_after};\n'
        f'- dempfrec: Демпфирование в уравнениях движения: Демпф "до" = {get_dempfrec}; "после" = {get_dempfrec_after};\n'
        f'- corrT: Корректировать Т в парковских моделях: Корр Т "до" = {get_corr_t}; "после" = {get_corr_t_after};\n'
        f'- is_demp: Учет демп. момента в моделях с демп контурами: Уч Демп "до" = {get_is_demp}; "после" = {get_is_demp_after};\n'
        f'- frSXNtoY: Напряжения перехода с СХН на шунт: V_минСХРН "до" = {get_frsxntoy}; "после" = {get_frsxntoy_after};\n'
        f'- SXNTolerance: Допустимый небаланс СХН: SXNTol "до" = {get_sxntolerance}; "после" = {get_sxntolerance_after};\n'
        f'- SnapPath: Выходной каталог файлов результатов: Кат. результатов "до" = {get_snap_path}; "после" = {get_snap_path_after};\n'
        f'- MaxResultFiles: Максимальное кол-во файлов результатов: Макс. файлов "до" = {get_max_result_files}; "после" = {get_max_result_files_after};\n'
        f'- SnapTemplate: Шаблон имени выходного файла: Шаблон имени "до" = {get_snap_template}; "после" = {get_snap_template_after};\n'
        f'- SnapAutoLoad: Автозагрузка последнего результата: Автозагрузка "до" = {get_snap_auto_load}; "после" = {get_snap_auto_load_after};\n'
        f'- SnapMaxCount: Максимальное кол-во слотов результатов: Макс. рез-тов "до" = {get_snap_max_count}; "после" = {get_snap_max_count_after};\n'
        f'- TripGeneratorOnSpeed: Отключать генератор при превышении скорости %: Уставка автоматов безопасности "до" = {get_trip_generator_on_speed}; "после" = {get_trip_generator_on_speed_after};\n'
        f'- PickupDropout: Информировать о пуске/возврате автоматики: Информировать о пуске/возврате автоматики "до" = {get_pickup_dropout}; "после" = {get_pickup_dropout_after};\n'
        f'- RealtimeCSV: Выводить контролируемые величины в CSV: Выводить контролируемые величины в CSV "до" = {get_realtime_csv}; "после" = {get_realtime_csv_after};\n'
        f'- PeriodAngle: Отображать углы в диапазоне +/-180: Отображать углы в диапазоне +/-180 "до" = {get_period_angle}; "после" = {get_period_angle_after};\n'
        f'- ResultFlowDirection: Положительное направление результатов: Положительное направление результатов "до" = {get_result_flow_direction}; "после" = {get_result_flow_direction_after};\n'
        f'- TreatWarningsAsErrors: Считать предупреждения ошибками: Предупреждение=Ошибка "до" = {get_treat_warnings_as_errors}; "после" = {get_treat_warnings_as_errors_after};\n'
        f'- EventProcess: Метод обработки дискретных изменений: Дискретные изменения "до" = {get_event_process}; "после" = {get_event_process_after};\n'
        f'{separator_noun}\n'
    )
