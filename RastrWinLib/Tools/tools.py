# -*- coding: utf-8 -*-
from prettytable import PrettyTable


def changing_number_of_semicolons(number, digits=0):
    return f"{number:.{digits}f}"


class TableOutput(PrettyTable):
    """

    """

    def __init__(self, fieldName):
        """

        :param fieldName:
        """
        super().__init__()
        self.field_names = fieldName

    def row_add(self, message) -> None:
        """
        Add
        :param message:
        :return:
        """
        self.add_row(message)

    def show(self, title_table: str) -> None:
        """
        :return:
        """
        print(self.get_string(title=title_table))


if __name__ == '__main__':
    tb = TableOutput(fieldName=['Описание', 'Параметр'])
    tb.row_add(['Время расчета для динамики', 'cек.'])
    tb.row_add(['Время расчета для динамики', 'cек.'])
    tb.row_add(['Время расчета для динамики', 'cек.'])
    tb.row_add(['Время расчета для динамики', 'cек.'])
    tb.show(title_table='Параметры')

    print(changing_number_of_semicolons(number=15315.00515, digits=5))
