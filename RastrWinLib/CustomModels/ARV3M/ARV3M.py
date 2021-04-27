# -*- coding: utf-8 -*-
#  ---------------- Модель ARV-3M ----------------
# Модель автоматического регулятора возбуждения типа ARV3M,
# реализованная в ПК RUSTab, состоит из макроблоков.
# Параметры модели AVR-3M_res.xmldev заносятся в таблицу «АРВ (ИД)».

import RastrWinLib.CustomModels.ARV3M.Parameters_ARV3M as parameter
import RastrWinLib.tables.Dynamic.ExcControl as ExcControl
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.log_tools.tools import separator_grid
from RastrWinLib.variables.variable_parametrs import Variable


class ARV3M(Variable, GettingParameter):

    def __init__(self, rastr_win, switch_command_line=False):
        """

        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param switch_command_line: True/False - выводит сообщения в протокол.
        """
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

        self.variable_ = Variable.__init__(self, rastr_win=self.rastr_win, switch_command_line=False)
        self.get_ = GettingParameter.__init__(self, rastr_win=rastr_win)

    def change_parameters(self,
                          Id=None,
                          row_id=None,
                          Ku=parameter.Ku,
                          K_Q=parameter.K_Q,
                          Kif1=parameter.Kif1,
                          T1if=parameter.T1if,
                          Ku1=parameter.Ku1,
                          T1u1=parameter.T1u1,
                          K_P=parameter.K_P,
                          K_Ia=parameter.K_Ia,
                          Tf=parameter.Tf,
                          Kf=parameter.Kf,
                          Kf1=parameter.Kf1,
                          TINT=parameter.TINT):
        """
        Метод change_parameters -
        :param Id: Номер возбудителя;
        :param row_id: порядковый номер в таблице (от 0 до [max.count]);
        :param Ku: Коэффициент усиления пропорционального канала регулятора напряжения;
        :param K_Q: Коэффициент усиления канала по производной тока ротора;
        :param Kif1: Коэффициент усиления канала по производной тока ротора;
        :param T1if: Постоянная времени дифференциру-ющего звена в канале по производной тока ротора;
        :param Ku1: Коэффициент усиления канала по производной напряжения;
        :param T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения;
        :param K_P: Коэффициент усиления выходного сигнала ОМВ;
        :param K_Ia: Уставка ограничителя максимального тока ротора;
        :param Tf: Постоянная времени дифференцирующего звена в канале по частоте;
        :param Kf: Коэффициент усиления в канале по частоте;
        :param Kf1: Коэффициент усиления в канале по производной частоты;
        :param TINT: Постоянная времени интегратора
        :return:
        """
        if Id is not None:
            # Ku
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.Ku,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=Ku)
            # K_Q
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.K_Q,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=K_Q)
            # Kif1
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.Kif1,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=Kif1)
            # T1if
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.T1if,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=T1if)
            # Ku1
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.Ku1,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=Ku1)
            # T1u1
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.T1u1,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=T1u1)
            # K_P
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.K_P,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=K_P)
            # K_Ia
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.K_Ia,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=K_Ia)
            # Tf
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.Tf,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=Tf)
            # Kf
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.Kf,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=Kf)
            # Kf1
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.Kf1,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=Kf1)
            # TINT
            self.variable_.make_changes_setsel(table=ExcControl.table,
                                               column=ExcControl.TINT,
                                               key=f'{ExcControl.Id}={Id}',
                                               value=TINT)

        if row_id is None:
            # Ku
            Ku = self.get_.get_param(table=ExcControl.table,
                                     column=ExcControl.Ku,
                                     key=f'{ExcControl.Id}={Id}')
            # K_Q
            self.get_.get_param(table=ExcControl.table,
                                column=ExcControl.K_Q,
                                key=f'{ExcControl.Id}={Id}')
            # Kif1
            Kif1 = self.get_.get_param(table=ExcControl.table,
                                       column=ExcControl.Kif1,
                                       key=f'{ExcControl.Id}={Id}')
            # T1if
            T1if = self.get_.get_param(table=ExcControl.table,
                                       column=ExcControl.T1if,
                                       key=f'{ExcControl.Id}={Id}')
            # Ku1
            Ku1 = self.get_.get_param(table=ExcControl.table,
                                      column=ExcControl.Ku1,
                                      key=f'{ExcControl.Id}={Id}')
            # T1u1
            T1u1 = self.get_.get_param(table=ExcControl.table,
                                       column=ExcControl.T1u1,
                                       key=f'{ExcControl.Id}={Id}')
            # K_P
            K_P = self.get_.get_param(table=ExcControl.table,
                                      column=ExcControl.K_P,
                                      key=f'{ExcControl.Id}={Id}')
            # K_Ia
            K_Ia = self.get_.get_param(table=ExcControl.table,
                                       column=ExcControl.K_Ia,
                                       key=f'{ExcControl.Id}={Id}')
            # Tf
            Tf = self.get_.get_param(table=ExcControl.table,
                                     column=ExcControl.Tf,
                                     key=f'{ExcControl.Id}={Id}')
            # Kf
            Kf = self.get_.get_param(table=ExcControl.table,
                                     column=ExcControl.Kf,
                                     key=f'{ExcControl.Id}={Id}')
            # Kf1
            Kf1 = self.get_.get_param(table=ExcControl.table,
                                      column=ExcControl.Kf1,
                                      key=f'{ExcControl.Id}={Id}')
            # TINT
            TINT = self.get_.get_param(table=ExcControl.table,
                                       column=ExcControl.TINT,
                                       key=f'{ExcControl.Id}={Id}')
            print(
                f'{separator_grid}'
                f'Параметры АРВ: ARV-3M.'
                f'- Id: Номер возбудителя: {Id};\n'
                f'- row_id: порядковый номер: {row_id};\n'
                f'- Ku: Коэффициент усиления пропорционального канала регулятора напряжения: {Ku};\n'
                f'- K_Q: Коэффициент усиления канала по производной тока ротора: {K_Q};\n'
                f'- Kif1: Коэффициент усиления канала по производной тока ротора: {Kif1};\n'
                f'- T1if: Постоянная времени дифференцирующего звена в канале по производной тока ротора: {T1if};\n'
                f'- Ku1: Коэффициент усиления канала по производной напряжения: {Ku1};\n'
                f'- T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения: {T1u1};\n'
                f'- K_P: Коэффициент усиления выходного сигнала ОМВ: {K_P};\n'
                f'- K_Ia: Уставка ограничителя максимального тока ротора: {K_Ia};\n'
                f'- Tf: Постоянная времени дифференцирующего звена в канале по частоте: {Tf};\n'
                f'- Kf: Коэффициент усиления в канале по частоте: {Kf};\n'
                f'- Kf1: Коэффициент усиления в канале по производной частоты: {Kf1};\n'
                f'- TINT: Постоянная времени интегратора: {TINT};\n'
                f'{separator_grid}'
            )
