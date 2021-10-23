# -*- coding: utf-8 -*-
from prettytable import PrettyTable

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Tables.Dynamic.Generator import Generator
from RastrWinLib.Tables.Node.node import Node
from RastrWinLib.Tables.Vetv.vetv import Vetv
from RastrWinLib.Tools.сonclutation_output import ErrorOutputProtocol
from RastrWinLib.Tools.сonclutation_output import OutputResultsProtocol


class Delete(ErrorOutputProtocol, OutputResultsProtocol):
    """
    Удаляет заданный элемент (объект) из таблицы заданной таблицы
    """

    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line: bool = False):
        """
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        super().__init__()
        self.output = OutputResultsProtocol()
        self.outputError = ErrorOutputProtocol()
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def __bool__(self):
        return self.switch_command_line

    def delete_by_SetSel_vetv(self, formula: str = None):
        """
        Удаляет из таблицы "Ветви" выбранную ветв по формуле SetSel
        :param formula: формула ("ip=")
        :return: nothing returns;
        """
        if formula is not None:
            table_ = self.rastr_win.Tables(Vetv.table)
            table_.SetSel(formula)
            table_.delete()
            if self.switch_command_line:
                message(table=Vetv.table_name, number_or_formula=formula)
        else:
            message_error(table=Vetv.table_name, number_or_formula=formula)

    def delete_by_SetSel_node(self, formula: str = None):
        """
        Удаление из таблицы "Узлы" выбранный узел по формуле SetSel
        :param formula: Задать выборку. Выборка задается в виде формулы,
                        имеющей логическое значение: 0 – не в выборке,
                        1 – в выборке. Выборку можно представить как некоторый дополнительный
                        временный столбец, заданный формулой
        :return: nothing returns;
        """
        if formula is not None:
            table_ = self.rastr_win.Tables(Node.table)
            table_.SetSel(formula)
            table_.delete()
            if self.switch_command_line:
                message(table=Node.table_name, number_or_formula=formula)
        else:
            message_error(table=Node.table_name, number_or_formula=formula)

    def delete_by_SetSel_generator(self, formula: str = None):
        """

        :param formula:
        :return: nothing returns;
        """
        if formula is not None:
            table_ = self.rastr_win.Tables(Generator.table)
            table_.SetSel(formula)
            table_.delete()
            if self.switch_command_line:
                message(table=Generator.table_name, number_or_formula=formula)
        else:
            message_error(table=Generator.table_name, number_or_formula=formula)

    def delete_SetSel_any_table(self, table: str = None, formula: str = None):
        """

        :param table:
        :param formula:
        :return: nothing returns;
        """
        if table and formula is not None:
            table_ = self.rastr_win.Tables(table)
            table_.SetSel(formula)
            row = table_.FindNextSel(-1)
            if row != (-1):
                table_.delete(row)
            else:
                self.outputError.any_tables_output_when_using_formula(table=table, formula=formula)
            if self.switch_command_line:
                self.output.any_tables_output_when_using_formula(table=table, formula=formula)
        else:
            self.outputError.any_tables_output_when_using_formula(table=table, formula=formula)

    def delete_by_node_ny(self, ny: int = None):
        """
        Удаление из таблицы "Узлы" выбранный узел по формуле SetSel
        :param ny: номер узла (ny=51700111)
        :return: nothing returns;
        """
        if ny is not None:
            table_ = self.rastr_win.Tables(Node.table)
            table_.SetSel(f'ny={ny}')
            table_.delete()
            if self.switch_command_line:
                message(table=Node.table_name, number_or_formula=ny)
        else:
            message_error(table=Node.table_name, number_or_formula=ny)

    def set_selection(self, table):
        pt = PrettyTable()
        pt.field_names = ['Таблица', 'Формула', ]
        table.SetSel(formula)
        row_number = table.FindNextSel(-1)
        if row_number == -1:
            pass

    @staticmethod
    def message(table, number_or_formula):
        """

        :param table:
        :param number_or_formula:
        :return: nothing returns;
        """
        pt = PrettyTable()
        pt.field_names = ['Таблица', 'Номер/Формула']
        pt.add_row([table, number_or_formula])
        print(pt.get_string(title="Удаление элемента из Таблицы RastrWin3"))

    @staticmethod
    def message_error(table, number_or_formula):
        """

        :param table:
        :param number_or_formula:
        :return: nothing returns;
        """
        pt = PrettyTable()
        pt.field_names = ['Таблица', 'Номер/Формула']
        pt.add_row([table, number_or_formula])
        print(pt.get_string(title="ERROR: Удаление элемента из Таблицы RastrWin3"))


if __name__ == '__main__':
    from RastrWinLib.Load import load_file
    from RastrWinLib.Load.shablon import Shabl
    from RastrWinLib.AstraRastr import RASTR

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

    # delete = Delete(switch_command_line=True)
    # # output = ErrorOutput()
    # #
    # delete.delete_SetSel_any_table(table=Node.table, formula='ny=1')
    tab = RASTR.Tables(Node.table)
    print(tab.Name)
