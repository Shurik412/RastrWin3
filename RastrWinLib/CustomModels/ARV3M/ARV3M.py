# -*- coding: utf-8 -*-
#  ---------------- Модель ARV-3M ----------------
# Модель автоматического регулятора возбуждения типа ARV3M,
# реализованная в ПК RUSTab, состоит из макроблоков.
# Параметры модели AVR-3M_res.xmldev заносятся в таблицу «АРВ (ИД)».

import RastrWinLib.tables.Dynamic.ExcControl as ExcControl
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.log_tools.tools import separator_grid
from RastrWinLib.variables.variable_parametrs import Variable


def change_parameters(
        Id=None,
        row_id=None,
        Ku: float = parameter.Ku,
        K_Q: float = parameter.K_Q,
        Kif1: float = parameter.Kif1,
        T1if: float = parameter.T1if,
        Ku1: float = parameter.Ku1,
        T1u1: float = parameter.T1u1,
        K_P: float = parameter.K_P,
        K_Ia: float = parameter.K_Ia,
        Tf: float = parameter.Tf,
        Kf: float = parameter.Kf,
        Kf1: float = parameter.Kf1,
        TINT: float = parameter.TINT,
        rastr_win=RASTR,
        switch_command_line: bool = False
):
    """
    Функция change_parameters -
    :param switch_command_line:
    :param rastr_win: COM - объект Rastr.Astra (win32com);
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
    variable_ = Variable(rastr_win=rastr_win)
    get_ = GettingParameter(rastr_win=rastr_win)

    if Id is not None and row_id is not None:
        # Ku
        ku_before = get_.get_cell(table=ExcControl.table,
                                  column=ExcControl.Ku,
                                  row_id=row_id)
        variable_.make_changes_row(table=ExcControl.table,
                                   column=ExcControl.Ku,
                                   row_id=row_id,
                                   value=Ku)
        ku_after = get_.get_cell(table=ExcControl.table,
                                 column=ExcControl.Ku,
                                 key=f'{ExcControl.Id}={Id}')
        # K_Q
        k_q_before = get_.get_cell(table=ExcControl.table,
                                   column=ExcControl.K_Q,
                                   row_id=row_id)
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_Q,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_Q)
        k_q_after = get_.get_cell(table=ExcControl.table,
                                  column=ExcControl.K_Q,
                                  row_id=row_id)
        # Kif1
        kif1_before = get_.get_cell(table=ExcControl.table,
                                    column=ExcControl.Kif1,
                                    row_id=row_id)
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kif1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kif1)
        kif1_after = get_.get_cell(table=ExcControl.table,
                                   column=ExcControl.Kif1,
                                   row_id=row_id)
        # T1if
        t1if_before = get_.get_cell(table=ExcControl.table,
                                    column=ExcControl.T1if,
                                    row_id=row_id)
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.T1if,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=T1if)
        t1if_after = get_.get_cell(table=ExcControl.table,
                                   column=ExcControl.T1if,
                                   row_id=row_id)
        # Ku1
        ku1_before = get_.get_cell(table=ExcControl.table,
                                   column=ExcControl.Ku1,
                                   row_id=row_id)
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Ku1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Ku1)
        ku1_after = get_.get_cell(table=ExcControl.table,
                                  column=ExcControl.Ku1,
                                  row_id=row_id)
        # T1u1
        t1u1_before = get_.get_cell(table=ExcControl.table,
                                    column=ExcControl.T1u1,
                                    row_id=row_id)
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.T1u1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=T1u1)
        t1u1_after = get_.get_cell(table=ExcControl.table,
                                   column=ExcControl.T1u1,
                                   row_id=row_id)
        # K_P
        kp_before = get_.get_cell(table=ExcControl.table,
                                  column=ExcControl.K_P,
                                  row_id=row_id)
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_P,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_P)
        kp_after = get_.get_cell(table=ExcControl.table,
                                 column=ExcControl.K_P,
                                 row_id=row_id)
        # K_Ia
        k_ia_before = get_.get_cell(table=ExcControl.table,
                                    column=ExcControl.K_Ia,
                                    row_id=row_id)
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_Ia,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_Ia)
        k_ia_after = get_.get_cell(table=ExcControl.table,
                                   column=ExcControl.K_Ia,
                                   row_id=row_id)
        # Tf
        tf_before = get_.get_cell(table=ExcControl.table,
                                  column=ExcControl.Tf,
                                  row_id=row_id)
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Tf,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Tf)
        tf_after = get_.get_cell(table=ExcControl.table,
                                 column=ExcControl.Tf,
                                 row_id=row_id)
        # Kf
        kf_before = get_.get_cell(table=ExcControl.table,
                                  column=ExcControl.Kf,
                                  row_id=row_id)
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf)
        kf_after = get_.get_cell(table=ExcControl.table,
                                 column=ExcControl.Kf,
                                 row_id=row_id)
        # Kf1
        kf1_before = get_.get_cell(table=ExcControl.table,
                                   column=ExcControl.Kf1,
                                   row_id=row_id)
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf1)
        kf1_after = get_.get_cell(table=ExcControl.table,
                                  column=ExcControl.Kf1,
                                  row_id=row_id)
        # TINT
        tint_before = get_.get_cell(table=ExcControl.table,
                                    column=ExcControl.TINT,
                                    row_id=row_id)
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.TINT,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=TINT)
        tint_after = get_.get_cell(table=ExcControl.table,
                                   column=ExcControl.TINT,
                                   row_id=row_id)

        if switch_command_line is not False:
            print(
                f'{separator_grid}\n'
                f'Таблица: "{ExcControl.table}" - {ExcControl.table_name}:\n'
                f'- Id: Номер возбудителя: {Id}\n'
                f'- Ku: Коэффициент усиления пропорционального канала регулятора напряжения: до {ku_before}; после {ku_after};\n'
                f'- K_Q: Коэффициент усиления канала по производной тока ротора: до {k_q_before}; после {k_q_after};\n'
                f'- Kif1: Коэффициент усиления канала по производной тока ротора: до {kif1_before}; после {kif1_after};\n'
                f'- T1if: Постоянная времени дифференцирующего звена в канале по производной тока ротора: до {t1if_before}; после {t1if_after};\n'
                f'- Ku1: Коэффициент усиления канала по производной напряжения: до {ku1_before}; после {ku1_after};\n'
                f'- T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения: до {t1u1_before}; после {t1u1_after};\n'
                f'- K_P: Коэффициент усиления выходного сигнала ОМВ: до {kp_before}; после {kp_after};\n'
                f'- K_Ia: Уставка ограничителя максимального тока ротора: до {k_ia_before}; после {k_ia_after};\n'
                f'- Tf: Постоянная времени дифференцирующего звена в канале по частоте: до {tf_before}; после {tf_after};\n'
                f'- Kf: Коэффициент усиления в канале по частоте: до {kf_before}; после {kf_after};\n'
                f'- Kf1: Коэффициент усиления в канале по производной частоты: до {kf1_before}; после {kf1_after};\n'
                f'- TINT: Постоянная времени интегратора: до {tint_before}; после {tint_after};\n'
                f'{separator_grid}\n'
            )

    if row_id is not None and row_id is not None:
        # Ku
        ku_before = get_.get_cell(table=ExcControl.table,
                                  column=ExcControl.Ku,
                                  key=f'{ExcControl.Id}={Id}')

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Ku,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Ku)

        ku_after = get_.get_param(table=ExcControl.table,
                                  column=ExcControl.Ku,
                                  key=f'{ExcControl.Id}={Id}')
        # K_Q
        k_q_before = get_.get_param(table=ExcControl.table,
                                    column=ExcControl.K_Q,
                                    key=f'{ExcControl.Id}={Id}')
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_Q,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_Q)
        k_q_after = get_.get_param(table=ExcControl.table,
                                   column=ExcControl.K_Q,
                                   key=f'{ExcControl.Id}={Id}')
        # Kif1
        kif1_before = get_.get_param(table=ExcControl.table,
                                     column=ExcControl.Kif1,
                                     key=f'{ExcControl.Id}={Id}')
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kif1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kif1)
        kif1_after = get_.get_param(table=ExcControl.table,
                                    column=ExcControl.Kif1,
                                    key=f'{ExcControl.Id}={Id}')
        # T1if
        t1if_before = get_.get_param(table=ExcControl.table,
                                     column=ExcControl.T1if,
                                     key=f'{ExcControl.Id}={Id}')
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.T1if,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=T1if)
        t1if_after = get_.get_param(table=ExcControl.table,
                                    column=ExcControl.T1if,
                                    key=f'{ExcControl.Id}={Id}')
        # Ku1
        ku1_before = get_.get_param(table=ExcControl.table,
                                    column=ExcControl.Ku1,
                                    key=f'{ExcControl.Id}={Id}')
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Ku1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Ku1)
        ku1_after = get_.get_param(table=ExcControl.table,
                                   column=ExcControl.Ku1,
                                   key=f'{ExcControl.Id}={Id}')
        # T1u1
        t1u1_before = get_.get_param(table=ExcControl.table,
                                     column=ExcControl.T1u1,
                                     key=f'{ExcControl.Id}={Id}')
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.T1u1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=T1u1)
        t1u1_after = get_.get_param(table=ExcControl.table,
                                    column=ExcControl.T1u1,
                                    key=f'{ExcControl.Id}={Id}')
        # K_P
        kp_before = get_.get_param(table=ExcControl.table,
                                   column=ExcControl.K_P,
                                   key=f'{ExcControl.Id}={Id}')
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_P,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_P)
        kp_after = get_.get_param(table=ExcControl.table,
                                  column=ExcControl.K_P,
                                  key=f'{ExcControl.Id}={Id}')
        # K_Ia
        k_ia_before = get_.get_param(table=ExcControl.table,
                                     column=ExcControl.K_Ia,
                                     key=f'{ExcControl.Id}={Id}')
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_Ia,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_Ia)
        k_ia_after = get_.get_param(table=ExcControl.table,
                                    column=ExcControl.K_Ia,
                                    key=f'{ExcControl.Id}={Id}')
        # Tf
        tf_before = get_.get_param(table=ExcControl.table,
                                   column=ExcControl.Tf,
                                   key=f'{ExcControl.Id}={Id}')
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Tf,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Tf)
        tf_after = get_.get_param(table=ExcControl.table,
                                  column=ExcControl.Tf,
                                  key=f'{ExcControl.Id}={Id}')
        # Kf
        kf_before = get_.get_param(table=ExcControl.table,
                                   column=ExcControl.Kf,
                                   key=f'{ExcControl.Id}={Id}')
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf)
        kf_after = get_.get_param(table=ExcControl.table,
                                  column=ExcControl.Kf,
                                  key=f'{ExcControl.Id}={Id}')
        # Kf1
        kf1_before = get_.get_param(table=ExcControl.table,
                                    column=ExcControl.Kf1,
                                    key=f'{ExcControl.Id}={Id}')
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf1)
        kf1_after = get_.get_param(table=ExcControl.table,
                                   column=ExcControl.Kf1,
                                   key=f'{ExcControl.Id}={Id}')
        # TINT
        tint_before = get_.get_param(table=ExcControl.table,
                                     column=ExcControl.TINT,
                                     key=f'{ExcControl.Id}={Id}')
        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.TINT,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=TINT)
        tint_after = get_.get_param(table=ExcControl.table,
                                    column=ExcControl.TINT,
                                    key=f'{ExcControl.Id}={Id}')

        if switch_command_line is not False:
            print(
                f'{separator_grid}\n'
                f'Таблица: "{ExcControl.table}" - {ExcControl.table_name}:\n'
                f'- row_id: порядковый номер в таблице (от 0 до [max.count]);: {row_id}\n'
                f'- Ku: Коэффициент усиления пропорционального канала регулятора напряжения: до {ku_before}; после {ku_after};\n'
                f'- K_Q: Коэффициент усиления канала по производной тока ротора: до {k_q_before}; после {k_q_after};\n'
                f'- Kif1: Коэффициент усиления канала по производной тока ротора: до {kif1_before}; после {kif1_after};\n'
                f'- T1if: Постоянная времени дифференцирующего звена в канале по производной тока ротора: до {t1if_before}; после {t1if_after};\n'
                f'- Ku1: Коэффициент усиления канала по производной напряжения: до {ku1_before}; после {ku1_after};\n'
                f'- T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения: до {t1u1_before}; после {t1u1_after};\n'
                f'- K_P: Коэффициент усиления выходного сигнала ОМВ: до {kp_before}; после {kp_after};\n'
                f'- K_Ia: Уставка ограничителя максимального тока ротора: до {k_ia_before}; после {k_ia_after};\n'
                f'- Tf: Постоянная времени дифференцирующего звена в канале по частоте: до {tf_before}; после {tf_after};\n'
                f'- Kf: Коэффициент усиления в канале по частоте: до {kf_before}; после {kf_after};\n'
                f'- Kf1: Коэффициент усиления в канале по производной частоты: до {kf1_before}; после {kf1_after};\n'
                f'- TINT: Постоянная времени интегратора: до {tint_before}; после {tint_after};\n'
                f'{separator_grid}\n'
            )
