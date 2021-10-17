# -*- coding: utf-8 -*-
from prettytable import PrettyTable


class OutputResultsProtocol:
    """

    """

    def __init__(self):
        # super().__init__()
        self.pt = PrettyTable()

    def any_tables_output_when_using_formula(self, table, formula):
        self.pt.field_names = ['Таблица', 'Формула', 'Описание ошибки']
        self.pt.add_row([{table}, {formula}, 'Объект не найден! Проверьте формулу (выборку)!'])
        print(self.pt)


class ErrorOutputProtocol(PrettyTable):
    """

    """

    def __init__(self):
        super().__init__()
        self.pt = PrettyTable()

    def any_tables_output_when_using_formula(self, table, formula):
        self.field_names = ['Таблица', 'Формула', 'Описание ошибки']
        self.add_row([{table}, {formula}, 'Объект не найден! Проверьте формулу (выборку)!'])
        print(self.pt)

    def output_node(self, table, ny):
        self.field_names = ['Таблица', 'Номер узла', 'Описание ошибки']
        self.add_row([{table}, {ny}, 'Объект не найден! Проверьте номер узла!'])

    def output_vetv(self, table, ip, iq, np):
        pass

    def output_generator(self, table, num):
        self.field_names = ['Таблица', 'Номер генератора', 'Описание ошибки']
        self.add_row([{table}, {num}, 'Объект не найден! Проверьте номер генератора!'])


if __name__ == '__main__':
    from RastrWinLib.Load import load_file
    from RastrWinLib.Load.shablon import Shabl
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.ActionsObject.Delete import Delete

    load_file(rastr_win=RASTR,
              file_path=r'',
              shabl=Shabl.shablon_file_automation,
              switch_command_line=True)

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
              shabl=Shabl.shablon_file_scenario,
              switch_command_line=True)

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
              shabl=Shabl.shablon_file_dynamic,
              switch_command_line=True)

    delete = Delete()
    output = ErrorOutput()
