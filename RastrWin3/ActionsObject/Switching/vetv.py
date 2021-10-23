# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Tables.Vetv.vetv import Vetv
from RastrWinLib.Tools.tools import Tools


class SwitchVetv:

    def __init__(self,
                 rastr_win=RASTR,
                 table=Vetv.table,
                 switch_command_line=False):
        f"""
        Класс выполняет отключение и включение ветви в RastrWin3
        :param rastr_win: {Tools.RastrDoc};
        :param table: название таблицы RastrWin3;
        :param switch_command_line: {Tools.switch_command_line_doc};
        """
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)
        self.switch_command_line = switch_command_line

    def off(self,
            ip,
            iq,
            np=0):
        """

        :param ip: начало ветви;
        :param iq: конец ветви;
        :param np: номер параллельности ветви;
        :return:
        """
        if self.switch_command_line is not False:
            print(f'Отключение объекта ip={ip}, iq={iq}, np={np}')
        self.table.SetSel(f"(ip={ip} & iq={iq} & np={np})|(ip={iq} & iq={ip} & np={np})")
        row_id = self.table.FindNextSel(-1)
        if row_id != (-1):
            switch_sta_off = self.table.Cols('sta').Z(row_id)
            if switch_sta_off != 1:
                self.table.Cols("sta").Calc("1")
            else:
                print(f'\t\tОбъект ip={ip},iq={iq},np={np} уже отключен!')
        else:
            print(f'\t\tОбъект ip={ip},iq={iq},np={np} не найдет в таблице {self.table.Name}')

    def on(self,
           ip,
           iq,
           np=0):
        """

        :param ip: начало ветви;
        :param iq: конец ветви;
        :param np: номер параллельности ветви;
        :return:
        """
        if self.switch_command_line is not False:
            print(f'Включение объекта ip={ip}, iq={iq}, np={np}')
        self.table.SetSel(f'(ip={ip} & iq={iq} & np={np})|(ip={iq} & iq={ip} & np={np})')
        row_id = self.table.FindNextSel(-1)
        if row_id != (-1):
            switch_sta_on = self.table.Cols('sta').Z(row_id)
            if switch_sta_on != 0:
                self.table.Cols("sta").Calc("0")
            else:
                print(f'\t\tОбъект ip={ip},iq={iq},np={np} уже отключен!')
        else:
            print(f'\t\tОбъект ip={ip},iq={iq},np={np} не найдет в таблице {self.table.Name}')

    def on_row_id(self, row_id):
        """

        :param row_id:
        :return:
        """
        if self.switch_command_line is not False:
            print(f'Включение объекта row_id={row_id}')
        if row_id != (-1) and row_id is not None:
            switch_sta_on = self.table.Cols('sta').Z(row_id)
            if switch_sta_on != 0:
                self.table.Cols("sta").Calc("0")
            else:
                print(f'\t\tОбъект row_id={row_id} уже отключен!')
        else:
            print(f'\t\tОбъект row_id={row_id} не найдет в таблице {self.table.Name}')

    def off_row_id(self, row_id):
        """

        :param row_id:
        :return:
        """
        if self.switch_command_line is not False:
            print(f'Отключение объекта row_id={row_id}')

        if row_id != (-1) and row_id is not None:
            switch_sta_off = self.table.Cols('sta').Z(row_id)
            if switch_sta_off != 1:
                self.table.Cols("sta").Calc("1")
            else:
                print(f'\t\tОбъект row_id={row_id} уже отключен!')
        else:
            print(f'\t\tОбъект row_id={row_id} не найдет в таблице {self.table.Name}')
