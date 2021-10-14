# -*- coding: utf-8 -*-
#  ---------------- Модель ARV-2M_БСВ ----------------
# Модель автоматического регулятора возбуждения типа АРВ-2М_БСВ (Силмаш),
# реализованная в ПК RUSTab, состоит из следующих макроблоков:
# 1.АРВ: AVR2M_bsv.xmldev;
# 2.Релейная форсировка: AVR-2M_RF.xmldev.
# Параметры модели AVR2M_bsv.xmldev заносятся в таблицу «АРВ (ИД)».

from RastrWinLib.tables.Dynamic.ExcControl import ExcControl
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Getting.get import GettingParameter
from RastrWinLib.tools.tools import separator_two
from RastrWinLib.variables.variable_parametrs import Variable


class Parameters:
    """
    Модель автоматического регулятора возбуждения типа АРВ-2М_БСВ (Силмаш),
     реализованная в ПК RUSTab, состоит из следующих макроблоков:
    1.АРВ: AVR2M_bsv.xmldev;
    2.Релейная форсировка: AVR-2M_RF.xmldev.
    Параметры модели AVR2M_bsv.xmldev заносятся в таблицу «АРВ (ИД)».
    Типовые значение параметров настройки, приняты согласно информации
    от производителя системы возбуждения.
     В случае наличия листинга настроек для конкретного энергообъекта
     необходимо использовать фактические параметры настройки.

     ---- Параметры модели AVR-2M_RF.xmldev заносятся в таблицу «Форсировка (ИД)». ----
     Типовые значение параметров настройки, приняты согласно информации
     от производителя системы возбуждения. В случае наличия листинга настроек
     для конкретного энергообъекта необходимо использовать фактические параметры настройки.
    """

    Ku: float = 10.0  # Коэффициент усиления регулятора
    K_Q: float = 1.0  # Коэффициент усиления канала по производной тока ротора
    Kif1: float = 1.0  # Коэффициент усиления канала по производной тока ротора
    T1if: float = 0.05  # Постоянная времени дифференцирующего звена в канале по производной тока ротора
    Ku1: float = 3.0  # Коэффициент усиления канала по производной напряжения
    T1u1: float = 0.06  # Постоянная времени дифференцирующего звена в канале по производной напряжения
    K_P: float = 5.0  # Коэффициент усиления выходного сигнала ОМВ
    K_Ia: float = 2.0  # Уставка по току ротора
    Tf: float = 2.0  # Постоянная времени дифференцирующего звена в канале по частоте
    Kf: float = 1.0  # Коэффициент усиления в канале по частоте
    Kf1: float = 1.0  # Коэффициент усиления в канале по производной частоты
    TINT: float = 1.0  # Постоянная времени интегратора

    # Параметры модели AVR-2M_RF.xmldev заносятся в таблицу «Форсировка (ИД)».
    Ubf: float = 0.85  # Напряжение ввода форсировки
    Uef: float = 0.9  # Напряжение снятие форсировки
    Tz_out: float = 0.1  # Задержка на снятие форсировки


def change_parameters_ARV2M_BSV(
        Id=None,
        row_id=None,
        Ku: float = Parameters.Ku,
        K_Q: float = Parameters.K_Q,
        Kif1: float = Parameters.Kif1,
        T1if: float = Parameters.T1if,
        Ku1: float = Parameters.Ku1,
        T1u1: float = Parameters.T1u1,
        K_P: float = Parameters.K_P,
        K_Ia: float = Parameters.K_Ia,
        Tf: float = Parameters.Tf,
        Kf: float = Parameters.Kf,
        Kf1: float = Parameters.Kf1,
        TINT: float = Parameters.TINT,
        switch_command_line: bool = False):
    """

    :param Id: номер возбудителя;
    :param row_id: порядковый номер в таблице (от 0 до [max.count]);
    :param Ku: Коэффициент усиления регулятора;
    :param K_Q: Коэффициент усиления канала по производной тока ротора;
    :param Kif1: Коэффициент усиления канала по производной тока ротора;
    :param T1if: Постоянная времени дифференцирующего звена в канале по производной тока ротора;
    :param Ku1: Коэффициент усиления канала по производной напряжения;
    :param T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения;
    :param K_P: Коэффициент усиления выходного сигнала ОМВ;
    :param K_Ia: Уставка по току ротора;
    :param Tf: Постоянная времени дифференцирующего звена в канале по частоте;
    :param Kf: Коэффициент усиления в канале по частоте;
    :param Kf1: Коэффициент усиления в канале по производной частоты;
    :param TINT: Постоянная времени интегратора;
    :param switch_command_line: True/False - вывод сообщений в протакол;
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)
    get_ = GettingParameter(rastr_win=rastr_win)

    if Id is not None and row_id is None:
        # Ku
        if switch_command_line is not None:
            ku_before = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Ku,
                                         Id=Id)
        else:
            ku_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Ku,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Ku)

        if switch_command_line is not None:
            ku_after = get_.get_cell_id(table=ExcControl.table,
                                        column=ExcControl.Ku,
                                        Id=Id)
        else:
            ku_after = None

        # K_Q
        if switch_command_line is not None:
            k_q_before = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.K_Q,
                                          Id=Id)
        else:
            k_q_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Ku,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_Q)

        if switch_command_line is not None:
            k_q_after = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.K_Q,
                                         Id=Id)
        else:
            k_q_after = None

        # Kif1
        if switch_command_line is not None:
            kif1_before = get_.get_cell_id(table=ExcControl.table,
                                           column=ExcControl.Kif1,
                                           Id=Id)
        else:
            kif1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kif1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kif1)

        if switch_command_line is not None:
            kif1_after = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.Kif1,
                                          Id=Id)
        else:
            kif1_after = None

        # T1if
        if switch_command_line is not None:
            t1if_before = get_.get_cell_id(table=ExcControl.table,
                                           column=ExcControl.T1if,
                                           Id=Id)
        else:
            t1if_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.T1if,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=T1if)

        if switch_command_line is not None:
            t1if_after = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.T1if,
                                          Id=Id)
        else:
            t1if_after = None

        # Ku1
        if switch_command_line is not None:
            ku1_before = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.Ku1,
                                          Id=Id)
        else:
            ku1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Ku1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Ku1)

        if switch_command_line is not None:
            ku1_after = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Ku1,
                                         Id=Id)
        else:
            ku1_after = None

        # T1u1
        if switch_command_line is not None:
            t1u1_before = get_.get_cell_id(table=ExcControl.table,
                                           column=ExcControl.T1u1,
                                           Id=Id)
        else:
            t1u1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.T1u1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=T1u1)

        if switch_command_line is not None:
            t1u1_after = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.T1u1,
                                          Id=Id)
        else:
            t1u1_after = None

        # K_P
        if switch_command_line is not None:
            k_p_before = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.K_P,
                                          Id=Id)
        else:
            k_p_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_P,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_P)

        if switch_command_line is not None:
            k_p_after = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.K_P,
                                         Id=Id)
        else:
            k_p_after = None

        # K_Ia
        if switch_command_line is not None:
            k_ia_before = get_.get_cell_id(table=ExcControl.table,
                                           column=ExcControl.K_Ia,
                                           Id=Id)
        else:
            k_ia_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_Ia,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_Ia)

        if switch_command_line is not None:
            k_ia_after = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.K_Ia,
                                          Id=Id)
        else:
            k_ia_after = None

        # Tf
        if switch_command_line is not None:
            tf_before = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Tf,
                                         Id=Id)
        else:
            tf_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Tf,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Tf)

        if switch_command_line is not None:
            tf_after = get_.get_cell_id(table=ExcControl.table,
                                        column=ExcControl.Tf,
                                        Id=Id)
        else:
            tf_after = None

        # Kf
        if switch_command_line is not None:
            kf_before = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Kf,
                                         Id=Id)
        else:
            kf_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf)

        if switch_command_line is not None:
            kf_after = get_.get_cell_id(table=ExcControl.table,
                                        column=ExcControl.Kf,
                                        Id=Id)
        else:
            kf_after = None

        # Kf1
        if switch_command_line is not None:
            kf1_before = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.Kf1,
                                          Id=Id)
        else:
            kf1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf1)

        if switch_command_line is not None:
            kf1_after = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Kf1,
                                         Id=Id)
        else:
            kf1_after = None

        # TINT
        if switch_command_line is not None:
            tint_before = get_.get_cell_id(table=ExcControl.table,
                                           column=ExcControl.TINT,
                                           Id=Id)
        else:
            tint_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.TINT,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=TINT)

        if switch_command_line is not None:
            tint_after = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.TINT,
                                          Id=Id)
        else:
            tint_after = None
