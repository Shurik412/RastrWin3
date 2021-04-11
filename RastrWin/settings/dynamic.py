# -*- coding: utf-8 -*-
from RastrWin.AstraRastr import RASTR
from RastrWin.variables.variable_parametrs import VariableDefRowId
from RastrWin.tables.tables_attributes import com_dynamics_table, com_dynamics_attributes


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
        VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table, switch_command_line=switch_command_line)

    def set(self,
            t_ras=5,
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
        VariableDefRowId.make_changes(self, column=self.list_key[0], row_id=0, value=float(t_ras))
        VariableDefRowId.make_changes(self, column=self.list_key[1], row_id=0, value=float(h_int))
        VariableDefRowId.make_changes(self, column=self.list_key[2], row_id=0, value=float(h_min))
        VariableDefRowId.make_changes(self, column=self.list_key[3], row_id=0, value=float(h_max))
        VariableDefRowId.make_changes(self, column=self.list_key[4], row_id=0, value=float(h_out))
        VariableDefRowId.make_changes(self, column=self.list_key[5], row_id=0, value=int(mint))
        VariableDefRowId.make_changes(self, column=self.list_key[6], row_id=0, value=int(smint))
        VariableDefRowId.make_changes(self, column=self.list_key[7], row_id=0, value=float(int_epsilon))
        VariableDefRowId.make_changes(self, column=self.list_key[8], row_id=0, value=float(inform_on_step_change))
        VariableDefRowId.make_changes(self, column=self.list_key[9], row_id=0, value=float(tf))
        VariableDefRowId.make_changes(self, column=self.list_key[10], row_id=0, value=float(dEf))
        VariableDefRowId.make_changes(self, column=self.list_key[11], row_id=0, value=float(npf))
        VariableDefRowId.make_changes(self, column=self.list_key[12], row_id=0, value=float(valid))
        VariableDefRowId.make_changes(self, column=self.list_key[13], row_id=0, value=float(dempfrec))
        VariableDefRowId.make_changes(self, column=self.list_key[14], row_id=0, value=float(corrT))
        VariableDefRowId.make_changes(self, column=self.list_key[15], row_id=0, value=float(is_demp))
        VariableDefRowId.make_changes(self, column=self.list_key[16], row_id=0, value=float(frSXNtoY))
        VariableDefRowId.make_changes(self, column=self.list_key[17], row_id=0, value=float(SXNTolerance))
        VariableDefRowId.make_changes(self, column=self.list_key[18], row_id=0, value=str(SnapPath))
        VariableDefRowId.make_changes(self, column=self.list_key[19], row_id=0, value=float(MaxResultFiles))
        VariableDefRowId.make_changes(self, column=self.list_key[20], row_id=0, value=str(SnapTemplate))
        VariableDefRowId.make_changes(self, column=self.list_key[21], row_id=0, value=float(SnapAutoLoad))
        VariableDefRowId.make_changes(self, column=self.list_key[22], row_id=0, value=float(SnapMaxCount))
        VariableDefRowId.make_changes(self, column=self.list_key[23], row_id=0, value=float(TripGeneratorOnSpeed))
        VariableDefRowId.make_changes(self, column=self.list_key[24], row_id=0, value=float(PickupDropout))
        VariableDefRowId.make_changes(self, column=self.list_key[25], row_id=0, value=float(RealtimeCSV))
        VariableDefRowId.make_changes(self, column=self.list_key[26], row_id=0, value=float(PeriodAngle))
        VariableDefRowId.make_changes(self, column=self.list_key[27], row_id=0, value=float(ResultFlowDirection))
        VariableDefRowId.make_changes(self, column=self.list_key[28], row_id=0, value=float(TreatWarningsAsErrors))
        VariableDefRowId.make_changes(self, column=self.list_key[29], row_id=0, value=float(EventProcess))
