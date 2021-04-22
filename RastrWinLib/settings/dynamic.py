# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.log_tools.tools import separator_noun
from RastrWinLib.tables.tables_attributes import com_dynamics_table, com_dynamics_attributes, \
    com_dynamics_attributes_list
from RastrWinLib.variables.variable_parametrs import Variable
from RastrWinLib.getting.get import GettingParameter


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
        MaxResultFiles='',
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
        switch_command_line=False,
):
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
                                  switch_command_line=switch_command_line)
    get_param_ = GettingParameter()

    get_t_ras = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[0],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[0],
                                        row_id=0,
                                        value=float(t_ras))

    get_h_int = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[1],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[1],
                                        row_id=0,
                                        value=float(h_int))

    get_h_min = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[2],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[2],
                                        row_id=0,
                                        value=float(h_min))

    get_h_max = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[3],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[3],
                                        row_id=0,
                                        value=float(h_max))

    get_h_out = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[4],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[4],
                                        row_id=0,
                                        value=float(h_out))

    get_mint = get_param_.get_cell(table=com_dynamics_table,
                                   column=com_dynamics_attributes_list[5],
                                   row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[5],
                                        row_id=0,
                                        value=int(mint))

    get_smint = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[6],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[6],
                                        row_id=0,
                                        value=int(smint))

    get_int_epsilon = get_param_.get_cell(table=com_dynamics_table,
                                          column=com_dynamics_attributes_list[7],
                                          row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[7],
                                        row_id=0,
                                        value=float(int_epsilon))

    get_inform_on_step_change = get_param_.get_cell(table=com_dynamics_table,
                                                    column=com_dynamics_attributes_list[8],
                                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[8],
                                        row_id=0,
                                        value=float(inform_on_step_change))

    get_tf = get_param_.get_cell(table=com_dynamics_table,
                                 column=com_dynamics_attributes_list[9],
                                 row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[9],
                                        row_id=0,
                                        value=float(tf))

    get_def = get_param_.get_cell(table=com_dynamics_table,
                                  column=com_dynamics_attributes_list[10],
                                  row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[10],
                                        row_id=0,
                                        value=float(dEf))

    get_npf = get_param_.get_cell(table=com_dynamics_table,
                                  column=com_dynamics_attributes_list[11],
                                  row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[11],
                                        row_id=0,
                                        value=float(npf))

    get_valid = get_param_.get_cell(table=com_dynamics_table,
                                    column=com_dynamics_attributes_list[12],
                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[12],
                                        row_id=0,
                                        value=float(valid))

    get_dempfrec = get_param_.get_cell(table=com_dynamics_table,
                                       column=com_dynamics_attributes_list[13],
                                       row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[13],
                                        row_id=0,
                                        value=float(dempfrec))

    get_corr_t = get_param_.get_cell(table=com_dynamics_table,
                                     column=com_dynamics_attributes_list[14],
                                     row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[14],
                                        row_id=0,
                                        value=float(corrT))

    get_is_demp = get_param_.get_cell(table=com_dynamics_table,
                                      column=com_dynamics_attributes_list[15],
                                      row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[15],
                                        row_id=0,
                                        value=float(is_demp))

    get_frsxntoy = get_param_.get_cell(table=com_dynamics_table,
                                       column=com_dynamics_attributes_list[16],
                                       row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[16],
                                        row_id=0,
                                        value=float(frSXNtoY))

    get_sxntolerance = get_param_.get_cell(table=com_dynamics_table,
                                           column=com_dynamics_attributes_list[17],
                                           row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[17],
                                        row_id=0,
                                        value=float(SXNTolerance))

    get_snap_path = get_param_.get_cell(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[18],
                                        row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[18],
                                        row_id=0,
                                        value=str(SnapPath))

    get_max_result_files = get_param_.get_cell(table=com_dynamics_table,
                                               column=com_dynamics_attributes_list[19],
                                               row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[19],
                                        row_id=0,
                                        value=float(MaxResultFiles))

    get_snap_template = get_param_.get_cell(table=com_dynamics_table,
                                            column=com_dynamics_attributes_list[20],
                                            row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[20],
                                        row_id=0,
                                        value=str(SnapTemplate))

    get_snap_auto_load = get_param_.get_cell(table=com_dynamics_table,
                                             column=com_dynamics_attributes_list[21],
                                             row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[21],
                                        row_id=0,
                                        value=float(SnapAutoLoad))

    get_snap_max_count = get_param_.get_cell(table=com_dynamics_table,
                                             column=com_dynamics_attributes_list[22],
                                             row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[22],
                                        row_id=0,
                                        value=float(SnapMaxCount))

    get_trip_generator_on_speed = get_param_.get_cell(table=com_dynamics_table,
                                                      column=com_dynamics_attributes_list[23],
                                                      row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[23],
                                        row_id=0,
                                        value=float(TripGeneratorOnSpeed))

    get_pickup_dropout = get_param_.get_cell(table=com_dynamics_table,
                                             column=com_dynamics_attributes_list[24],
                                             row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[24],
                                        row_id=0,
                                        value=float(PickupDropout))

    get_realtime_csv = get_param_.get_cell(table=com_dynamics_table,
                                           column=com_dynamics_attributes_list[25],
                                           row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[25],
                                        row_id=0,
                                        value=float(RealtimeCSV))

    get_period_angle = get_param_.get_cell(table=com_dynamics_table,
                                           column=com_dynamics_attributes_list[26],
                                           row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[26],
                                        row_id=0,
                                        value=float(PeriodAngle))

    get_result_flow_direction = get_param_.get_cell(table=com_dynamics_table,
                                                    column=com_dynamics_attributes_list[27],
                                                    row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[27],
                                        row_id=0,
                                        value=float(ResultFlowDirection))

    get_treat_warnings_as_errors = get_param_.get_cell(table=com_dynamics_table,
                                                       column=com_dynamics_attributes_list[28],
                                                       row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[28],
                                        row_id=0,
                                        value=float(TreatWarningsAsErrors))

    get_event_process = get_param_.get_cell(table=com_dynamics_table,
                                            column=com_dynamics_attributes_list[29],
                                            row_id=0)
    variable_def_rowid.make_changes_row(table=com_dynamics_table,
                                        column=com_dynamics_attributes_list[29],
                                        row_id=0,
                                        value=float(EventProcess))

    if switch_command_line is not False:
        print(separator_noun)
        print(
            f' Параметры настройки "Общие данные для расчета динамики" (таблица "Динамика": com_dynamics):\n'
            f'- t_ras: Время расчета: Tras до = {get_t_ras}; Tras "после" = {};\n'
            f'- h_int: Начальный шаг интегрирования: H_инт до = {get_h_int}; H_инт "после" = {};\n'
            f'- h_min: Минимальный шаг интегрирования: H_мин до = {get_h_min}; H_мин "после" = {};\n'
            f'- h_max: Максимальный шаг интегрирования: H_макс до = {get_h_max}; H_макс "после" = {};\n'
            f'- h_out: Шаг печати: H_печ до = {get_h_out}; H_печ "после" = {};\n'
            f'- mint: Основной метод интегрирования: Осн.Метод до = {get_mint}; Осн.Метод "после" = {};\n'
            f'- smint: Стартовый метод интегрирования: Старт.Метод до = {get_smint}; Старт.Метод "после" = {};\n'
            f'- int_epsilon: Точность шага интегрирования: dInt до = {get_int_epsilon}; dInt "после" = {};\n'
            f'- inform_on_step_change: Информировать об изменении шага: Выводить шаг до = {get_inform_on_step_change}; Выводить шаг "после" = {};\n'
            f'- tf: Постоянная сглаживания угловой скорости (частоты) узла: Tf до = {get_tf}; Tf "после" = {};\n'
            f'- dEf: Точность балансировки эдс при учете явнополюсности: dEf до = {get_def}; dEf "после" = {};\n'
            f'- npf: Макс число пересчетов УР на шаге при учете явнополюсности: Ит до = {get_npf}; Ит "после" = {};\n'
            f'- valid: Контроль входных параметров: Контр. до = {get_valid}; Контр. "после" = {};\n'
            f'- dempfrec: Демпфирование в уравнениях движения: Демпф до = {get_dempfrec}; Демпф "после" = {};\n'
            f'- corrT: Корректировать Т в парковских моделях: Корр Т до = {get_corr_t}; Корр Т "после" = {};\n'
            f'- is_demp: Учет демп. момента в моделях с демп контурами: Уч Демп до = {get_is_demp}; Уч Демп "после" = {};\n'
            f'- frSXNtoY: Напряжения перехода с СХН на шунт: V_минСХРН до = {get_frsxntoy}; V_минСХРН "после" = {};\n'
            f'- SXNTolerance: Допустимый небаланс СХН: SXNTol до = {get_sxntolerance}; SXNTol "после" = {};\n'
            f'- SnapPath: Выходной каталог файлов результатов: Кат. результатов до = {get_snap_path}; Кат. результатов "после" = {};\n'
            f'- MaxResultFiles: Максимальное кол-во файлов результатов: Макс. файлов до = {get_max_result_files}; Макс. файлов "после" = {};\n'
            f'- SnapTemplate: Шаблон имени выходного файла: Шаблон имени до = {get_snap_template}; Шаблон имени "после" = {};\n'
            f'- SnapAutoLoad: Автозагрузка последнего результата: Автозагрузка до = {get_snap_auto_load}; Автозагрузка "после" = {};\n'
            f'- SnapMaxCount: Максимальное кол-во слотов результатов: Макс. рез-тов до = {get_snap_max_count}; Макс. рез-тов "после" = {};\n'
            f'- TripGeneratorOnSpeed: Отключать генератор при превышении скорости %: Уставка автоматов безопасности до = {get_trip_generator_on_speed}; Уставка автоматов безопасности "после" = {};\n'
            f'- PickupDropout: Информировать о пуске/возврате автоматики: Информировать о пуске/возврате автоматики до = {get_pickup_dropout}; Информировать о пуске/возврате автоматики "после" = {};\n'
            f'- RealtimeCSV: Выводить контролируемые величины в CSV: Выводить контролируемые величины в CSV "до" = {get_realtime_csv}; Выводить контролируемые величины в CSV "после" = {};\n'
            f'- PeriodAngle: Отображать углы в диапазоне +/-180: Отображать углы в диапазоне +/-180 "до" = {get_period_angle}; Отображать углы в диапазоне +/-180 "после" = {};\n'
            f'- ResultFlowDirection: Положительное направление результатов: Положительное направление результатов "до" = {get_result_flow_direction}; Положительное направление результатов "после" = {};\n'
            f'- TreatWarningsAsErrors: Считать предупреждения ошибками: Предупреждение=Ошибка "до" = {get_treat_warnings_as_errors}; Предупреждение=Ошибка "после" = {};\n'
            f'- EventProcess: Метод обработки дискретных изменений: Дискретные изменения "до" = {get_event_process}; Дискретные изменения "после" = {};\n'
        )
        print(separator_noun)
    return True


class SetDynamic(VariableDefRowId):
    """
    Класс выставляет параметров настройки "Общие данные для расчета динамики"
    """

    def __init__(self, rastr_win=RASTR, table=com_dynamics_table, switch_command_line=False):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in com_dynamics_attributes.keys():
            self.list_key.append(key)
        self.switch_command_line = switch_command_line
        self.variable_def_rowid = VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table,
                                                            switch_command_line=switch_command_line)

    def set(self,
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
            MaxResultFiles='',
            SnapTemplate='<count>.sna',
            SnapAutoLoad=1,
            SnapMaxCount=6,
            TripGeneratorOnSpeed='',
            PickupDropout=0,
            RealtimeCSV=0,
            PeriodAngle=0,
            ResultFlowDirection=0,
            TreatWarningsAsErrors=0,
            EventProcess=0):
        """
        Параметры настройки "Общие данные для расчета динамики" (таблица "Динамика": com_dynamics):

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
        """
        self.variable_def_rowid.make_changes(column=self.list_key[0], row_id=0, value=float(t_ras))
        self.variable_def_rowid.make_changes(column=self.list_key[1], row_id=0, value=float(h_int))
        self.variable_def_rowid.make_changes(column=self.list_key[2], row_id=0, value=float(h_min))
        self.variable_def_rowid.make_changes(column=self.list_key[3], row_id=0, value=float(h_max))
        self.variable_def_rowid.make_changes(column=self.list_key[4], row_id=0, value=float(h_out))
        self.variable_def_rowid.make_changes(column=self.list_key[5], row_id=0, value=int(mint))
        self.variable_def_rowid.make_changes(column=self.list_key[6], row_id=0, value=int(smint))
        self.variable_def_rowid.make_changes(column=self.list_key[7], row_id=0, value=float(int_epsilon))
        self.variable_def_rowid.make_changes(column=self.list_key[8], row_id=0, value=float(inform_on_step_change))
        self.variable_def_rowid.make_changes(column=self.list_key[9], row_id=0, value=float(tf))
        self.variable_def_rowid.make_changes(column=self.list_key[10], row_id=0, value=float(dEf))
        self.variable_def_rowid.make_changes(column=self.list_key[11], row_id=0, value=float(npf))
        self.variable_def_rowid.make_changes(column=self.list_key[12], row_id=0, value=float(valid))
        self.variable_def_rowid.make_changes(column=self.list_key[13], row_id=0, value=float(dempfrec))
        self.variable_def_rowid.make_changes(column=self.list_key[14], row_id=0, value=float(corrT))
        self.variable_def_rowid.make_changes(column=self.list_key[15], row_id=0, value=float(is_demp))
        self.variable_def_rowid.make_changes(column=self.list_key[16], row_id=0, value=float(frSXNtoY))
        self.variable_def_rowid.make_changes(column=self.list_key[17], row_id=0, value=float(SXNTolerance))
        self.variable_def_rowid.make_changes(column=self.list_key[18], row_id=0, value=str(SnapPath))
        self.variable_def_rowid.make_changes(column=self.list_key[19], row_id=0, value=float(MaxResultFiles))
        self.variable_def_rowid.make_changes(column=self.list_key[20], row_id=0, value=str(SnapTemplate))
        self.variable_def_rowid.make_changes(column=self.list_key[21], row_id=0, value=float(SnapAutoLoad))
        self.variable_def_rowid.make_changes(column=self.list_key[22], row_id=0, value=float(SnapMaxCount))
        self.variable_def_rowid.make_changes(column=self.list_key[23], row_id=0, value=float(TripGeneratorOnSpeed))
        self.variable_def_rowid.make_changes(column=self.list_key[24], row_id=0, value=float(PickupDropout))
        self.variable_def_rowid.make_changes(column=self.list_key[25], row_id=0, value=float(RealtimeCSV))
        self.variable_def_rowid.make_changes(column=self.list_key[26], row_id=0, value=float(PeriodAngle))
        self.variable_def_rowid.make_changes(column=self.list_key[27], row_id=0, value=float(ResultFlowDirection))
        self.variable_def_rowid.make_changes(column=self.list_key[28], row_id=0, value=float(TreatWarningsAsErrors))
        self.variable_def_rowid.make_changes(column=self.list_key[29], row_id=0, value=float(EventProcess))

        if self.switch_command_line is not False:
            print(separator_noun)
            print(
                f' Параметры настройки "Общие данные для расчета динамики" (таблица "Динамика": com_dynamics):\n'
                '- t_ras: Время расчета: Tras до = {}; Tras "после" ={};\n'
                '- h_int: Начальный шаг интегрирования: H_инт до = {}; H_инт "после" = {};\n'
                '- h_min: Минимальный шаг интегрирования: H_мин до = {}; H_мин "после" = {};\n'
                '- h_max: Максимальный шаг интегрирования: H_макс до = {}; H_макс "после" = {};\n'
                '- h_out: Шаг печати: H_печ до = {}; H_печ "после" = {};\n'
                '- mint: Основной метод интегрирования: Осн.Метод до = {}; Осн.Метод "после" = {};\n'
                '- smint: Стартовый метод интегрирования: Старт.Метод до = {}; Старт.Метод "после" = {};\n'
                '- int_epsilon: Точность шага интегрирования: dInt до = {}; dInt "после" = {};\n'
                '- inform_on_step_change: Информировать об изменении шага: Выводить шаг до = {}; Выводить шаг "после" = {};\n'
                '- tf: Постоянная сглаживания угловой скорости (частоты) узла: Tf до = {}; Tf "после" = {};\n'
                '- dEf: Точность балансировки эдс при учете явнополюсности: dEf до = {}; dEf "после" = {};\n'
                '- npf: Макс число пересчетов УР на шаге при учете явнополюсности: Ит до = {}; Ит "после" = {};\n'
                '- valid: Контроль входных параметров: Контр. до = {}; Контр. "после" = {};\n'
                '- dempfrec: Демпфирование в уравнениях движения: Демпф до = {}; Демпф "после" = {};\n'
                '- corrT: Корректировать Т в парковских моделях: Корр Т до = {}; Корр Т "после" = {};\n'
                '- is_demp: Учет демп. момента в моделях с демп контурами: Уч Демп до = {}; Уч Демп "после" = {};\n'
                '- frSXNtoY: Напряжения перехода с СХН на шунт: V_минСХРН до = {}; V_минСХРН "после" = {};\n'
                '- SXNTolerance: Допустимый небаланс СХН: SXNTol до = {}; SXNTol "после" = {};\n'
                '- SnapPath: Выходной каталог файлов результатов: Кат. результатов до = {}; Кат. результатов "после" = {};\n'
                '- MaxResultFiles: Максимальное кол-во файлов результатов: Макс. файлов до = {}; Макс. файлов "после" = {};\n'
                '- SnapTemplate: Шаблон имени выходного файла: Шаблон имени до = {}; Шаблон имени "после" = {};\n'
                '- SnapAutoLoad: Автозагрузка последнего результата: Автозагрузка до = {}; Автозагрузка "после" = {};\n'
                '- SnapMaxCount: Максимальное кол-во слотов результатов: Макс. рез-тов до = {}; Макс. рез-тов "после" = {};\n'
                '- TripGeneratorOnSpeed: Отключать генератор при превышении скорости %: Уставка автоматов безопасности до = {}; Уставка автоматов безопасности "после" = {};\n'
                '- PickupDropout: Информировать о пуске/возврате автоматики: Информировать о пуске/возврате автоматики до = {}; Информировать о пуске/возврате автоматики "после" = {};\n'
                '- RealtimeCSV: Выводить контролируемые величины в CSV: Выводить контролируемые величины в CSV "до" = {}; Выводить контролируемые величины в CSV "после" = {};\n'
                '- PeriodAngle: Отображать углы в диапазоне +/-180: Отображать углы в диапазоне +/-180 "до" = {}; Отображать углы в диапазоне +/-180 "после" = {};\n'
                '- ResultFlowDirection: Положительное направление результатов: Положительное направление результатов "до" = {}; Положительное направление результатов "после" = {};\n'
                '- TreatWarningsAsErrors: Считать предупреждения ошибками: Предупреждение=Ошибка "до" = {}; Предупреждение=Ошибка "после" = {};\n'
                '- EventProcess: Метод обработки дискретных изменений: Дискретные изменения "до" = {}; Дискретные изменения "после" = {};\n'
            )
            print(separator_noun)
        return True


if __name__ == '__main__':
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.AstraRastr import RASTR

    load_file()

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
        MaxResultFiles='',
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
        switch_command_line=False)
