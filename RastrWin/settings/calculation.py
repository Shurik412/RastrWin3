# -*- coding: utf-8 -*-

from RastrWin.object_rastr import RASTR
from RastrWin.variables.variable_parametrs import VariableDefRowId
from RastrWin.tables.tablesAttributes import com_ekviv_table, com_ekviv_attributes, com_regim_table, \
    com_regim_attributes, com_dynamics_attributes, com_dynamics_table, alt_unit_attributes, alt_unit_table, \
    ut_common_table, ut_common_attributes


class SetEkviv(VariableDefRowId):
    """
    Класс выставляет параметров настройки "Эквивалент"
    """

    def __init__(self, rastr_win=RASTR, table=com_ekviv_table):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in com_ekviv_attributes.keys():
            self.list_key.append(key)
        VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table, switch_command_line=True)

    def set(self,
            selekv=0,
            met_ekv=0,
            tip_ekv=0,
            ekvgen=0,
            tip_gen=1,
            kfc_x='',
            pot_gen=0,
            kpn='',
            tip_sxn=0,
            smart=0,
            zmax=1000,
            otm_n=0):
        """
        Параметры настройки "Общие параметры эквивалентирования" (таблица "Эквивалент": com_ekviv):

        :param selekv: Отмеченные узлы: (Отмеч)
        :param met_ekv: Метод эквивалентирования (Мет Экв)
        :param tip_ekv: Тип эквивалентирования (Тип Экв)
        :param ekvgen: Эквивалент узлов с фикс V (фиксV)
        :param tip_gen: Тип эквивалентирования генераторов (Тип Ген)
        :param kfc_x: Коэффициент для Xg_ген (К_X_Ген)
        :param pot_gen: Учет потерь при разносе генерации: (dP_Ген)
        :param kpn: Доля нагрузки, пересчитываемая в шунт (d_наг)
        :param tip_sxn: Учитывать СХН при эквивалентировании (СХН)
        :param smart: "Умное" эквивалентирование : (Smart)
        :param zmax: Удаление ветвей с сопротивлением большим: (Z_max)
        :param otm_n: Отмечать узлы после эквивалентирования (Отм)
        """

        VariableDefRowId.make_changes(self, column=self.list_key[0], row_id=0, value=selekv)
        VariableDefRowId.make_changes(self, column=self.list_key[1], row_id=0, value=met_ekv)
        VariableDefRowId.make_changes(self, column=self.list_key[2], row_id=0, value=tip_ekv)
        VariableDefRowId.make_changes(self, column=self.list_key[3], row_id=0, value=ekvgen)
        VariableDefRowId.make_changes(self, column=self.list_key[4], row_id=0, value=tip_gen)
        VariableDefRowId.make_changes(self, column=self.list_key[5], row_id=0, value=kfc_x)
        VariableDefRowId.make_changes(self, column=self.list_key[6], row_id=0, value=pot_gen)
        VariableDefRowId.make_changes(self, column=self.list_key[7], row_id=0, value=kpn)
        VariableDefRowId.make_changes(self, column=self.list_key[8], row_id=0, value=tip_sxn)
        VariableDefRowId.make_changes(self, column=self.list_key[9], row_id=0, value=smart)
        VariableDefRowId.make_changes(self, column=self.list_key[10], row_id=0, value=zmax)
        VariableDefRowId.make_changes(self, column=self.list_key[11], row_id=0, value=otm_n)


class SetRegim(VariableDefRowId):
    """
    Класс выставляет параметров настройки "Общие параметры режима"
    """

    def __init__(self, rastr_win=RASTR, table=com_regim_table, switch_command_line=False):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in com_regim_attributes.keys():
            self.list_key.append(key)
        self.switch_command_line = switch_command_line

        VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table, switch_command_line=switch_command_line)

    def set(self,
            neb_p=1.000,
            it_max=500,
            start=0,
            flot=1,
            dv_min=0.5,
            dv_max=2.000,
            dd_max=5157,
            status=0,
            rr=0,
            wt='',
            gen_p=0,
            method=0,
            method_ogr=0,
            print_mode=0,
            qmax=0,
            min_x='',
            calc_tr=0,
            nag_p=0,
            rem_breaker=0,
            gram=0,
            ctrl_baza=0,
            itz='',
            itz_ogr_max='',
            itz_ogr_min='',
            min_nodes_in_island=''):
        """
        Параметры настройки "Общие параметры режима" (таблица "Режим": com_regim):

        :param neb_p: Точность расчета (dP)
        :param it_max: Максимальное число итераций (It)
        :param start: Стартовый алгоритм (Start)
        :param flot: Плоский старт (Пл.старт)
        :param dv_min: Мин. допустимое снижение V (dV-)
        :param dv_max: Макс. допустимое превышение V (dV+)
        :param dd_max: Макс. допустимый угол по связи (dDelta)
        :param status: Состояние расчета режима (Статус)
        :param rr: Учет частоты: (W)
        :param wt: Отклонение частоты (dF)
        :param gen_p: Пересчитывать P/Q узла по P ген (Ген->P)
        :param method: Метод Расчета (Метод)
        :param method_ogr: Метод учета ограничений Q (Метод учета ограничений Q)
        :param print_mode: Уровень печати (Печать)
        :param qmax: Точный метод расчета Qmax (Qmax)
        :param min_x: Сопротивление выключателя (ое на 10-6) (Min_X)
        :param calc_tr: Пересчет АТ/3х обм. трансформаторов (Транс.)
        :param nag_p: Пересчитывать (P/Q) нагрузки узла по ВРДО (Наг->P)
        :param rem_breaker: Удаление выключателей из схемы: (Выкл)
        :param gram: Пересчет мощности генератора по ГРАМ: (Грам)
        :param ctrl_baza: Автоматическое создание БУ (БУ)
        :param itz: Стартовый метод: число итераций (Z_it)
        :param itz_ogr_max: Стартовый метод: Учет Qmax с итерации (Z_it_max)
        :param itz_ogr_min: Стартовый метод: Учет Qmin с итерации (Z_it_min)
        :param min_nodes_in_island: Минимальное число узлов в острове (Min_nodes)
        """
        VariableDefRowId.make_changes(self, column=self.list_key[0], row_id=0, value=float(neb_p))
        VariableDefRowId.make_changes(self, column=self.list_key[1], row_id=0, value=it_max)
        VariableDefRowId.make_changes(self, column=self.list_key[2], row_id=0, value=start)
        VariableDefRowId.make_changes(self, column=self.list_key[3], row_id=0, value=flot)
        VariableDefRowId.make_changes(self, column=self.list_key[4], row_id=0, value=float(dv_min))
        VariableDefRowId.make_changes(self, column=self.list_key[5], row_id=0, value=float(dv_max))
        VariableDefRowId.make_changes(self, column=self.list_key[6], row_id=0, value=dd_max)
        VariableDefRowId.make_changes(self, column=self.list_key[7], row_id=0, value=status)
        VariableDefRowId.make_changes(self, column=self.list_key[8], row_id=0, value=rr)
        VariableDefRowId.make_changes(self, column=self.list_key[9], row_id=0, value=wt)
        VariableDefRowId.make_changes(self, column=self.list_key[10], row_id=0, value=gen_p)
        VariableDefRowId.make_changes(self, column=self.list_key[11], row_id=0, value=method)
        VariableDefRowId.make_changes(self, column=self.list_key[12], row_id=0, value=method_ogr)
        VariableDefRowId.make_changes(self, column=self.list_key[13], row_id=0, value=print_mode)
        VariableDefRowId.make_changes(self, column=self.list_key[14], row_id=0, value=qmax)
        VariableDefRowId.make_changes(self, column=self.list_key[15], row_id=0, value=min_x)
        VariableDefRowId.make_changes(self, column=self.list_key[16], row_id=0, value=calc_tr)
        VariableDefRowId.make_changes(self, column=self.list_key[17], row_id=0, value=nag_p)
        VariableDefRowId.make_changes(self, column=self.list_key[18], row_id=0, value=rem_breaker)
        VariableDefRowId.make_changes(self, column=self.list_key[19], row_id=0, value=gram)
        VariableDefRowId.make_changes(self, column=self.list_key[20], row_id=0, value=ctrl_baza)
        VariableDefRowId.make_changes(self, column=self.list_key[21], row_id=0, value=itz)
        VariableDefRowId.make_changes(self, column=self.list_key[22], row_id=0, value=itz_ogr_max)
        VariableDefRowId.make_changes(self, column=self.list_key[23], row_id=0, value=itz_ogr_min)
        VariableDefRowId.make_changes(self, column=self.list_key[24], row_id=0, value=min_nodes_in_island)


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


class AltUnit(VariableDefRowId):
    """
    Класс выставляет параметров настройки "Описание альтернативных единиц измерения"
    """

    def __init__(self, rastr_win=RASTR, table=alt_unit_table, switch_command_line=False):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in alt_unit_attributes.keys():
            self.list_key.append(key)
        self.switch_command_line = switch_command_line
        VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table, switch_command_line=switch_command_line)

    def set(self,
            row_id=0,
            Active='',
            Unit='',
            Alt='',
            Formula='',
            Prec='',
            Tabl=''):
        VariableDefRowId.make_changes(self, column=self.list_key[0], row_id=row_id, value=int(Active))
        VariableDefRowId.make_changes(self, column=self.list_key[1], row_id=row_id, value=str(Unit))
        VariableDefRowId.make_changes(self, column=self.list_key[2], row_id=row_id, value=str(Alt))
        VariableDefRowId.make_changes(self, column=self.list_key[3], row_id=row_id, value=str(Formula))
        VariableDefRowId.make_changes(self, column=self.list_key[4], row_id=row_id, value=str(Prec))
        VariableDefRowId.make_changes(self, column=self.list_key[5], row_id=row_id, value=str(Tabl))


class UtCommon(VariableDefRowId):
    """
    Класс выставляет параметров настройки "Описание альтернативных единиц измерения"
    """

    def __init__(self, rastr_win=RASTR, table=ut_common_table, switch_command_line=False):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in ut_common_attributes.keys():
            self.list_key.append(key)
        self.switch_command_line = switch_command_line
        VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table, switch_command_line=switch_command_line)

    def set(self,
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
            sum_kfc='',
            ds=0,
            it='',
            Status=0,
            KorrT=25,
            KorrPer='',
            KorrVib='',
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
            dyn_find_pred=0):
        VariableDefRowId.make_changes(self, column=self.list_key[0], row_id=0, value=float(maxs))
        VariableDefRowId.make_changes(self, column=self.list_key[1], row_id=0, value=float(maxv))
        VariableDefRowId.make_changes(self, column=self.list_key[2], row_id=0, value=float(maxd))
        VariableDefRowId.make_changes(self, column=self.list_key[3], row_id=0, value=float(maxa))
        VariableDefRowId.make_changes(self, column=self.list_key[4], row_id=0, value=float(iter))
        VariableDefRowId.make_changes(self, column=self.list_key[5], row_id=0, value=float(tip))
        VariableDefRowId.make_changes(self, column=self.list_key[6], row_id=0, value=float(f_ots))
        VariableDefRowId.make_changes(self, column=self.list_key[7], row_id=0, value=float(add_d))
        VariableDefRowId.make_changes(self, column=self.list_key[8], row_id=0, value=float(ekstr))
        VariableDefRowId.make_changes(self, column=self.list_key[9], row_id=0, value=float(kfc))
        VariableDefRowId.make_changes(self, column=self.list_key[10], row_id=0, value=float(sum_kfc))
        VariableDefRowId.make_changes(self, column=self.list_key[11], row_id=0, value=float(ds))
        VariableDefRowId.make_changes(self, column=self.list_key[12], row_id=0, value=float(it))
        VariableDefRowId.make_changes(self, column=self.list_key[13], row_id=0, value=float(Status))
        VariableDefRowId.make_changes(self, column=self.list_key[14], row_id=0, value=float(KorrT))
        VariableDefRowId.make_changes(self, column=self.list_key[15], row_id=0, value=float(KorrPer))
        VariableDefRowId.make_changes(self, column=self.list_key[16], row_id=0, value=float(KorrVib))
        VariableDefRowId.make_changes(self, column=self.list_key[17], row_id=0, value=float(enable_contr))
        VariableDefRowId.make_changes(self, column=self.list_key[18], row_id=0, value=float(dis_v_contr))
        VariableDefRowId.make_changes(self, column=self.list_key[19], row_id=0, value=float(dis_p_contr))
        VariableDefRowId.make_changes(self, column=self.list_key[20], row_id=0, value=float(dis_i_contr))
        VariableDefRowId.make_changes(self, column=self.list_key[21], row_id=0, value=float(ss_calc))
        VariableDefRowId.make_changes(self, column=self.list_key[21], row_id=0, value=float(criterion))
        VariableDefRowId.make_changes(self, column=self.list_key[22], row_id=0, value=float(no_crit_d_ba))
        VariableDefRowId.make_changes(self, column=self.list_key[23], row_id=0, value=float(no_crit_d_coa))
        VariableDefRowId.make_changes(self, column=self.list_key[24], row_id=0, value=float(no_crit_d_ga))
        VariableDefRowId.make_changes(self, column=self.list_key[25], row_id=0, value=float(save_files_filter))
        VariableDefRowId.make_changes(self, column=self.list_key[26], row_id=0, value=float(save_files_path))
        VariableDefRowId.make_changes(self, column=self.list_key[27], row_id=0, value=float(stop_u_n))
        VariableDefRowId.make_changes(self, column=self.list_key[28], row_id=0, value=float(dyn_find_pred))


if __name__ == '__main__':
    from RastrWin.loading.load import load_file
    from RastrWin.loading.shablon import shablon_file_regime
    from RastrWin.loading.shablon import test_195_rg
    from RastrWin.object_rastr import RASTR
    from RastrWin.loading.save import save_file

    load_file(rastr_win=RASTR, file_path=test_195_rg, shablon=shablon_file_regime)
    set = SetEkviv(rastr_win=RASTR)

    set.set(selekv=1,
            smart=1,
            zmax=85)
    save_file(rastr_win=RASTR, file_path=r'C:\Users\Ohrimenko_AG\Desktop\65\t.rg2', shablon=shablon_file_regime,
              switch_command_line=True)
