# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Tables.Node.node import Node
from RastrWinLib.Tables.Vetv.vetv import Vetv
from RastrWinLib.Variables.group_correction import GroupCorr


def selection(switch_command_line=False):
    group_corr_node_sel = GroupCorr(rastr_win=RASTR,
                                    switch_command_line=False,
                                    table=Node.table,
                                    column=Node.sel)

    group_corr_vetv_sel = GroupCorr(rastr_win=RASTR,
                                    switch_command_line=False,
                                    table=Vetv.table,
                                    column=Vetv.sel)

    group_corr_node_sel.calc(key="", formula="0")
    if switch_command_line is not False:
        print(' - Сняты отметки с Узлов')

    group_corr_vetv_sel.calc(key="", formula="0")
    if switch_command_line is not False:
        print(' - Сняты отметки с Ветви')


if __name__ == '__main__':
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.save import save_file
    from RastrWinLib.loading.shablon import Shabl
    from RastrWinLib.AstraRastr import RASTR

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\БРМ 2021 версия 4\БРМ лето 2020 минимум_4.rg2',
              shabl=Shabl.shablon_file_regime)

    selection(switch_command_line=False)

    save_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\БРМ 2021 версия 4\БРМ лето 2020 минимум_4_NEW.rg2',
              shabl=Shabl.shablon_file_regime)
