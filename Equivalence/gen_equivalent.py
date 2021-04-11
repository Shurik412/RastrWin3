# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.settings.equivalence import SetEkviv
from RastrWinLib.tables.tables_attributes import node_table, vetv_table
from RastrWinLib.variables.variable_parametrs import FindNextSel
from RastrWinLib.getting.get import GettingParameterInstance


def equivalent_gen(viborka_gen):
    SetEkviv(rastr_win=RASTR).set(selekv=0,
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
                                          switch_command_line=True).get(column='ny')
        row_vetv_in_ny_one = FindNextSel(rastr_win=RASTR,
                                         table=vetv_table).row(
            key=f'(ip.uhom<110 & iq=" & {ny_one} & ")|(iq.uhom<110 & ip=" & {ny_one} & ")')








class ViborkaEquivalent(SetEkviv,
                        FindNextSel):

    def __init__(self, rastr_win=RASTR):
        self.rastr_win = rastr_win
        self.set_ekviv = SetEkviv.__init__(self,
                                           rastr_win=rastr_win)
        self.table_name = node_table
        self.find_next_sel = FindNextSel.__init__(self,
                                                  rastr_win=RASTR,
                                                  table=self.table_name)

    def getting(self, viborka):
        self.set_ekviv.set(selekv=0,
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

        k = self.find_next_sel.row(key=str(viborka))
        return k
