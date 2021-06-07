# -*- coding: utf-8 -*-
from openpyxl import load_workbook

from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.save import save_file
from RastrWinLib.loading.shablon import Shabl
from RastrWinLib.tables.Scenario.DFWAutoActionScn import DFWAutoActionScn
from RastrWinLib.tables.Scenario.DFWAutoLogicScn import DFWAutoLogicScn
from RastrWinLib.variables.variable_parametrs import Variable




def create_file_scn(WorkSheet,):
    # 1 строка
    WorkSheet['A14'] = '1'
    WorkSheet['B14'] = '1'
    WorkSheet['C14'] = 'Узел Rш'
    WorkSheet['D14'] = WorkSheet['N3'].value
    WorkSheet['E14'] = WorkSheet['N25'].value
    WorkSheet['F14'] = ''
    WorkSheet['G14'] = ''
    WorkSheet['H14'] = f'ny={WorkSheet["T25"].value}'

    # 2 строка
    WorkSheet['A15'] = '2'
    WorkSheet['B15'] = '1'
    WorkSheet['C15'] = 'Узел Xш'
    WorkSheet['D15'] = WorkSheet['N3'].value
    WorkSheet['E15'] = WorkSheet['N26'].value
    WorkSheet['F15'] = ''
    WorkSheet['G15'] = ''
    WorkSheet['H15'] = f'ny={WorkSheet["T25"].value}'

    # 3 строка
    WorkSheet['A16'] = '3'
    WorkSheet['B16'] = '2'
    WorkSheet['C16'] = 'Узел Rш'
    WorkSheet['D16'] = WorkSheet['N4'].value
    WorkSheet['E16'] = WorkSheet['N35'].value
    WorkSheet['F16'] = ''
    WorkSheet['G16'] = ''
    WorkSheet['H16'] = f'ny={WorkSheet["AE25"].value}'

    # 4 строка
    WorkSheet['A17'] = '4'
    WorkSheet['B17'] = '2'
    WorkSheet['C17'] = 'Узел Xш'
    WorkSheet['D17'] = WorkSheet['N4'].value
    WorkSheet['E17'] = WorkSheet['N36'].value
    WorkSheet['F17'] = ''
    WorkSheet['G17'] = ''
    WorkSheet['H17'] = f'ny={WorkSheet["AE25"].value}'

    # 5 строка
    WorkSheet['A18'] = '5'
    WorkSheet['B18'] = '2'
    WorkSheet['C18'] = 'Объект'
    WorkSheet['D18'] = WorkSheet['N2'].value
    WorkSheet['E18'] = WorkSheet['N32'].value
    WorkSheet['F18'] = 'vetv'
    WorkSheet['G18'] = 'r'
    WorkSheet['H18'] = f'ip={WorkSheet["X25"].value},iq={WorkSheet["Z25"].value},np={WorkSheet["AB25"].value}'

    # 6 строка
    WorkSheet['A19'] = '6'
    WorkSheet['B19'] = '2'
    WorkSheet['C19'] = 'Объект'
    WorkSheet['D19'] = WorkSheet['N2'].value
    WorkSheet['E19'] = WorkSheet['N33'].value
    WorkSheet['F19'] = 'vetv'
    WorkSheet['G19'] = 'x'
    WorkSheet['H19'] = f'ip={WorkSheet["X25"].value},iq={WorkSheet["Z25"].value},np={WorkSheet["AB25"].value}'

    # 7 строка
    WorkSheet['A20'] = '7'
    WorkSheet['B20'] = '2'
    WorkSheet['C20'] = 'Объект'
    WorkSheet['D20'] = WorkSheet['N2'].value
    WorkSheet['E20'] = '0'
    WorkSheet['F20'] = 'vetv'
    WorkSheet['G20'] = 'b'
    WorkSheet['H20'] = f'ip={WorkSheet["X25"].value},iq={WorkSheet["Z25"].value},np={WorkSheet["AB25"].value}'

    # 8 строка
    WorkSheet['A21'] = '8'
    WorkSheet['B21'] = '2'
    WorkSheet['C21'] = 'Узел Rш'
    WorkSheet['D21'] = WorkSheet['N3'].value
    WorkSheet['E21'] = WorkSheet['N29'].value
    WorkSheet['F21'] = ''
    WorkSheet['G21'] = ''
    WorkSheet['H21'] = f'ny={WorkSheet["T25"].value}'

    # 9 строка
    WorkSheet['A22'] = '9'
    WorkSheet['B22'] = '2'
    WorkSheet['C22'] = 'Узел Xш'
    WorkSheet['D22'] = WorkSheet['N3'].value
    WorkSheet['E22'] = WorkSheet['N30'].value
    WorkSheet['F22'] = ''
    WorkSheet['G22'] = ''
    WorkSheet['H22'] = f'ny={WorkSheet["T25"].value}'

    # 10 строка
    WorkSheet['A23'] = '10'
    WorkSheet['B23'] = '3'
    WorkSheet['C23'] = 'Узел Xш'
    WorkSheet['D23'] = WorkSheet['N3'].value
    WorkSheet['E23'] = WorkSheet['N30'].value
    WorkSheet['F23'] = ''
    WorkSheet['G23'] = ''
    WorkSheet['H23'] = f'ny={WorkSheet["T25"].value}'


class CreateActionsSCN(Variable):
    def __init__(self, rastr_win, dir_name_file_excel, name_list_excel, switch_command_line=False):

        self.rastr_win = rastr_win
        load_file(rastr_win=rastr_win, shabl=Shabl.shablon_file_scenario)
        excel_wb = load_workbook(filename=dir_name_file_excel, data_only=True)
        self.ws = excel_wb[name_list_excel]

        Variable.__init__(self, rastr_win=self.rastr_win,
                          switch_command_line=switch_command_line)

    def create(self, table=DFWAutoActionScn.table, start=14, finish=31):
        table_ = self.rastr_win.Tables(table)
        for index in range(start, finish):
            table_.AddRow()
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.State,
                                      row_id=index - start,
                                      value=0)  # Cocт
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.Id,
                                      row_id=index - start,
                                      value=self.ws[f'A{index}'].value)  # N
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.ParentId,
                                      row_id=index - start,
                                      value=self.ws[f'B{index}'].value)  # N группы
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.Type,
                                      row_id=index - start,
                                      value=self.ws[f'C{index}'].value)  # Тип
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.Name,
                                      row_id=index - start,
                                      value=self.ws[f'D{index}'].value)  # Название
            Variable.make_changes_row(self, table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.Formula,
                                      row_id=index - start,
                                      value=self.ws[f'E{index}'].value)  # Формула
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.ObjectClass,
                                      row_id=index - start,
                                      value=self.ws[f'F{index}'].value)  # Тип объекта
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.ObjectProp,
                                      row_id=index - start,
                                      value=self.ws[f'G{index}'].value)  # Свойство объекта
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.ObjectKey,
                                      row_id=index - start,
                                      value=self.ws[f'H{index}'].value)  # Ключ объекта
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.OutputMode,
                                      row_id=index - start,
                                      value=0)  # Режим
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.RunsCount,
                                      row_id=index - start,
                                      value=1)  # N сраб
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.TimeStart,
                                      row_id=index - start,
                                      value=0)  # Время начала
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.DT,
                                      row_id=index - start,
                                      value=0)  # Длительность
            Variable.make_changes_row(self,
                                      table=DFWAutoActionScn.table,
                                      column=DFWAutoActionScn.Tag,
                                      row_id=index - start,
                                      value=0)  # Тэг упрощенного сценария

    def create_log(self, start=4, finish=8, switch_command_line=False):

        Variable.__init__(self,
                          rastr_win=self.rastr_win,
                          switch_command_line=switch_command_line)

        table_ = self.rastr_win.Tables(DFWAutoLogicScn.table)
        for index in range(start, finish):
            table_.AddRow()
            Variable.make_changes_row(self,
                                      table=DFWAutoLogicScn.table,
                                      column=DFWAutoLogicScn.Id,
                                      row_id=index - start,
                                      value=self.ws[f'A{index}'].value)  # Id

            Variable.make_changes_row(self,
                                      table=DFWAutoLogicScn.table,
                                      column=DFWAutoLogicScn.Name,
                                      row_id=index - start,
                                      value=self.ws[f'B{index}'].value)  # Название
            Variable.make_changes_row(self,
                                      table=DFWAutoLogicScn.table,
                                      column=DFWAutoLogicScn.ParentId,
                                      row_id=index - start,
                                      value=self.ws[f'C{index}'].value)  # Номер модуля
            Variable.make_changes_row(self,
                                      table=DFWAutoLogicScn.table,
                                      column=DFWAutoLogicScn.Type,
                                      row_id=index - start,
                                      value=self.ws[f'D{index}'].value)  # Тип логики
            Variable.make_changes_row(self,
                                      table=DFWAutoLogicScn.table,
                                      column=DFWAutoLogicScn.Formula,
                                      row_id=index - start,
                                      value=self.ws[f'E{index}'].value)  # Формула
            Variable.make_changes_row(self,
                                      table=DFWAutoLogicScn.table,
                                      column=DFWAutoLogicScn.Actions,
                                      row_id=index - start,
                                      value=self.ws[f'F{index}'].value)  # Действия
            Variable.make_changes_row(self,
                                      table=DFWAutoLogicScn.table,
                                      column=DFWAutoLogicScn.Delay,
                                      row_id=index - start,
                                      value=self.ws[f'G{index}'].value)  # Выдержка времени
            Variable.make_changes_row(self,
                                      table=DFWAutoLogicScn.table,
                                      column=DFWAutoLogicScn.UnitStarters,
                                      row_id=index - start,
                                      value=self.ws[f'H{index}'].value)  # ПО мод
            Variable.make_changes_row(self,
                                      table=DFWAutoLogicScn.table,
                                      column=DFWAutoLogicScn.UnitConstants,
                                      row_id=index - start,
                                      value=self.ws[f'I{index}'].value)  # Const мод
            Variable.make_changes_row(self,
                                      table=DFWAutoLogicScn.table,
                                      column=DFWAutoLogicScn.UnitActions,
                                      row_id=index - start,
                                      value=self.ws[f'J{index}'].value)  # Дейст мод
            Variable.make_changes_row(self,
                                      table=DFWAutoLogicScn.table,
                                      column=DFWAutoLogicScn.OutputMode,
                                      row_id=index - start,
                                      value=self.ws[f'H{index}'].value)  # Режим выхода

    def save_scn(self, dir_file_name_save_scn=None, dir_file=None, name_save_scn=None, switch_command_line=False):

        if dir_file_name_save_scn is not None:
            save_file(rastr_win=self.rastr_win,
                      file_path=dir_file_name_save_scn,
                      shabl=Shabl.shablon_file_scenario,
                      switch_command_line=switch_command_line)

        elif (dir_file is not None) and (name_save_scn is not None):
            save_file(rastr_win=self.rastr_win,
                      file_path=f'{dir}/{name_save_scn}',
                      shabl=Shabl.shablon_file_scenario,
                      switch_command_line=switch_command_line)



















if __name__ == '__main__':
    import win32com.client

    # from openpyxl import load_workbook
    # from RastrWinLib.loading.shablons_dir import shablon_file_scenario
    # from RastrWinLib.loading.save_file_rastrwin import save_file
    # from RastrWinLib.loading.load_file_rastrwin import load_file
    from RastrWinLib.loading.shablon import Shabl

    rastr = win32com.client.Dispatch('Astra.Rastr')
    load_file(rastr_win=rastr, shabl=Shabl.shablon_file_scenario)
    filename = r'L:\SER\Охрименко\03. RastrWin3\19\ВЛ 500 кВ Нововоронежская АЭС – Воронежская.xlsx'
    scn = CreateActionsSCN(rastr_win=rastr, name_list_excel='Сценарий', dir_name_file_excel=filename, )
    scn.create()
    scn.create_log()
    scn.save_scn(dir_file_name_save_scn=r'L:\SER\Охрименко\03. RastrWin3\19\scn1.scn', switch_command_line=True)
