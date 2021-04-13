# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.tables_attributes import ut_common_table, ut_common_attributes
from RastrWinLib.variables.variable_parametrs import VariableDefRowId


def ut_common(
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
        dyn_find_pred=0,
        switch_command_line=False,
):
    list_key = []
    for key in ut_common_attributes.keys():
        list_key.append(key)

    variable_def_rowid = VariableDefRowId(rastr_win=RASTR, table=ut_common_table,
                                          switch_command_line=switch_command_line)

    variable_def_rowid.make_changes(column=list_key[0], row_id=0, value=float(maxs))
    variable_def_rowid.make_changes(column=list_key[1], row_id=0, value=float(maxv))
    variable_def_rowid.make_changes(column=list_key[2], row_id=0, value=float(maxd))
    variable_def_rowid.make_changes(column=list_key[3], row_id=0, value=float(maxa))
    variable_def_rowid.make_changes(column=list_key[4], row_id=0, value=float(iter))
    variable_def_rowid.make_changes(column=list_key[5], row_id=0, value=float(tip))
    variable_def_rowid.make_changes(column=list_key[6], row_id=0, value=float(f_ots))
    variable_def_rowid.make_changes(column=list_key[7], row_id=0, value=float(add_d))
    variable_def_rowid.make_changes(column=list_key[8], row_id=0, value=float(ekstr))
    variable_def_rowid.make_changes(column=list_key[9], row_id=0, value=float(kfc))
    variable_def_rowid.make_changes(column=list_key[10], row_id=0, value=float(sum_kfc))
    variable_def_rowid.make_changes(column=list_key[11], row_id=0, value=float(ds))
    variable_def_rowid.make_changes(column=list_key[12], row_id=0, value=float(it))
    variable_def_rowid.make_changes(column=list_key[13], row_id=0, value=float(Status))
    variable_def_rowid.make_changes(column=list_key[14], row_id=0, value=float(KorrT))
    variable_def_rowid.make_changes(column=list_key[15], row_id=0, value=float(KorrPer))
    variable_def_rowid.make_changes(column=list_key[16], row_id=0, value=float(KorrVib))
    variable_def_rowid.make_changes(column=list_key[17], row_id=0, value=float(enable_contr))
    variable_def_rowid.make_changes(column=list_key[18], row_id=0, value=float(dis_v_contr))
    variable_def_rowid.make_changes(column=list_key[19], row_id=0, value=float(dis_p_contr))
    variable_def_rowid.make_changes(column=list_key[20], row_id=0, value=float(dis_i_contr))
    variable_def_rowid.make_changes(column=list_key[21], row_id=0, value=float(ss_calc))
    variable_def_rowid.make_changes(column=list_key[21], row_id=0, value=float(criterion))
    variable_def_rowid.make_changes(column=list_key[22], row_id=0, value=float(no_crit_d_ba))
    variable_def_rowid.make_changes(column=list_key[23], row_id=0, value=float(no_crit_d_coa))
    variable_def_rowid.make_changes(column=list_key[24], row_id=0, value=float(no_crit_d_ga))
    variable_def_rowid.make_changes(column=list_key[25], row_id=0, value=float(save_files_filter))
    variable_def_rowid.make_changes(column=list_key[26], row_id=0, value=float(save_files_path))
    variable_def_rowid.make_changes(column=list_key[27], row_id=0, value=float(stop_u_n))
    variable_def_rowid.make_changes(column=list_key[28], row_id=0, value=float(dyn_find_pred))

    if switch_command_line is not False:
        return print(
            'Внесены изменения в настройки "Общие данные для утяжеления" (таблица "Утяжеление": ut_common)')
    else:
        return True


class UtCommon(VariableDefRowId):
    """
    Класс выставляет параметров настройки "Общие данные для утяжеления"
    """

    def __init__(self, rastr_win=RASTR, table=ut_common_table, switch_command_line=False):
        self.rastr_win = rastr_win
        self.list_key = []
        for key in ut_common_attributes.keys():
            self.list_key.append(key)
        self.switch_command_line = switch_command_line
        self.variable_def_rowid = VariableDefRowId.__init__(self, rastr_win=rastr_win, table=table,
                                                            switch_command_line=switch_command_line)

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

        self.variable_def_rowid.make_changes(column=self.list_key[0], row_id=0, value=float(maxs))
        self.variable_def_rowid.make_changes(column=self.list_key[1], row_id=0, value=float(maxv))
        self.variable_def_rowid.make_changes(column=self.list_key[2], row_id=0, value=float(maxd))
        self.variable_def_rowid.make_changes(column=self.list_key[3], row_id=0, value=float(maxa))
        self.variable_def_rowid.make_changes(column=self.list_key[4], row_id=0, value=float(iter))
        self.variable_def_rowid.make_changes(column=self.list_key[5], row_id=0, value=float(tip))
        self.variable_def_rowid.make_changes(column=self.list_key[6], row_id=0, value=float(f_ots))
        self.variable_def_rowid.make_changes(column=self.list_key[7], row_id=0, value=float(add_d))
        self.variable_def_rowid.make_changes(column=self.list_key[8], row_id=0, value=float(ekstr))
        self.variable_def_rowid.make_changes(column=self.list_key[9], row_id=0, value=float(kfc))
        self.variable_def_rowid.make_changes(column=self.list_key[10], row_id=0, value=float(sum_kfc))
        self.variable_def_rowid.make_changes(column=self.list_key[11], row_id=0, value=float(ds))
        self.variable_def_rowid.make_changes(column=self.list_key[12], row_id=0, value=float(it))
        self.variable_def_rowid.make_changes(column=self.list_key[13], row_id=0, value=float(Status))
        self.variable_def_rowid.make_changes(column=self.list_key[14], row_id=0, value=float(KorrT))
        self.variable_def_rowid.make_changes(column=self.list_key[15], row_id=0, value=float(KorrPer))
        self.variable_def_rowid.make_changes(column=self.list_key[16], row_id=0, value=float(KorrVib))
        self.variable_def_rowid.make_changes(column=self.list_key[17], row_id=0, value=float(enable_contr))
        self.variable_def_rowid.make_changes(column=self.list_key[18], row_id=0, value=float(dis_v_contr))
        self.variable_def_rowid.make_changes(column=self.list_key[19], row_id=0, value=float(dis_p_contr))
        self.variable_def_rowid.make_changes(column=self.list_key[20], row_id=0, value=float(dis_i_contr))
        self.variable_def_rowid.make_changes(column=self.list_key[21], row_id=0, value=float(ss_calc))
        self.variable_def_rowid.make_changes(column=self.list_key[21], row_id=0, value=float(criterion))
        self.variable_def_rowid.make_changes(column=self.list_key[22], row_id=0, value=float(no_crit_d_ba))
        self.variable_def_rowid.make_changes(column=self.list_key[23], row_id=0, value=float(no_crit_d_coa))
        self.variable_def_rowid.make_changes(column=self.list_key[24], row_id=0, value=float(no_crit_d_ga))
        self.variable_def_rowid.make_changes(column=self.list_key[25], row_id=0, value=float(save_files_filter))
        self.variable_def_rowid.make_changes(column=self.list_key[26], row_id=0, value=float(save_files_path))
        self.variable_def_rowid.make_changes(column=self.list_key[27], row_id=0, value=float(stop_u_n))
        self.variable_def_rowid.make_changes(column=self.list_key[28], row_id=0, value=float(dyn_find_pred))

        if self.switch_command_line is not False:
            return print(
                'Внесены изменения в настройки "Общие данные для утяжеления" (таблица "Утяжеление": ut_common)')
        else:
            return True
