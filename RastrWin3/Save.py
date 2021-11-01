# -*- coding: utf-8 -*-
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Templates import directory_shabl
from RastrWin3.Tools.tools import TableOutput


def save_file(rastr_win=RASTR,
              path_file: str = None,
              shabl: str = None,
              switch_command_line: bool = False) -> None:
    """
    Сохраняет информацию из рабочей области в файле name по шаблону shabl.

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param path_file: директория и название файла сохранения файла;
    :param shabl: шаблон RastrWin3 для сохранения;
    :param switch_command_line: True/False - выводит сообщения в протокол;
    :return: None;
    """

    def save(path_file_save: str, shablon: str) -> bool:
        try:
            rastr_win.Save(path_file_save, shablon)
        except pywintypes.com_error as er:
            hr, msg, exc, arg = er.args
            table_output = TableOutput(fieldName=['Сообщение'])
            table_output.row_add(message=[exc[2]])
            table_output.show(title_table=f'Ошибка при запуске функции: "{save_file.__name__}"')
            return False
        except pythoncom.com_error as error:
            hr, msg, exc, arg = error.args
            table_output = TableOutput(fieldName=['Сообщение'])
            table_output.row_add(message=[exc[2]])
            table_output.show(title_table=f'Ошибка при запуске функции: "{save_file.__name__}"')
            return False
        except ValueError as error:
            table_output = TableOutput(fieldName=['Сообщение'])
            table_output.row_add(message=[f'Тип аргумента "rg_kod" должен быть int а не "";\n {error}'])
            table_output.show(title_table=f'Ошибка при запуске функции: "{save_file.__name__}"')
            return False
        else:
            return True

    if shabl is None or shabl == '' or shabl == ' ':
        save_ = save(path_file_save=path_file, shablon="")
        if save_:
            shabl = 'без шаблона \n по-умолчанию выбран: "режим"'
            shabl_rgm = directory_shabl(rus_name_shabl='режим')
            save(path_file_save=path_file, shablon=shabl_rgm)
            if switch_command_line:
                pt = TableOutput(fieldName=['Файл', 'Шаблон'])
                pt.title = 'Сохранение файла RastrWin3'
                if path_file == '' or path_file == ' ' or path_file is None:
                    pt.row_add(['Ссылка для сохранения файла не задана!', shabl])
                else:
                    pt.row_add([path_file, shabl])
                pt.show(title_table='Сохранение файла RastrWin3')
    else:
        shabl_path_file = directory_shabl(rus_name_shabl=shabl)
        load = load_(kod_rg=rg_kod, pathFile=path_file, shablon=shabl_path_file)
        if load:
            if switch_command_line:
                pt = TableOutput(fieldName=['Файл', 'Шаблон'])
                pt.add_row([path_file, shabl_path_file])
                pt.show(title_table='Сохранение файла RastrWin3')
