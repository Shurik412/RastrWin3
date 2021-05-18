from openpyxl import load_workbook

from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.save import save_file
from RastrWinLib.loading.shablon import Shabl
from RastrWinLib.tables.Scenario.DFWAutoActionScn import DFWAutoActionScn
from RastrWinLib.tables.Scenario.DFWAutoLogicScn import DFWAutoLogicScn
from RastrWinLib.variables.variable_parametrs import Variable


class CreateActionsSCN(Variable):
    def __init__(self, rastr_win, dir_name_file_excel, name_list_excel, switch_command_line=False):

        self.rastr_win = rastr_win
        load_file(rastr_win=rastr_win, shabl=Shabl.shablon_file_scenario)
        excel_wb = load_workbook(filename=dir_name_file_excel, data_only=True)
        self.ws = excel_wb[name_list_excel]

        Variable.__init__(self, rastr_win=self.rastr_win,
                          switch_command_line=switch_command_line)

    def create(self, table=DFWAutoActionScn.table, start=14, finish=32):
        table_ = self.rastr_win.Tables(table)
        table_.DelRows()
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
        table_.DelRows()
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

    rastr = win32com.client.Dispatch('Astra.Rastr')
    load_file(rastr_win=rastr, shabl=shablon_file_scenario)
    filename = 'L:\\SER\\Охрименко\\03. RastrWinLib\\16\\ВЛ 500 кВ Рязанская ГРЭС – Липецкая Восточная.xlsx'
    scn = CreateActionsSCN(rastr_win=rastr, name_list_excel='Сценарий', dir_name_file_excel=filename, )
    scn.create()
    scn.create_log()
    scn.save_scn(dir_file_name_save_scn='L:\\SER\\Охрименко\\03. RastrWinLib\\16\\scn1.scn', switch_command_line=True)
