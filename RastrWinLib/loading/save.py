# -*- coding: utf-8 -*-
from os import path

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.loading.shablon import Shabl
from RastrWinLib.tools.tools import Tools


def save_file(rastr_win=RASTR,
              file_path='',
              shabl=Shabl.shablon_file_dynamic,
              switch_command_line=False):
    """
    Сохраняет информацию из рабочей области в файле name по шаблону shabl.

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param file_path: директория и название файла сохранения файла;
    :param shabl: шаблон RastrWin3 для загрузки;
    :param switch_command_line: True/False - выводит сообщения в протокол.
    :return: True
    """
    rastr_win.save(file_path, shabl)

    if switch_command_line is not False:
        if file_path == '':
            print(f'{Tools.separator_grid}\n'
                  f'Ссылка для сохранения файла не задана!\n'
                  f'{Tools.separator_grid}\n')
        else:
            print(f'{Tools.separator_grid}\n'
                  f'Файл "{path.basename(file_path)}" сохранен по шаблону "{path.basename(shabl)}".\n'
                  f'{Tools.separator_grid}\n')
    return True
