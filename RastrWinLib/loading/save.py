# -*- coding: utf-8 -*-
from os import path

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.loading.shablon import shablon_file_dynamic
from RastrWinLib.log_tools.tools import separator_grid


def save_file(rastr_win=RASTR,
              file_path='',
              shablon=shablon_file_dynamic,
              switch_command_line=False):
    """
    Сохраняет информацию из рабочей области в файле name по шаблону shablon
    :param rastr_win: объект RastrWinLib = win32com.client.Dispatch("Astra.Rastr")
    :param file_path: директория и название файла сохранения файла
    :param shablon: шаблон
    :param switch_command_line: True - вывод сообщения о выполнении.
    :return: True
    """
    rastr_win.save(file_path, shablon)

    if switch_command_line is not False:
        print(separator_grid)
        if file_path == '':
            print(f'Ссылка для сохранения файла не задана!')
        else:
            print(f'Файл "{path.basename(file_path)}" сохранен по шаблону "{path.basename(shablon)}".')
        print(separator_grid)
    return True