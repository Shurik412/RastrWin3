# -*- coding: utf-8 -*-

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.calculation.equivalent import Equivalent
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.settings.equivalence import set_com_ekviv
from RastrWinLib.tables.tables_attributes import node_table, vetv_table, vetv_attributes_list, node_attributes_list
from RastrWinLib.variables.group_correction import GroupCorr
from RastrWinLib.variables.removal_marked_objects import RemoveSelObjects
from RastrWinLib.variables.variable_parametrs import Variable


def equivalent_gen(viborka_gen):
    # ekv_obj = Equivalent(rastr_win=RASTR,
    #                      switch_command_line=False)
    sel_remove = RemoveSelObjects(rastr_win=RASTR)
    sel_remove.remove_sel_vetv()
    sel_remove.remove_sel_node()
    tables_node = RASTR.Tables(node_table)
    tables_vetv = RASTR.Tables(vetv_table)
    var_node_obj = Variable(rastr_win=RASTR,
                            switch_command_line=False)
    # set_com_ekviv(selekv=0,
    #               met_ekv=0,
    #               tip_ekv=0,
    #               ekvgen=0,
    #               tip_gen=1,
    #               kfc_x=0,
    #               pot_gen=0,
    #               kpn=0,
    #               tip_sxn=0,
    #               smart=0,
    #               zmax=1000,
    #               otm_n=0,
    #               switch_command_line=True)

    tables_node.SetSel(f'{viborka_gen}')
    row_viborki = tables_node.FindNextSel(-1)
    print(f'row_viborki = {row_viborki}')
    while row_viborki != (-1):
        ny_one = tables_node.Cols(node_attributes_list[3]).Z(row_viborki)
        print(f'ny_one = {ny_one}')
        tables_vetv.SetSel(f'"(ip.uhom<110 & iq=" & {ny_one} & ")|(iq.uhom<110 & ip=" & {ny_one} & ")"')
        row_vetv_in_ny_one = tables_vetv.FindNextSel(-1)
        print(f'row_vetv_in_ny_one = {row_vetv_in_ny_one}')

        while row_vetv_in_ny_one != (-1):
            ip_one = GettingParameter().get_cell(table=vetv_table,
                                                 column=vetv_attributes_list[3],
                                                 row_id=row_vetv_in_ny_one)

            iq_one = GettingParameter().get_cell(table=vetv_table,
                                                 column=vetv_attributes_list[4],
                                                 row_id=row_vetv_in_ny_one)

            if ip_one == ny_one:
                ny_two = iq_one
            else:
                ny_two = ip_one

            tables_node.SetSel(f'ny={ny_two}')
            row_node_in_ny_two = tables_node.FindNextSel(-1)

            if row_node_in_ny_two != (-1):
                var_node_obj.make_changes_row(table=node_table,
                                              column=node_attributes_list[0],
                                              row_id=row_node_in_ny_two,
                                              value=1)
            row_vetv_in_ny_one = tables_vetv.FindNextSel(row_vetv_in_ny_one)

        tables_node.SetSel(f'"{str(viborka_gen)}"')
        row_viborki = tables_node.FindNextSel(row_viborki)

    # set_com_ekviv(selekv=0,
    #               met_ekv=0,
    #               tip_ekv=0,
    #               ekvgen=0,
    #               tip_gen=1,
    #               kfc_x=0,
    #               pot_gen=0,
    #               kpn=0,
    #               tip_sxn=0,
    #               smart=0,
    #               zmax=1000,
    #               otm_n=0,
    #               switch_command_line=True)
    # ekv_obj.ekv()
    # tables_node.SetSel(f'uhom > 50')
    # tables_node.Cols('sel').Calc('0')
    #
    # ekv_obj.ekv()
    # tables_node.SetSel(f'uhom > 50')
    # tables_node.Cols('sel').Calc('0')
    #
    # ekv_obj.ekv()
    # tables_node.SetSel(f'uhom > 50')
    # tables_node.Cols('sel').Calc('0')
    #
    # ekv_obj.ekv()
    # tables_node.SetSel(f'uhom > 50')
    # tables_node.Cols('sel').Calc('0')
    #
    # ekv_obj.ekv()
    # tables_node.SetSel(f'uhom > 50')
    # tables_node.Cols('sel').Calc('0')
    #
    # ekv_obj.ekv()
    # tables_node.SetSel(f'uhom > 50')
    # tables_node.Cols('sel').Calc('0')
    #
    # ekv_obj.ekv()
    # tables_node.SetSel(f'uhom > 50')
    # tables_node.Cols('sel').Calc('0')


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
