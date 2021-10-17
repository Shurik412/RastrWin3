# -*- coding: utf-8 -*-
from os import path

from prettytable import PrettyTable

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Templates import directory_shabl


def save_file(rastr_win=RASTR,
              path_file: str = None,
              shabl: str = None,
              switch_command_line: bool = False):
    """
    Сохраняет информацию из рабочей области в файле name по шаблону shabl.

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param path_file: директория и название файла сохранения файла;
    :param shabl: шаблон RastrWin3 для сохранения;
    :param switch_command_line: True/False - выводит сообщения в протокол;
    :return: True;
    """
    rastr_win.Save(path_file, directory_shabl(rus_name_shabl=shabl))

    if switch_command_line:
        pt = PrettyTable()
        pt.title = 'Сохранение файла RastrWin3'
        pt.field_names = ['Файл', 'Шаблон']
        if path_file == '' or path_file is None:
            pt.add_row(['Ссылка для сохранения файла не задана!', shabl])
        else:
            pt.add_row([f'{path.basename(path_file)}', shabl])
    return True


if __name__ == '__main__':
    from RastrWinLib.Load import load_file
    from RastrWinLib.AstraRastr import RASTR

    load_file(rastr_win=RASTR,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.scn',
              shabl='сценарий',
              switch_command_line=True)

    load_file(rastr_win=RASTR,
              path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
              shabl='динамика',
              switch_command_line=True)

    save_file(path_file=r'C:\Users\Ohrimenko_AG\Desktop\test_911.rst',
              switch_command_line=True,
              shabl='динамика')
