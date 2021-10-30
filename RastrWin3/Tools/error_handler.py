# -*- coding: utf-8 -*-
import pythoncom
from RastrWin3.Tools.tools import TableOutput


def error_load_file(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except pythoncom.com_error as error:
            hr, msg, exc, arg = error.args
            pt = TableOutput(fieldName=['Сообщение'])
            pt.row_add(message=[exc[2]])
            print(error)
            # print(hr)  # -2147352567
            # print(msg)  # Ошибка.
            # print(exc)  # (0, 'Astra.Rastr.1', 'Ошибка открытия файла asd2 ', None, 0, -2147467259)
            # print(arg)  # None
            pt.show(title_table=f'Ошибка при запуске функции: "{func.__name__}"')

        except ValueError as error:
            print(error)
            pt = TableOutput(fieldName=['Сообщение'])
            pt.row_add(message=[f'Тип аргумента "rg_kod" должен быть int а не "";\n {error}'])
            pt.show(title_table=f'Ошибка при запуске функции: "{func.__name__}"')

    return wrapper
