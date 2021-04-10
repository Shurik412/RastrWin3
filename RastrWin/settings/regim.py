# -*- coding: utf-8 -*-
from RastrWin.AstraRastr import RASTR
from RastrWin.variables.variable_parametrs import VariableDefRowId
from RastrWin.tables.tablesAttributes import com_regim_table, com_regim_attributes


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
