# -*- coding: utf-8 -*-
from RastrWinLib.Tables.Settings.com_dynamics import ComDynamics
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.operation.Get import GettingParameter
from RastrWinLib.operation.Variable import Variable

from prettytable import PrettyTable


def set_dynamic(
        t_ras: float = 10.0,
        h_int: float = 0.01,
        h_min: float = 0.01,
        h_max: float = 0.01,
        h_out: float = 0.01,
        mint: str = 'HH5',
        smint: str = 'КМ4',
        int_epsilon: float = 0.0001,
        inform_on_step_change: bool = False,
        tf: float = 0.02,
        dEf: float = 0.001,
        npf=10,
        valid: str = 'По умолчанию',
        dempfrec='S',
        corrT: str = 'Да',
        is_demp: str = 'Нет',
        frSXNtoY: float = 0.3,
        SXNTolerance=0,
        SnapPath: str = 'c:\\tmp\\',
        MaxResultFiles=0,
        SnapTemplate: str = '<count>.sna',
        SnapAutoLoad=True,
        SnapMaxCount: int = 6,
        TripGeneratorOnSpeed=0,
        PickupDropout=False,
        RealtimeCSV=False,
        PeriodAngle='Нет',
        ResultFlowDirection: str = 'RastrWin',
        TreatWarningsAsErrors='Нет',
        EventProcess: str = 'Стандартный',
        rastr_win=RASTR,
        switch_command_line=False):
    f"""
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
    :param switch_command_line: True/False - вывод сообщений в протокол;
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

    if switch_command_line:
        pt = PrettyTable()
        pt.title = f'Параметры настройки "Общие данные для расчета динамики" (таблица: {ComDynamics.table})'
        pt.field_names = ['Название параметра', '"ДО"', '"ПОСЛЕ"']
        pt.add_row(['Время расчета: Tras', get_t_ras, get_t_ras_after])
        pt.add_row(['Начальный шаг интегрирования: H_инт', get_h_int, get_h_int_after])
        pt.add_row(['Минимальный шаг интегрирования: H_мин', get_h_min, get_h_min_after])
        pt.add_row(['Максимальный шаг интегрирования: H_макс', get_h_max, get_h_max_after])
        pt.add_row(['Шаг печати: H_печ', get_h_out, get_h_out_after])
        pt.add_row(['Основной метод интегрирования: Осн.Метод', get_mint, get_mint_after])
        pt.add_row(['Стартовый метод интегрирования: Старт.Метод', get_smint, get_smint_after])
        pt.add_row(['Точность шага интегрирования: dInt', get_int_epsilon, get_int_epsilon_after])
        pt.add_row(['Информировать об изменении шага: Выводить шаг', get_inform_on_step_change,
                    get_inform_on_step_change_after])
        pt.add_row(['Постоянная сглаживания угловой скорости (частоты) узла: Tf', get_tf, get_tf_after])
        pt.add_row(['Точность балансировки эдс при учете явнополюсности: dEf', get_def, get_def_after])
        pt.add_row(['Макс число пересчетов УР на шаге при учете явнополюсности: Ит', get_npf, get_npf_after])
        pt.add_row(['Контроль входных параметров: Контр.', get_valid, get_valid_after])
        pt.add_row(['Демпфирование в уравнениях движения: Демпф', get_dempfrec, get_dempfrec_after])
        pt.add_row(['Корректировать Т в парковских моделях: Корр Т', get_corr_t, get_corr_t_after])
        pt.add_row(['Учет демп. момента в моделях с демп контурами: Уч Демп', get_is_demp, get_is_demp_after])
        pt.add_row(['Напряжения перехода с СХН на шунт: V_минСХРН', get_frsxntoy, get_frsxntoy_after])
        pt.add_row(['Допустимый небаланс СХН: SXNTol', get_sxntolerance, get_sxntolerance_after])
        pt.add_row(['Выходной каталог файлов результатов: Кат. результатов', get_snap_path, get_snap_path_after])
        pt.add_row(
            ['Максимальное кол-во файлов результатов: Макс. файлов', get_max_result_files, get_max_result_files_after])
        pt.add_row(['Шаблон имени выходного файла: Шаблон имени', get_snap_template, get_snap_template_after])
        pt.add_row(['Автозагрузка последнего результата: Автозагрузка', get_snap_auto_load, get_snap_auto_load_after])
        pt.add_row(
            ['Максимальное кол-во слотов результатов: Макс. рез-тов', get_snap_max_count, get_snap_max_count_after])
        pt.add_row(['Отключать генератор при превышении скорости %: Уставка автоматов безопасности',
                    get_trip_generator_on_speed,
                    get_trip_generator_on_speed_after])
        pt.add_row(['Информировать о пуске/возврате автоматики: Информировать о пуске/возврате автоматики',
                    get_pickup_dropout, get_pickup_dropout_after])
        pt.add_row(['Выводить контролируемые величины в CSV: Выводить контролируемые величины в CSV',
                    get_realtime_csv, get_realtime_csv_after])
        pt.add_row(['Отображать углы в диапазоне +/-180: Отображать углы в диапазоне +/-180',
                    get_period_angle, get_period_angle_after])
        pt.add_row(['Положительное направление результатов: Положительное направление результатов',
                    get_result_flow_direction, get_result_flow_direction_after])
        pt.add_row(['Считать предупреждения ошибками: Предупреждение=Ошибка',
                    get_treat_warnings_as_errors, get_treat_warnings_as_errors_after])
        pt.add_row(['Метод обработки дискретных изменений: Дискретные изменения',
                    get_event_process, get_event_process_after])
        print(pt)


class GetSettingsDynamic(GettingParameter):

    def __init__(self, rastr_win=RASTR):
        """
        Параметры настройки "Общие данные для расчета динамики" (таблица: com_dynamics)
        :param rastr_win: COM - объект Rastr.Astra (win32com).
        """
        self.rastr_win = rastr_win
        super().__init__(rastr_win)

    def Tras(self) -> float:
        """
        Метод возвращает установленное значение: Время расчета: (Tras);
        :return: t_ras -> float
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.Tras,
                                 row_id=0)

    def Hint(self) -> float:
        """
        Начальный шаг интегрирования (H_инт)
        :return: Hint -> float
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.Hint,
                                 row_id=0)

    def Hmin(self) -> float:
        """
        Минимальный шаг интегрирования (H_мин)
        :return: Hmin -> float
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.Hmin,
                                 row_id=0)

    def Hmax(self) -> float:
        """
        Максимальный шаг интегрирования (H_макс)
        :return: Hmax -> float
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.Hmax,
                                 row_id=0)

    def Hout(self) -> float:
        """
        Шаг печати (H_печ)
        :return: Hout -> float
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.Hout,
                                 row_id=0)

    def Mint(self) -> int:
        """
        Основной метод интегрирования (Осн.Метод)
        :return: Mint -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.Mint,
                                 row_id=0)

    def SMint(self) -> int:
        """
        Стартовый метод интегрирования (Старт.Метод)
        :return: SMint -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.SMint,
                                 row_id=0)

    def IntEpsilon(self) -> float:
        """
        Точность шага интегрирования (dInt)
        :return: IntEpsilon -> float
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.IntEpsilon,
                                 row_id=0)

    def InformOnStepChange(self) -> bool:
        """
        Информировать об изменении шага (Выводить шаг)
        :return: InformOnStepChange -> bool
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.InformOnStepChange,
                                 row_id=0)

    def Tf(self) -> float:
        """
        Постоянная сглаживания угловой скорости (частоты) узла (Tf)
        :return: Tf -> float
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.Tf,
                                 row_id=0)

    def dEf(self) -> float:
        """
        Точность балансировки эдс при учете явнополюсности (dEf)
        :return: dEf -> float
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.dEf,
                                 row_id=0)

    def Npf(self) -> int:
        """
        Макс число пересчетов УР на шаге при учете явнополюсности (Ит)
        :return: Npf -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.Npf,
                                 row_id=0)

    def Valid(self) -> int:
        """
        Контроль входных параметров (Контр.)
        :return: Valid -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.Valid,
                                 row_id=0)

    def dempfrec(self) -> int:
        """
        Демпфирование в уравнениях движения (Демпф)
        :return: dempfrec -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.dempfrec,
                                 row_id=0)

    def corrT(self) -> int:
        """
        Корректировать Т в парковских моделях (Корр Т)
        :return: corrT -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.corrT,
                                 row_id=0)

    def IsDemp(self) -> int:
        """
        Учет демп. момента в моделях с демп контурами (Уч Демп)
        :return: IsDemp -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.IsDemp,
                                 row_id=0)

    def frSXNtoY(self) -> float:
        """
        Напряжения перехода с СХН на шунт (V_минСХРН)
        :return: frSXNtoY -> float
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.frSXNtoY,
                                 row_id=0)

    def SXNTolerance(self) -> float:
        """
        Допустимый небаланс СХН (SXNTol)
        :return: SXNTolerance -> float
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.SXNTolerance,
                                 row_id=0)

    def SnapPath(self) -> str:
        """
        Выходной каталог файлов результатов (Кат. результатов)
        :return: SnapPath -> str
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.SnapPath,
                                 row_id=0)

    def MaxResultFiles(self) -> int:
        """
        Максимальное кол-во файлов результатов (Макс. файлов)
        :return: MaxResultFiles -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.MaxResultFiles,
                                 row_id=0)

    def SnapTemplate(self) -> str:
        """
        Шаблон имени выходного файла (Шаблон имени)
        :return: SnapTemplate -> str
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.SnapTemplate,
                                 row_id=0)

    def SnapAutoLoad(self) -> bool:
        """
        Автозагрузка последнего результата (Автозагрузка)
        :return: SnapAutoLoad -> bool
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.SnapAutoLoad,
                                 row_id=0)

    def SnapMaxCount(self) -> int:
        """
        Метод возвращает установленное максимальное кол-во слотов результатов: (Макс. рез-тов);
        :return: snap_max_count -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.SnapMaxCount,
                                 row_id=0)

    def TripGeneratorOnSpeed(self) -> float:
        """
        Отключать генератор при превышении скорости % (Уставка автоматов безопасности)
        :return: TripGeneratorOnSpeed -> float
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.TripGeneratorOnSpeed,
                                 row_id=0)

    def PickupDropout(self) -> bool:
        """
        Информировать о пуске/возврате автоматики (Информировать о пуске/возврате автоматики)
        :return: PickupDropout -> bool
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.PickupDropout,
                                 row_id=0)

    def RealtimeCSV(self) -> bool:
        """
        Выводить контролируемые величины в CSV (Выводить контролируемые величины в CSV)
        :return: RealtimeCSV -> bool
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.RealtimeCSV,
                                 row_id=0)

    def PeriodAngle(self) -> int:
        """
        Отображать углы в диапазоне +/-180 (Отображать углы в диапазоне +/-180)
        :return:
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.PeriodAngle,
                                 row_id=0)

    def ResultFlowDirection(self) -> int:
        """
        Положительное направление результатов (Положительное направление результатов)
        :return: ResultFlowDirection -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.ResultFlowDirection,
                                 row_id=0)

    def TreatWarningsAsErrors(self) -> int:
        """
        Считать предупреждения ошибками (Предупреждение=Ошибка)
        :return: TreatWarningsAsErrors -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.TreatWarningsAsErrors,
                                 row_id=0)

    def EventProcess(self) -> int:
        """
        Метод обработки дискретных изменений (Дискретные изменения)
        :return: EventProcess -> int
        """
        return self.get_cell_row(table=ComDynamics.table,
                                 column=ComDynamics.EventProcess,
                                 row_id=0)

    def table(self) -> str:
        """
        Возвращает название таблицы: 'com_dynamics'
        :return: ComDynamics.table -> str
        """
        return ComDynamics.table

    def table_name(self) -> str:
        """
        Возвращает название таблицы: "Общие данные для расчета динамики"
        :return: ComDynamics.table_name -> str
        """
        return ComDynamics.table_name


class VariableSettingsDynamic(Variable):
    def __init__(self):
        super().__init__(rastr_win=RASTR)

    def Tras(self, value: float) -> float:
        """
        Метод возвращает установленное значение: Время расчета: (Tras);
        :return: t_ras -> float
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.Tras,
                                     row_id=0,
                                     value=value)

    def Hint(self, value: float) -> float:
        """
        Начальный шаг интегрирования (H_инт)
        :return: Hint -> float
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.Hint,
                                     row_id=0,
                                     value=value)

    def Hmin(self, value: float) -> float:
        """
        Минимальный шаг интегрирования (H_мин)
        :return: Hmin -> float
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.Hmin,
                                     row_id=0,
                                     value=value)

    def Hmax(self, value: float) -> float:
        """
        Максимальный шаг интегрирования (H_макс)
        :return: Hmax -> float
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.Hmax,
                                     row_id=0,
                                     value=value)

    def Hout(self, value: float) -> float:
        """
        Шаг печати (H_печ)
        :return: Hout -> float
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.Hout,
                                     row_id=0,
                                     value=value)

    def Mint(self, value: int) -> int:
        """
        Основной метод интегрирования (Осн.Метод)
        :return: Mint -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.Mint,
                                     row_id=0,
                                     value=value)

    def SMint(self, value: int) -> int:
        """
        Стартовый метод интегрирования (Старт.Метод)
        :return: SMint -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.SMint,
                                     row_id=0,
                                     value=value)

    def IntEpsilon(self, value: float) -> float:
        """
        Точность шага интегрирования (dInt)
        :return: IntEpsilon -> float
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.IntEpsilon,
                                     row_id=0,
                                     value=value)

    def InformOnStepChange(self, value: bool) -> bool:
        """
        Информировать об изменении шага (Выводить шаг)
        :return: InformOnStepChange -> bool
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.InformOnStepChange,
                                     row_id=0,
                                     value=value)

    def Tf(self, value: float) -> float:
        """
        Постоянная сглаживания угловой скорости (частоты) узла (Tf)
        :return: Tf -> float
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.Tf,
                                     row_id=0,
                                     value=value)

    def dEf(self, value: float) -> float:
        """
        Точность балансировки эдс при учете явнополюсности (dEf)
        :return: dEf -> float
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.dEf,
                                     row_id=0,
                                     value=value)

    def Npf(self, value: int) -> int:
        """
        Макс число пересчетов УР на шаге при учете явнополюсности (Ит)
        :return: Npf -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.Npf,
                                     row_id=0,
                                     value=value)

    def Valid(self, value: int) -> int:
        """
        Контроль входных параметров (Контр.)
        :return: Valid -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.Valid,
                                     row_id=0,
                                     value=value)

    def dempfrec(self, value: int) -> int:
        """
        Демпфирование в уравнениях движения (Демпф)
        :return: dempfrec -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.dempfrec,
                                     row_id=0,
                                     value=value)

    def corrT(self, value: int) -> int:
        """
        Корректировать Т в парковских моделях (Корр Т)
        :return: corrT -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.corrT,
                                     row_id=0,
                                     value=value)

    def IsDemp(self, value: int) -> int:
        """
        Учет демп. момента в моделях с демп контурами (Уч Демп)
        :return: IsDemp -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.IsDemp,
                                     row_id=0,
                                     value=value)

    def frSXNtoY(self, value: float) -> float:
        """
        Напряжения перехода с СХН на шунт (V_минСХРН)
        :return: frSXNtoY -> float
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.frSXNtoY,
                                     row_id=0,
                                     value=value)

    def SXNTolerance(self, value: float) -> float:
        """
        Допустимый небаланс СХН (SXNTol)
        :return: SXNTolerance -> float
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.SXNTolerance,
                                     row_id=0,
                                     value=value)

    def SnapPath(self, value: str) -> str:
        """
        Выходной каталог файлов результатов (Кат. результатов)
        :return: SnapPath -> str
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.SnapPath,
                                     row_id=0,
                                     value=value)

    def MaxResultFiles(self, value: int) -> int:
        """
        Максимальное кол-во файлов результатов (Макс. файлов)
        :return: MaxResultFiles -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.MaxResultFiles,
                                     row_id=0,
                                     value=value)

    def SnapTemplate(self, value: str) -> str:
        """
        Шаблон имени выходного файла (Шаблон имени)
        :return: SnapTemplate -> str
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.SnapTemplate,
                                     row_id=0,
                                     value=value)

    def SnapAutoLoad(self, value: bool) -> bool:
        """
        Автозагрузка последнего результата (Автозагрузка)
        :return: SnapAutoLoad -> bool
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.SnapAutoLoad,
                                     row_id=0,
                                     value=value)

    def SnapMaxCount(self, value: int) -> int:
        """
        Метод возвращает установленное максимальное кол-во слотов результатов: (Макс. рез-тов);
        :return: snap_max_count -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.SnapMaxCount,
                                     row_id=0,
                                     value=value)

    def TripGeneratorOnSpeed(self, value: float) -> float:
        """
        Отключать генератор при превышении скорости % (Уставка автоматов безопасности)
        :return: TripGeneratorOnSpeed -> float
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.TripGeneratorOnSpeed,
                                     row_id=0,
                                     value=value)

    def PickupDropout(self, value: bool) -> bool:
        """
        Информировать о пуске/возврате автоматики (Информировать о пуске/возврате автоматики)
        :return: PickupDropout -> bool
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.PickupDropout,
                                     row_id=0,
                                     value=value)

    def RealtimeCSV(self, value: bool) -> bool:
        """
        Выводить контролируемые величины в CSV (Выводить контролируемые величины в CSV)
        :return: RealtimeCSV -> bool
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.RealtimeCSV,
                                     row_id=0,
                                     value=value)

    def PeriodAngle(self, value: int) -> int:
        """
        Отображать углы в диапазоне +/-180 (Отображать углы в диапазоне +/-180)
        :return:
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.PeriodAngle,
                                     row_id=0,
                                     value=value)

    def ResultFlowDirection(self, value: int) -> int:
        """
        Положительное направление результатов (Положительное направление результатов)
        :return: ResultFlowDirection -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.ResultFlowDirection,
                                     row_id=0,
                                     value=value)

    def TreatWarningsAsErrors(self, value: int) -> int:
        """
        Считать предупреждения ошибками (Предупреждение=Ошибка)
        :return: TreatWarningsAsErrors -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.TreatWarningsAsErrors,
                                     row_id=0,
                                     value=value)

    def EventProcess(self, value: int) -> int:
        """
        Метод обработки дискретных изменений (Дискретные изменения)
        :return: EventProcess -> int
        """
        return self.make_changes_row(table=ComDynamics.table,
                                     column=ComDynamics.EventProcess,
                                     row_id=0,
                                     value=value)


if __name__ == '__main__':
    from RastrWinLib.Load import load_file
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.operation.Get import GettingParameter

    load_file(rastr_win=RASTR,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
              shabl='сценарий',
              switch_command_line=False)

    load_file(rastr_win=RASTR,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test92.rst',
              shabl='динамика',
              switch_command_line=False)

    get = GetSettingsDynamic()
    var = VariableSettingsDynamic()

    # print(get.Tras())
    # print(type(get.Tras()))
    #
    # var.Tras(200)
    #
    # print(get.Tras())
    # print(type(get.Tras()))

    set_dynamic(switch_command_line=True)