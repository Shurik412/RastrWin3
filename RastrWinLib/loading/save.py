# -*- coding: utf-8 -*-
from os import path

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.loading.shablon import Shabl
from RastrWinLib.log_tools.tools import separator_grid


def save_file(rastr_win=RASTR,
              file_path='',
              shablon=Shabl.shablon_file_dynamic,
              switch_command_line=False):
    """
    Сохраняет информацию из рабочей области в файле name по шаблону shablon
    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param file_path: директория и название файла сохранения файла
    :param shablon: шаблон
    :param switch_command_line: True - вывод сообщения о выполнении.
    :return: True
    """
    rastr_win.save(file_path, shablon)

    if switch_command_line is not False:
        if file_path == '':
            print(f'{separator_grid}\n'
                  f'Ссылка для сохранения файла не задана!\n'
                  f'{separator_grid}\n')
        else:
            print(f'{separator_grid}\n'
                  f'Файл "{path.basename(file_path)}" сохранен по шаблону "{path.basename(shablon)}".\n'
                  f'{separator_grid}\n')
    return True
