# -*- coding: utf-8 -*-
from R_modules.load_and_save_file.shablons_dir import shablon_file_dynamic
from os import path


def save_file(rastr_win, file_path='', shablon=shablon_file_dynamic, switch_command_line=False):
    """
    Сохраняет информацию из рабочей области в файле name по шаблону shablon
    :param rastr_win: объект RastrWin = win32com.client.Dispatch("Astra.Rastr")
    :param file_path: директория и название файла сохранения файла
    :param shablon: шаблон
    :param switch_command_line: True - вывод сообщения о выполнении.
    :return:
    """
    rastr_win.save(file_path, shablon)

    if switch_command_line is not False:
        if file_path == '':
            print(f'Ссылка для сохранения файла не задана!')
        else:
            print(f'Файл "{path.basename(file_path)}" сохранен по шаблону "{path.basename(shablon)}".')


if __name__ == '__main__':
    import win32com.client
    from load_file_rastrwin import load_file

    RastrWin = win32com.client.Dispatch("Astra.Rastr")
    load_file(rastr_win=RastrWin,
              rg_kod=1,
              file_path='C:\\Users\\Ohrimenko_AG\\Documents\\RastrWin3\\test-rastr\\RUSTab\\test9.rst',
              shablon=shablon_file_dynamic,
              switch_command_line=True)

    save_file(rastr_win=RastrWin,
              file_path='C:\\Users\\Ohrimenko_AG\\Desktop\\21\\test9.rst',
              shablon=shablon_file_dynamic,
              switch_command_line=True)