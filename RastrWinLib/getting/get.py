# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.tables_attributes import com_cxema_table, com_cxema_attributes, node_table, generator_table, \
    vetv_table


class GettingParameter:
    def __init__(self, rastr_win=RASTR):
        self.rastr_win = rastr_win
        """
        Класс предназначен для работы с ячейками таблиц в RastrWin3.
        1. Метод get_cell - возвращает значение ячейки из таблицы.
        2. Метод get_row_line - возвращает значение ячейки из таблицы "Ветви".
        3. Метод get_row_node - возвращает значение ячейки из таблицы "Узлы".
        4. 
        """
    def get_cell(self, table, column, row_id):
        """
        Метод get_cell - возвращает значение ячейки.
        :param table: название таблицы RastrWin3 (generator)
        :param column: навание колонки (столбца) RastrWin3 (Num)
        :param row_id: порядковый номер в таблице (от 0 до max.count)
        :return: value_cell_of_row - возвращает значение ячейки по номеру row_id
        """
        table_ = self.rastr_win.Tables(table)
        value_cell_of_row = table_.Cols(column).Z(row_id)
        return value_cell_of_row

    def get_row_vetv(self, ip, iq, np):
        """
        Метод get_row_line - возвращает порядковый номер строки таблицы "Ветви".
        :param ip: начало ветви;
        :param iq: конец ветви;
        :param np: номер паралельности ветви;
        :return: row_vetv: номер строки таблицы ветви.
        """
        table_ = self.rastr_win.Tables(vetv_table)
        table_.SetSel(f'(ip={ip};iq={iq};np={np})|(ip={iq};iq={ip};np={np})')
        row_vetv = table_.FindNextSel(-1)
        return row_vetv

    def get_row_node(self, node_ny):
        """
        Метод get_row_node - возвращает
        :param node_ny:
        :return:
        """
        table_ = self.rastr_win.Tables(node_table)
        table_.SetSel(f'(ny={node_ny})')
        row = table_.FindNextSel(-1)
        return row

    def get_row_gen(self, num, table=generator_table):
        table_ = self.rastr_win.Tables(table)
        table_.SetSel(f'(num={num})')
        row = table_.FindNextSel(-1)
        return row


class GetTableCommonInfo:
    """

    """

    def __init__(self, rastr_win=RASTR, switch_command_line=False, path_file_log=False):
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(com_cxema_table)
        self.switch_command_line = switch_command_line
        self.path_file_log = path_file_log
        if path_file_log is not False:
            self.file_log = open(path_file_log, 'w')

    def get(self):
        if self.path_file_log is not False:
            self.file_log.write(f'Таблица: Общая информация -> {com_cxema_table}\n')
            print(f'Таблица: Общая информация -> {com_cxema_table}')
        else:
            print(f'Таблица: Общая информация -> {com_cxema_table}')
        for key_ in com_cxema_attributes:
            column = self.table.Cols(key_)
            parametr = column.Z(0)
            if self.path_file_log is not False:
                if type(parametr) == float:
                    self.file_log.write(f'{com_cxema_table[key_]} = {"%.2f" % parametr}\n')
                    print(f'{com_cxema_attributes[key_]} = {"%.2f" % parametr}')
                else:
                    self.file_log.write(f'{com_cxema_attributes[key_]} = {parametr}\n')
                    print(f'{com_cxema_attributes[key_]} = {parametr}')
            else:
                if type(parametr) == float:
                    print(f'{com_cxema_attributes[key_]} = {"%.2f" % parametr}')
                else:
                    print(f'{com_cxema_attributes[key_]} = {parametr}')


class GettingParameterAttribute:
    """
    """

    def __init__(self, table, rastr_win=RASTR, switch_command_line=False):
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)
        self.switch_command_line = switch_command_line

    def getting(self, column, key=None, ip=None, iq=None, np=None):
        if key is not None:
            self.table.SetSel(key)
            row = self.table.FindNextSel(-1)
            if row != (-1):
                parameter = self.table.Cols(column).Z(row)
                if self.switch_command_line is not False:
                    print(f'\tПолучен параметр таблицы "{self.table.Description}" => "{column}" => "{parameter}";')
                return parameter
            else:
                return print(f'Не найден параметр с таким номеров в таблице "{self.table.Description}".')
        elif ip and iq and np is not None and self.table.Name == 'vetv':
            self.table.SetSel(f'(ip={ip}&iq={iq}&np={np})|(ip={iq}&iq={ip}&np={np})')
            row = self.table.FindNextSel(-1)
            if row != (-1):
                parameter = self.table.Cols(column).Z(row)
                if self.switch_command_line is not False:
                    print(f'\tПолучен параметр таблицы "{self.table.Description}" => "{column}" => "{parameter}";')
                return parameter
            else:
                return print(f'Не найден параметр с таким номеров в таблице "{self.table.Description}".')
