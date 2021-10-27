# -*- coding: utf-8 -*-

import RastrWinLib.Tables.Vetv.vetv as vetv
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.calculation.equivalent import Equivalent
from RastrWinLib.operation.get import GettingParameter
from RastrWinLib.Settings.equivalence import set_com_ekviv
from RastrWinLib.Tables.tables_attributes import node_table, vetv_table, node_attributes_list
from RastrWinLib.operation.GroupCorrection import GroupCorr
from RastrWinLib.operation.removal_marked_objects import RemoveSelObjects
from RastrWinLib.operation.Variable import Variable


def equivalent_gen(viborka_gen):
    ekv_obj = Equivalent(rastr_win=RASTR,
                         switch_command_line=False)
    sel_remove = RemoveSelObjects(rastr_win=RASTR)
    sel_remove.remove_sel_vetv()
    sel_remove.remove_sel_node()

    list_na = [102, 103, 104, 105, 106, 107, 108, 109]
    get_ = GettingParameter()
    variable_ = Variable()

    for i in range(0, 26558):
        na_vetv = get_.get_cell(table=vetv_table,
                                column=vetv.na,
                                row_id=i)

        v_ip = get_.get_cell(table=vetv_table,
                             column=vetv.v_ip,
                             row_id=i)
        v_iq = get_.get_cell(table=vetv_table,
                             column=vetv.v_iq,
                             row_id=i)

        for na in list_na:
            if na == na_vetv:
                if 160 > v_iq and 160 > v_ip:
                    variable_.make_changes_row(table=vetv_table,
                                               column=vetv.sel,
                                               row_id=i,
                                               value=1)


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
              column=node_attributes_list[0],
              switch_command_line=False).calc(key=viborka_rayon,
                                              formula=1)

    Equivalent(rastr_win=RASTR,
               switch_command_line=False).ekv()
