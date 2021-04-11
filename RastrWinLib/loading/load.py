# -*- coding: utf-8 -*-
from os import path

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.loading.shablon import shablon_file_automation


def load_file(rastr_win=RASTR, rg_kod=1, file_path='', shablon=shablon_file_automation, switch_command_line=False):
    """
      par: RG_KOD – числовое значение, определяет режим загрузки при наличии таблицы
               в рабочей области и может быть одним из следующих:
               Константа   Значение           Описание
               RG_ADD          0       Таблица добавляется к имеющейся в рабочей области, совпадение ключевых полей не
                                        контролируются (соответствует режиму «Присоединить» в меню).
               RG_REPL         1       Таблица в рабочей области замещается (соответствует режиму «Загрузить» в меню)
               RG_KEY          2       Данные в таблице, имеющие одинаковые ключевые поля, заменяются. Если ключ не
                                        найден, то данные игнорируются (соответствует режиму «Обновить» в меню)
               RG_ADDKEY       3       Данные в таблице, имеющие одинаковые ключевые поля, заменяются.
                                       Если ключ не найден, то данные вставляются (соответствует режиму «Объединить»)
       par: shablon - шаблон для загрузки.
       par: file_path - абсолютный путь с именем файла (пример:C:\\Folder\\ДРМ.rst)
       """
    rg_kod = int(rg_kod)
    rastr_win = rastr_win
    switch_command_line: bool

    rastr_win.Load(rg_kod, file_path, shablon)

    if switch_command_line is not False:
        print(f'Загружен файл: "{path.basename(file_path)}", по шаблону: "{path.basename(shablon)}".')
    return True


class LoadRUSTab:
    """

    """

    def __init__(self, rastr_win=RASTR, shablon=shablon_file_automation, rg_kod=1, switch_command_line=False):
        self.rastr_win = rastr_win
        self.shablon = shablon
        self.rg_kod = int(rg_kod)
        self.switch_command_line = switch_command_line

    def load_shablon_automation(self):
        self.rastr_win.Load(2, '', self.shablon)
        if self.switch_command_line is not None:
            print(f'Добавлена структура рабочей области по шаблону: "{path.basename(self.shablon)}".')
        return True

    def load(self, file_path):
        self.rastr_win.Load(self.rg_kod, file_path, self.shablon)
        if self.switch_command_line is not None:
            print(f'Загружен файл: "{path.basename(file_path)}", по шаблону: "{path.basename(self.shablon)}".\n'
                  f'\t\t - существующие данные не изменились!')
        return True

    def load_new_file(self):
        self.rastr_win.NewFile(self.shablon)
        if self.switch_command_line is not None:
            print(f'Очищена рабочая область по шаблону: "{path.basename(self.shablon)}".')
        return True


if __name__ == '__main__':
    import win32com.client
    from RastrWinLib.loading.shablon import shablon_file_dynamic

    RastrWin = win32com.client.Dispatch("Astra.Rastr")
    # load_file(rastr_win=RastrWinLib,
    #           rg_kod=1,
    #           file_path='C:\\Users\\Ohrimenko_AG\\Documents\\RastrWinLib\\test-rastr\\RUSTab\\test9.rst',
    #           shablon=shablon_file_dynamic,
    #           switch_command_line=True)

    load_file = LoadRUSTab(rastr_win=RastrWin,
                           shablon=shablon_file_dynamic,
                           switch_command_line=True)
    load_file.load(file_path='C:\\Users\\Ohrimenko_AG\\Documents\\RastrWinLib\\test-rastr\\RUSTab\\test9.rst')

    load_file.load_new_file()
    load_file.load_shablon_automation()
