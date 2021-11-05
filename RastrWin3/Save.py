# -*- coding: utf-8 -*-
from RastrWin3.AstraRastr import RASTR
from RastrWin3.Templates import ROOT_DIR_SHABLON, Key_to_select_location
from RastrWin3.Tools.tools import TableOutput
from RastrWin3.Templates import ROOT_DIR_SHABLON


def save_file(rastr_win=RASTR,
              path_file: str = None,
              name_shabl_russian: str = None,
              switch_command_line: bool = False) -> None:
    f"""
    Сохраняет информацию из рабочей области в файле path_file по шаблону name_shabl_russian.\n

    :param rastr_win: COM - объект Rastr.Astra (win32com);\n
    :param path_file: директория и название файла сохранения файла;\n
    :param name_shabl_russian: шаблон RastrWin3 для сохранения;\n
    :param switch_command_line: True/False - выводит сообщения в протокол;\n
    :return: Nothing;\n
    """
    _root_dir_shablon_obj = ROOT_DIR_SHABLON()

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

    if name_shabl_russian is None or name_shabl_russian == '' or name_shabl_russian == ' ':
        _save = save(path_file_save=path_file, shablon="")
        if _save:
            _name_shabl_russian = 'без шаблона \n по-умолчанию выбран: "режим"'
            _shabl_rgm = _root_dir_shablon_obj.directory_shabl(russian_name_shabl=str(name_shabl_russian))
            save(path_file_save=path_file, shablon=_shabl_rgm)
            if switch_command_line:
                _pretty_table = TableOutput(fieldName=['Файл', 'Шаблон'])
                _pretty_table.title = 'Сохранение файла RastrWin3'
                if path_file == '' or path_file == ' ' or path_file is None:
                    _pretty_table.row_add(['Ссылка для сохранения файла не задана!', _name_shabl_russian])
                else:
                    _pretty_table.row_add([path_file, name_shabl_russian])
                _pretty_table.show(title_table='Сохранение файла RastrWin3')
    else:
        _shabl_path_file = _root_dir_shablon_obj.directory_shabl(russian_name_shabl=str(name_shabl_russian))
        _save = save(path_file_save=path_file, shablon=_shabl_path_file)
        if _save:
            if switch_command_line:
                _pretty_table = TableOutput(fieldName=['Файл', 'Шаблон'])
                _pretty_table.add_row([path_file, _shabl_path_file])
                _pretty_table.show(title_table='Сохранение файла RastrWin3')
