# -*- coding: utf-8 -*-
from RastrWin3.AstraRastr import RASTR


class Selection:
    f""" Класс предназначени для работы с выделением строк таблице,
         а именно включение/отключение параметра (Переключатель) Отметка О "sel".
    """

    def __init__(self, rastr_win=RASTR):
        f"""
        :param rastr_win: COM - объект Rastr.Astra (win32com);\n
        """
        self.rastr_win = rastr_win

    def remove_all_selection(self, table: str = None) -> None:
        f""" Универсальный метод для удления всех отметок в таблице """
        pass

    def selection(self, switch_command_line=False):
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