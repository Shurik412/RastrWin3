# -*- coding: utf-8 -*-
from RastrWin.AstraRastr import RASTR
from RastrWin.variables.variable_parametrs import VariableDefRowId
from RastrWin.tables.tablesAttributes import ut_common_table, ut_common_attributes


class UtCommon(VariableDefRowId):
    """
    Класс выставляет параметров настройки ""
    """

    def __init__(self, rastr_win=RASTR, table=ut_common_table, switch_command_line=False):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in ut_common_attributes.keys():
            self.list_key.append(key)
        self.switch_command_line = switch_command_line
        VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table, switch_command_line=switch_command_line)

    def set(self,
            maxs=5,
            maxv=2,
            maxd=2,
            maxa=10,
            iter=100,
            tip=0,
            f_ots=0,
            add_d=0,
            ekstr=0,
            kfc=1.000,
            sum_kfc='',
            ds=0,
            it='',
            Status=0,
            KorrT=25,
            KorrPer='',
            KorrVib='',
            enable_contr=0,
            dis_v_contr=0,
            dis_p_contr=0,
            dis_i_contr=0,
            ss_calc=0,
            criterion=0,
            no_crit_d_ba=0,
            no_crit_d_coa=0,
            no_crit_d_ga=0,
            save_files_filter=0,
            save_files_path=0,
            stop_u_n=0,
            dyn_find_pred=0):

        VariableDefRowId.make_changes(self, column=self.list_key[0], row_id=0, value=float(maxs))
        VariableDefRowId.make_changes(self, column=self.list_key[1], row_id=0, value=float(maxv))
        VariableDefRowId.make_changes(self, column=self.list_key[2], row_id=0, value=float(maxd))
        VariableDefRowId.make_changes(self, column=self.list_key[3], row_id=0, value=float(maxa))
        VariableDefRowId.make_changes(self, column=self.list_key[4], row_id=0, value=float(iter))
        VariableDefRowId.make_changes(self, column=self.list_key[5], row_id=0, value=float(tip))
        VariableDefRowId.make_changes(self, column=self.list_key[6], row_id=0, value=float(f_ots))
        VariableDefRowId.make_changes(self, column=self.list_key[7], row_id=0, value=float(add_d))
        VariableDefRowId.make_changes(self, column=self.list_key[8], row_id=0, value=float(ekstr))
        VariableDefRowId.make_changes(self, column=self.list_key[9], row_id=0, value=float(kfc))
        VariableDefRowId.make_changes(self, column=self.list_key[10], row_id=0, value=float(sum_kfc))
        VariableDefRowId.make_changes(self, column=self.list_key[11], row_id=0, value=float(ds))
        VariableDefRowId.make_changes(self, column=self.list_key[12], row_id=0, value=float(it))
        VariableDefRowId.make_changes(self, column=self.list_key[13], row_id=0, value=float(Status))
        VariableDefRowId.make_changes(self, column=self.list_key[14], row_id=0, value=float(KorrT))
        VariableDefRowId.make_changes(self, column=self.list_key[15], row_id=0, value=float(KorrPer))
        VariableDefRowId.make_changes(self, column=self.list_key[16], row_id=0, value=float(KorrVib))
        VariableDefRowId.make_changes(self, column=self.list_key[17], row_id=0, value=float(enable_contr))
        VariableDefRowId.make_changes(self, column=self.list_key[18], row_id=0, value=float(dis_v_contr))
        VariableDefRowId.make_changes(self, column=self.list_key[19], row_id=0, value=float(dis_p_contr))
        VariableDefRowId.make_changes(self, column=self.list_key[20], row_id=0, value=float(dis_i_contr))
        VariableDefRowId.make_changes(self, column=self.list_key[21], row_id=0, value=float(ss_calc))
        VariableDefRowId.make_changes(self, column=self.list_key[21], row_id=0, value=float(criterion))
        VariableDefRowId.make_changes(self, column=self.list_key[22], row_id=0, value=float(no_crit_d_ba))
        VariableDefRowId.make_changes(self, column=self.list_key[23], row_id=0, value=float(no_crit_d_coa))
        VariableDefRowId.make_changes(self, column=self.list_key[24], row_id=0, value=float(no_crit_d_ga))
        VariableDefRowId.make_changes(self, column=self.list_key[25], row_id=0, value=float(save_files_filter))
        VariableDefRowId.make_changes(self, column=self.list_key[26], row_id=0, value=float(save_files_path))
        VariableDefRowId.make_changes(self, column=self.list_key[27], row_id=0, value=float(stop_u_n))
        VariableDefRowId.make_changes(self, column=self.list_key[28], row_id=0, value=float(dyn_find_pred))
