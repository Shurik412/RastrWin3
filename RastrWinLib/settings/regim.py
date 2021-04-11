# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.tables_attributes import com_regim_table, com_regim_attributes
from RastrWinLib.variables.variable_parametrs import VariableDefRowId


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

        self.variable_def_rowid = VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table,
                                                            switch_command_line=switch_command_line)

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
        self.variable_def_rowid.make_changes(column=self.list_key[0], row_id=0, value=float(neb_p))
        self.variable_def_rowid.make_changes(column=self.list_key[1], row_id=0, value=it_max)
        self.variable_def_rowid.make_changes(column=self.list_key[2], row_id=0, value=start)
        self.variable_def_rowid.make_changes(column=self.list_key[3], row_id=0, value=flot)
        self.variable_def_rowid.make_changes(column=self.list_key[4], row_id=0, value=float(dv_min))
        self.variable_def_rowid.make_changes(column=self.list_key[5], row_id=0, value=float(dv_max))
        self.variable_def_rowid.make_changes(column=self.list_key[6], row_id=0, value=dd_max)
        self.variable_def_rowid.make_changes(column=self.list_key[7], row_id=0, value=status)
        self.variable_def_rowid.make_changes(column=self.list_key[8], row_id=0, value=rr)
        self.variable_def_rowid.make_changes(column=self.list_key[9], row_id=0, value=wt)
        self.variable_def_rowid.make_changes(column=self.list_key[10], row_id=0, value=gen_p)
        self.variable_def_rowid.make_changes(column=self.list_key[11], row_id=0, value=method)
        self.variable_def_rowid.make_changes(column=self.list_key[12], row_id=0, value=method_ogr)
        self.variable_def_rowid.make_changes(column=self.list_key[13], row_id=0, value=print_mode)
        self.variable_def_rowid.make_changes(column=self.list_key[14], row_id=0, value=qmax)
        self.variable_def_rowid.make_changes(column=self.list_key[15], row_id=0, value=min_x)
        self.variable_def_rowid.make_changes(column=self.list_key[16], row_id=0, value=calc_tr)
        self.variable_def_rowid.make_changes(column=self.list_key[17], row_id=0, value=nag_p)
        self.variable_def_rowid.make_changes(column=self.list_key[18], row_id=0, value=rem_breaker)
        self.variable_def_rowid.make_changes(column=self.list_key[19], row_id=0, value=gram)
        self.variable_def_rowid.make_changes(column=self.list_key[20], row_id=0, value=ctrl_baza)
        self.variable_def_rowid.make_changes(column=self.list_key[21], row_id=0, value=itz)
        self.variable_def_rowid.make_changes(column=self.list_key[22], row_id=0, value=itz_ogr_max)
        self.variable_def_rowid.make_changes(column=self.list_key[23], row_id=0, value=itz_ogr_min)
        self.variable_def_rowid.make_changes(column=self.list_key[24], row_id=0, value=min_nodes_in_island)
        if self.switch_command_line is not False:
            return print(f'Внесены изменения в настройки "Общие параметры режима" (таблица "Режим": com_regim)')
        else:
            return True
