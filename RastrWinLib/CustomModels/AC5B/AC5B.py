# -*- coding: utf-8 -*-
#  ---------------- Модель AC5B ----------------
# Модель системы возбуждения типа AC5B,
# реализованная в ПК RUSTab, состоит одного макроблока.
# Параметры системы возбуждения AC5B.xmldev заносятся в ПК RUSTab в таблицу «ВозбудителиIEEE».

import RastrWinLib.CustomModels.AC5B.Parameters_AC5B as parameter
import RastrWinLib.tables.Dynamic.DFWIEEE421 as DFWIEEE421
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.variables.variable_parametrs import Variable


class AC5B(Variable, GettingParameter):

    def __init__(self, rastr_win, switch_command_line=False):
        """

        :param rastr_win: com - объект RastrWin3;
        :param switch_command_line:
        """
        self.switch_command_line = switch_command_line
        self.rastr_win = rastr_win
        self.variable_ = Variable.__init__(self, rastr_win=self.rastr_win, switch_command_line=False)
        self.get_ = GettingParameter.__init__(self, rastr_win=self.rastr_win)

    def change_parameters(self,
                          Id=None,
                          row_id=None,
                          Kpr=parameter.Kpr,
                          Tb=parameter.Tb,
                          Ka=parameter.Ka,
                          Vrmax=parameter.Vrmax,
                          Vrmin=parameter.Vrmin,
                          Te=parameter.Te,
                          Aex=parameter.Aex,
                          Bex=parameter.Bex):
        """

        :param Id: Номер возбудителя;
        :param row_id: порядковый номер в таблице (от 0 до [max.count]);
        :param Kpr: Коэффициент усиления дифференциального звена;
        :param Tb: Постоянная времени дифференциального звена;
        :param Ka: Пропорциональный коэффициент усиления регулятора напряжения;
        :param Vrmax: Максимальное ограничение интегрального звена;
        :param Vrmin: Минимальное ограничение интегрального звена;
        :param Te: Постоянная времени интегратора возбудителя;
        :param Aex: Коэффициент экспоненты (задание насыщения);
        :param Bex: Степень экспоненты (задание насыщения);
        :return:
        """
        if Id is not None:
            # Kpr
            self.variable_.make_changes_setsel(table=DFWIEEE421.table,
                                               column=DFWIEEE421.Kpr,
                                               key=f'{DFWIEEE421.Id}={Id}',
                                               value=Kpr)
            # Tb
            self.variable_.make_changes_setsel(table=DFWIEEE421.table,
                                               column=DFWIEEE421.Tb,
                                               key=f'{DFWIEEE421.Id}={Id}',
                                               value=Tb)
            # Ka
            self.variable_.make_changes_setsel(table=DFWIEEE421.table,
                                               column=DFWIEEE421.Ka,
                                               key=f'{DFWIEEE421.Id}={Id}',
                                               value=Ka)
            # Vrmax
            self.variable_.make_changes_setsel(table=DFWIEEE421.table,
                                               column=DFWIEEE421.Vrmax,
                                               key=f'{DFWIEEE421.Id}={Id}',
                                               value=Vrmax)
            # Vrmin
            self.variable_.make_changes_setsel(table=DFWIEEE421.table,
                                               column=DFWIEEE421.Vrmin,
                                               key=f'{DFWIEEE421.Id}={Id}',
                                               value=Vrmin)
            # Te
            self.variable_.make_changes_setsel(table=DFWIEEE421.table,
                                               column=DFWIEEE421.Te,
                                               key=f'{DFWIEEE421.Id}={Id}',
                                               value=Te)
            # Aex
            self.variable_.make_changes_setsel(table=DFWIEEE421.table,
                                               column=DFWIEEE421.Aex,
                                               key=f'{DFWIEEE421.Id}={Id}',
                                               value=Aex)

            # Bex
            self.variable_.make_changes_setsel(table=DFWIEEE421.table,
                                               column=DFWIEEE421.Bex,
                                               key=f'{DFWIEEE421.Id}={Id}',
                                               value=Bex)

        else:
            pass

        if row_id is not None:
            # Kpr
            self.variable_.make_changes_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Kpr,
                                            row_id=row_id,
                                            value=Kpr)
            # Tb
            self.variable_.make_changes_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Tb,
                                            row_id=row_id,
                                            value=Tb)
            # Ka
            self.variable_.make_changes_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Ka,
                                            row_id=row_id,
                                            value=Ka)
            # Vrmax
            self.variable_.make_changes_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Vrmax,
                                            row_id=row_id,
                                            value=Vrmax)
            # Vrmin
            self.variable_.make_changes_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Vrmin,
                                            row_id=row_id,
                                            value=Vrmin)
            # Te
            self.variable_.make_changes_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Te,
                                            row_id=row_id,
                                            value=Te)
            # Aex
            self.variable_.make_changes_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Aex,
                                            row_id=row_id,
                                            value=Aex)

            # Bex
            self.variable_.make_changes_row(table=DFWIEEE421.table,
                                            column=DFWIEEE421.Bex,
                                            row_id=row_id,
                                            value=Bex)
        else:
            pass

    def get(self, Id=None, row_id=None):
        """
        Метод get -
        :param Id:
        :param row_id:
        :return:
        """
        if Id is not None:
            # Kpr
            k_pr = self.get_.get_param(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Kpr,
                                       key=f'{DFWIEEE421.Id}={Id}')
            # Tb
            tb = self.get_.get_param(table=DFWIEEE421.table,
                                     column=DFWIEEE421.Kpr,
                                     key=f'{DFWIEEE421.Id}={Id}')
            # Ka
            ka = self.get_.get_param(table=DFWIEEE421.table,
                                     column=DFWIEEE421.Ka,
                                     key=f'{DFWIEEE421.Id}={Id}')
            # Vrmax
            vrmax = self.get_.get_param(table=DFWIEEE421.table,
                                        column=DFWIEEE421.Vrmax,
                                        key=f'{DFWIEEE421.Id}={Id}')
            # Vrmin
            vrmin = self.get_.get_param(table=DFWIEEE421.table,
                                        column=DFWIEEE421.Vrmin,
                                        key=f'{DFWIEEE421.Id}={Id}')
            # Te
            te = self.get_.get_param(table=DFWIEEE421.table,
                                     column=DFWIEEE421.Te,
                                     key=f'{DFWIEEE421.Id}={Id}')
            # Aex
            aex = self.get_.get_param(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Aex,
                                      key=f'{DFWIEEE421.Id}={Id}')
            # Bex
            bex = self.get_.get_param(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Bex,
                                      key=f'{DFWIEEE421.Id}={Id}')

        if row_id is not None:
            # Kpr
            k_pr = self.get_.get_cell(table=DFWIEEE421.table,
                                      column=DFWIEEE421.Kpr,
                                      row_id=row_id)
            # Tb
            tb = self.get_.get_cell(table=DFWIEEE421.table,
                                    column=DFWIEEE421.Kpr,
                                    row_id=row_id)
            # Ka
            ka = self.get_.get_cell(table=DFWIEEE421.table,
                                    column=DFWIEEE421.Ka,
                                    row_id=row_id)
            # Vrmax
            vrmax = self.get_.get_cell(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vrmax,
                                       row_id=row_id)
            # Vrmin
            vrmin = self.get_.get_cell(table=DFWIEEE421.table,
                                       column=DFWIEEE421.Vrmin,
                                       row_id=row_id)
            # Te
            te = self.get_.get_cell(table=DFWIEEE421.table,
                                    column=DFWIEEE421.Te,
                                    row_id=row_id)
            # Aex
            aex = self.get_.get_cell(table=DFWIEEE421.table,
                                     column=DFWIEEE421.Aex,
                                     row_id=row_id)
            # Bex
            bex = self.get_.get_cell(table=DFWIEEE421.table,
                                     column=DFWIEEE421.Bex,
                                     row_id=row_id)
