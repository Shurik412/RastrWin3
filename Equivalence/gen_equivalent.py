# -*- coding: utf-8 -*-

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.calculation.equivalent import Equivalent
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.getting.get import GettingParameterInstance
from RastrWinLib.settings.equivalence import set_com_ekviv
from RastrWinLib.tables.tables_attributes import node_table, vetv_table
from RastrWinLib.variables.group_correction import GroupCorr
from RastrWinLib.variables.removal_marked_objects import RemoveSelObjects
from RastrWinLib.variables.variable_parametrs import FindNextSel, VariableDefRowId


def equivalent_gen(viborka_gen):
    sel_remove = RemoveSelObjects(rastr_win=RASTR)
    sel_remove.remove_sel_vetv()
    sel_remove.remove_sel_node()
    set_com_ekviv(selekv=0,
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
                  otm_n=0)
    row_viborki = FindNextSel(rastr_win=RASTR, table=node_table).row(key=viborka_gen)
    while row_viborki != (-1):
        ny_one = GettingParameterInstance(rastr_win=RASTR,
                                          table=node_table,
                                          key=row_viborki,
                                          switch_command_line=False).get(column='ny')
        tables = RASTR.Tables(str(vetv_table))
        tables.SetSel(f'(ip.uhom<110 & iq=" & {ny_one} & ")|(iq.uhom<110 & ip=" & {ny_one} & ")')
        row_vetv_in_ny_one = tables.FindNextSel(-1)
        while row_vetv_in_ny_one != (-1):
            ip_one = GettingParameter(rastr_win=RASTR, table=vetv_table, column='ip').get(row_id=row_vetv_in_ny_one)
            iq_one = GettingParameter(rastr_win=RASTR, table=vetv_table, column='iq').get(row_id=row_vetv_in_ny_one)
            if ip_one == ny_one:
                ny_two = iq_one
            else:
                ny_two = ip_one

            # row_vetv_in_ny_two = FindNextSel(rastr_win=RASTR, table=node_table).row(key=f'ny={ny_two}')
            tables = RASTR.Tables(str(node_table))
            tables.SetSel(f'ny={ny_two}')
            row_vetv_in_ny_two = tables.FindNextSel(-1)

            if row_vetv_in_ny_two != (-1):
                VariableDefRowId(rastr_win=RASTR,
                                 table=node_table,
                                 switch_command_line=False).make_changes(column='sel',
                                                                         row_id=row_vetv_in_ny_two,
                                                                         value=1)
            row_vetv_in_ny_one = FindNextSel(rastr_win=RASTR,
                                             table=vetv_table).row(key=row_vetv_in_ny_one)
        tables = RASTR.Tables(str(node_table))
        tables.SetSel(f'{str(viborka_gen)}')
        row_viborki = tables.FindNextSel(row_viborki)
    set_com_ekviv(selekv=0,
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
                  otm_n=0)


def equivalent_smart(viborka_rayon):
    sel_remove = RemoveSelObjects(rastr_win=RASTR)
    sel_remove.remove_sel_node()
    sel_remove.remove_sel_vetv()

    set_com_ekviv(selekv=0,
                  met_ekv=0,
                  tip_ekv=0,
                  ekvgen=0,
                  tip_gen=1,
                  kfc_x='',
                  pot_gen=0,
                  kpn='',
                  tip_sxn=0,
                  smart=1,
                  zmax=1000,
                  otm_n=0)

    GroupCorr(rastr_win=RASTR,
              table=node_table,
              column='sel',
              switch_command_line=False).calc(key=viborka_rayon,
                                              formula=1)

    Equivalent(rastr_win=RASTR, switch_command_line=False).ekv()
