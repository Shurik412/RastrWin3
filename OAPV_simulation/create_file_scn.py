from RastrWin.variables.variable_parametrs import VariableDefRowId
from RastrWin.loading.save import save_file
from RastrWin.loading.shablon import shablon_file_scenario
from RastrWin.loading.load import load_file
from openpyxl import load_workbook


class CreateActionsSCN(VariableDefRowId):
    def __init__(self, rastr_win, dir_name_file_excel, name_list_excel, switch_command_line=False):
        self.rastr_win = rastr_win
        load_file(rastr_win=rastr_win, shablon=shablon_file_scenario)
        excel_wb = load_workbook(filename=dir_name_file_excel, data_only=True)
        self.ws = excel_wb[name_list_excel]
        VariableDefRowId.__init__(self, rastr_win=self.rastr_win, table="DFWAutoActionScn",
                                  switch_command_line=switch_command_line)

    def create(self, start=14, finish=32):
        self.table.DelRows()
        for index in range(start, finish):
            self.table.AddRow()
            VariableDefRowId.make_changes(self, column='State', row_id=index - start, value=0)  # Cocт
            VariableDefRowId.make_changes(self, column='Id', row_id=index - start,
                                          value=self.ws[f'A{index}'].value)  # Id группы
            VariableDefRowId.make_changes(self, column='ParentId', row_id=index - start,
                                          value=self.ws[f'B{index}'].value)  # N группы
            VariableDefRowId.make_changes(self, column='Type', row_id=index - start,
                                          value=self.ws[f'C{index}'].value)  # Тип
            VariableDefRowId.make_changes(self, column='Name', row_id=index - start,
                                          value=self.ws[f'D{index}'].value)  # Название
            VariableDefRowId.make_changes(self, column='Formula', row_id=index - start,
                                          value=self.ws[f'E{index}'].value)  # Формула
            VariableDefRowId.make_changes(self, column='ObjectClass', row_id=index - start,
                                          value=self.ws[f'F{index}'].value)  # Тип объекта
            VariableDefRowId.make_changes(self, column='ObjectProp', row_id=index - start,
                                          value=self.ws[f'G{index}'].value)  # Свойство объекта
            VariableDefRowId.make_changes(self, column='ObjectKey', row_id=index - start,
                                          value=self.ws[f'H{index}'].value)  # Ключ объекта
            VariableDefRowId.make_changes(self, column='OutputMode', row_id=index - start, value=0)  # Режим
            VariableDefRowId.make_changes(self, column='RunsCount', row_id=index - start, value=1)  # N сраб
            VariableDefRowId.make_changes(self, column='TimeStart', row_id=index - start, value=0)  # Время начала
            VariableDefRowId.make_changes(self, column='DT', row_id=index - start, value=0)  # Длительность
            VariableDefRowId.make_changes(self, column='Tag', row_id=index - start, value=0)  # Тэг упрощенного сценария

    def create_log(self, start=4, finish=8, switch_command_line=False):
        VariableDefRowId.__init__(self, rastr_win=self.rastr_win, table='DFWAutoLogicScn',
                                  switch_command_line=switch_command_line)
        self.table.DelRows()
        for index in range(start, finish):
            self.table.AddRow()
            VariableDefRowId.make_changes(self, column='Id', row_id=index - start,
                                          value=self.ws[f'A{index}'].value)  # Id
            VariableDefRowId.make_changes(self, column='Name', row_id=index - start,
                                          value=self.ws[f'B{index}'].value)  # Название
            VariableDefRowId.make_changes(self, column='ParentId', row_id=index - start,
                                          value=self.ws[f'C{index}'].value)  # Номер модуля
            VariableDefRowId.make_changes(self, column='Type', row_id=index - start,
                                          value=self.ws[f'D{index}'].value)  # Тип логики
            VariableDefRowId.make_changes(self, column='Formula', row_id=index - start,
                                          value=self.ws[f'E{index}'].value)  # Формула
            VariableDefRowId.make_changes(self, column='Actions', row_id=index - start,
                                          value=self.ws[f'F{index}'].value)  # Действия
            VariableDefRowId.make_changes(self, column='Delay', row_id=index - start,
                                          value=self.ws[f'G{index}'].value)  # Выдержка времени
            VariableDefRowId.make_changes(self, column='UnitStarters', row_id=index - start,
                                          value=self.ws[f'H{index}'].value)  # ПО мод
            VariableDefRowId.make_changes(self, column='UnitConstants', row_id=index - start,
                                          value=self.ws[f'I{index}'].value)  # Const мод
            VariableDefRowId.make_changes(self, column='UnitActions', row_id=index - start,
                                          value=self.ws[f'J{index}'].value)  # Дейст мод
            VariableDefRowId.make_changes(self, column='UnitActions', row_id=index - start,
                                          value=self.ws[f'H{index}'].value)  # Const мод
            VariableDefRowId.make_changes(self, column='OutputMode', row_id=index - start,
                                          value=self.ws[f'K{index}'].value)  # Режим выхода

    def save_scn(self, dir_file_name_save_scn=None, dir_file=None, name_save_scn=None, switch_command_line=False):
        if dir_file_name_save_scn is not None:
            save_file(rastr_win=self.rastr_win, file_path=dir_file_name_save_scn, shablon=shablon_file_scenario,
                      switch_command_line=switch_command_line)
        elif (dir_file is not None) and (name_save_scn is not None):
            save_file(rastr_win=self.rastr_win, file_path=f'{dir}/{name_save_scn}',
                      shablon=shablon_file_scenario,
                      switch_command_line=switch_command_line)


if __name__ == '__main__':
    import win32com.client
    # from openpyxl import load_workbook
    # from RastrWin.loading.shablons_dir import shablon_file_scenario
    # from RastrWin.loading.save_file_rastrwin import save_file
    # from RastrWin.loading.load_file_rastrwin import load_file

    rastr = win32com.client.Dispatch('Astra.Rastr')
    load_file(rastr_win=rastr, shablon=shablon_file_scenario)
    filename = 'L:\\SER\\Охрименко\\03. RastrWin\\16\\ВЛ 500 кВ Рязанская ГРЭС – Липецкая Восточная.xlsx'
    scn = CreateActionsSCN(rastr_win=rastr, name_list_excel='Сценарий', dir_name_file_excel=filename, )
    scn.create()
    scn.create_log()
    scn.save_scn(dir_file_name_save_scn='L:\\SER\\Охрименко\\03. RastrWin\\16\\scn1.scn', switch_command_line=True)
