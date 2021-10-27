# -*- coding: utf-8 -*-

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Tables.Vetv.vetv import Vetv
from RastrWinLib.Tools.tools import TableOutput


class FindNextSelection:
    """
    Класс FindNextSelection - поиск номера строки по выборке SetSel(key)
    """

    def __init__(self,
                 table: str = None,
                 rastr_win=RASTR):
        f"""
        Класс для поиска по выборки порядкового номера в таблице.\n
        Метод "row" возвращает row_ - порядковый номер строки в таблице.\n
        :param table: название таблицы RastrWin3;\n
        :param rastr_win: True/False - вывод сообщений в протокол;
        """
        self.rastr_win = rastr_win
        if table is not None:
            self.table = self.rastr_win.Tables(table)

    def row(self,
            table: str = None,
            select: str = None):
        f"""
        Метод "row" - возвращает порядковый  номер из таблицы.\n
        :param select: выборка SetSel;\n
        :return: row_: возвращает порядковый номер или -1 в случае отсутствия искомого элемента;
        """
        if table is not None:
            self.table = self.rastr_win.Tables(table)
            self.table.SetSel(select)
            row_ = self.table.FindNextSel(-1)
        else:
            table = self.rastr_win.Tables(table)
            table.SetSel(select)
            row_ = table.FindNextSel(-1)

        if row_ == (-1):
            return False
        else:
            return row_


class Variable(TableOutput, FindNextSelection):
    """
    Класс "Variable" изменяет параметры в таблицах RastrWin3
    """

    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line: bool = False):
        f"""
        Класс для изменений значений ячеек.\n
        :param rastr_win: COM - объект Rastr.Astra (win32com);\n
        :param switch_command_line: True/False - вывод сообщений в протокол;
        """
        super().__init__()
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def __bool__(self):
        return self.switch_command_line

    def make_changes_row(self,
                         table: str = None,
                         column: str = None,
                         row: int = None,
                         value=None) -> None:
        f"""
        Метод: make_changes_row - изменение параметра по заданному row\n
        :param table: название таблицы RastrWin3;\n
        :param column: назваине колонки RastrWin3;\n
        :param row: значение порядкового номера строки;\n
        :param value: значение новой величины заменяемого значения;\n
        :return: Nothing returns
        """

        if table and column and row is not None:
            table_ = self.rastr_win.Tables(table)
            col = table_.Cols(column)
            col.SetZ(row, value)
        else:
            pretty_table = TableOutput(fieldName=['ERROR', 'Описание'])
            row_add(['Таблица', table])
            row_add(['Колонка (стоблец)', column])
            row_add(['Порядковый номер в таблице', row])
            row_add(['Значение', value])
            pretty_table.show(title_table='ERROR: class Variable')

    def make_changes_setsel(self,
                            table: str = None,
                            column: str = None,
                            select: str = None,
                            value=None) -> None:
        f"""
        Метод: make_changes_setsel - изменение параметра по выборки SetSel(key) -> key = "ny=6516516";\n
        :param table: название таблицы RastrWin3;\n
        :param column: название колонки RastrWin3;\n
        :param select: выборка SetSel("ny=52135156") - задается в виде value='ny=52135156';\n
        :param value: значение для замены;\n
        :return: Nothing returns.
        """

        if table and column and select and value is not None:
            table_ = self.rastr_win.Tables(table)
            table_.SetSel(select)
            row_ = table_.FindNextSel(-1)
            if row_ != (-1):
                col = table_.Cols(column)
                col.SetZ(row_, value)
            else:
                pretty_table = TableOutput(fieldName=['ERROR', 'Описание'])
                row_add(['Таблица', table])
                row_add(['Колонка (стоблец)', column])
                row_add(['Выборка', select])
                row_add(['Значение', value])
                pretty_table.show(title_table='ERROR: class Variable method make_changes_setsel\n'
                                              f'Не найдена строка с выборкой:"{select}" -> row=(-1).')
        else:
            pretty_table = TableOutput(fieldName=['ERROR', 'Описание'])
            row_add(['Таблица', table])
            row_add(['Колонка (стоблец)', column])
            row_add(['Выборка', select])
            row_add(['Значение', value])
            pretty_table.show(title_table='ERROR: class Variable method make_changes_setsel')

    def make_changes_vetv(self,
                          table: str = Vetv.table,
                          column: str = None,
                          ip: int = None,
                          iq: int = None,
                          np: int = None,
                          value=None) -> None:
        f"""
        Метод изменяет значение ветви.\n
        :param table: название таблицы RastrWin3;\n
        :param column: название колонки (столбца) RastrWin3;\n
        :param ip: номер начала ветви;\n
        :param iq: номер конца ветви;\n
        :param np: номер параллельности ветви;\n
        :param value: значение;\n
        :return: Nothing returns
        """
        if (table | column | ip | iq | np | value) is not None:
            table_ = self.rastr_win.Tables(table)
            table_.SetSel(f'(ip={ip};iq={iq};np={np})|(ip={iq};iq={ip};np={np})')
            row_ = table_.FindNextSel(-1)

            row = row_with_table(table=table, key=f'(ip={ip};iq={iq};np={np})|(ip={iq};iq={ip};np={np})')
        if row != (-1):
            col = table_.Cols(column)
            col.SetZ(row, value)
        else:
            print('Error')


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.Load import load_file

    load_file(rastr_win=RASTR,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
              shabl='сценарий',
              switch_command_line=False)

    load_file(rastr_win=RASTR,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
              shabl='динамика',
              switch_command_line=False)

    find = FindNextSelection(rastr_win=RASTR,
                             table="com_dynamics")

    tras = RASTR.Tables("com_dynamics").Cols("Tras").Z(0)

    print(find.row(key=tras))
