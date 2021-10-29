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
    rastr_win.Save(path_file, directory_shabl(rus_name_shabl=shabl))

    if switch_command_line:
        pt = TableOutput(fieldName=['Файл', 'Шаблон'])
        pt.title = 'Сохранение файла RastrWin3'
        if path_file == '' or path_file == ' ' or path_file is None:
            pt.row_add(['Ссылка для сохранения файла не задана!', shabl])
        else:
            pt.row_add([f'{path_file}', shabl])
        pt.show(title_table='Сохранение файла RastrWin3')
