# -*- coding: utf-8 -*-

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.tables_attributes import com_ekviv_table, com_ekviv_attributes
from RastrWinLib.variables.variable_parametrs import Variable


def set_com_ekviv(selekv=0,
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
                  otm_n=0,
                  switch_command_line=False,
                  ):
    list_key = []
    for key in com_ekviv_attributes.keys():
        list_key.append(key)

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

    variable_def_rowid = Variable(rastr_win=RASTR,
                                  switch_command_line=switch_command_line)

    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[0], row_id=0, value=selekv)
    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[1], row_id=0, value=met_ekv)
    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[2], row_id=0, value=tip_ekv)
    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[3], row_id=0, value=ekvgen)
    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[4], row_id=0, value=tip_gen)
    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[5], row_id=0, value=kfc_x)
    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[6], row_id=0, value=pot_gen)
    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[7], row_id=0, value=kpn)
    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[8], row_id=0, value=tip_sxn)
    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[9], row_id=0, value=smart)
    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[10], row_id=0, value=zmax)
    variable_def_rowid.make_changes_row(table=com_ekviv_table, column=list_key[11], row_id=0, value=otm_n)

    if switch_command_line is not False:
        return print(
            f'Внесены изменения в настройки "Общие параметры эквивалентирования" (таблица "Эквивалент": com_ekviv)')
    else:
        return True


class SetEkviv:
    """
    Класс выставляет параметров настройки "Эквивалент"
    """

    def __init__(self,
                 rastr_win=RASTR,
                 table=com_ekviv_table,
                 switch_command_line=False):
        self.rastr_win = rastr_win
        self.table = table
        self.list_key = []
        for key in com_ekviv_attributes.keys():
            self.list_key.append(key)
        self.switch_command_line = switch_command_line

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

        self.variable_def_rowid.make_changes(column=self.list_key[0], row_id=0, value=selekv)
        self.variable_def_rowid.make_changes(column=self.list_key[1], row_id=0, value=met_ekv)
        self.variable_def_rowid.make_changes(column=self.list_key[2], row_id=0, value=tip_ekv)
        self.variable_def_rowid.make_changes(column=self.list_key[3], row_id=0, value=ekvgen)
        self.variable_def_rowid.make_changes(column=self.list_key[4], row_id=0, value=tip_gen)
        self.variable_def_rowid.make_changes(column=self.list_key[5], row_id=0, value=kfc_x)
        self.variable_def_rowid.make_changes(column=self.list_key[6], row_id=0, value=pot_gen)
        self.variable_def_rowid.make_changes(column=self.list_key[7], row_id=0, value=kpn)
        self.variable_def_rowid.make_changes(column=self.list_key[8], row_id=0, value=tip_sxn)
        self.variable_def_rowid.make_changes(column=self.list_key[9], row_id=0, value=smart)
        self.variable_def_rowid.make_changes(column=self.list_key[10], row_id=0, value=zmax)
        self.variable_def_rowid.make_changes(column=self.list_key[11], row_id=0, value=otm_n)

        if self.switch_command_line is not False:
            return print(
                f'Внесены изменения в настройки "Общие параметры эквивалентирования" (таблица "Эквивалент": com_ekviv)')
        else:
            return True
