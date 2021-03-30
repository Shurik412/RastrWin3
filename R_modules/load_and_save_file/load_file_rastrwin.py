# -*- coding: utf-8 -*-
from R_modules.load_and_save_file.shablons_dir import shablon_file_automation, shablon_file_dynamic, \
    shablon_file_regime, shablon_file_scenario
from os import path


def load_file(rastr_win, rg_kod=1, file_path='', shablon=shablon_file_automation, switch_command_line=False):
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


class LoadRUSTab:
    """
    """

    def __init__(self, rastr_win, shablon=shablon_file_automation, rg_kod=1, switch_command_line=False):
        self.rastr_win = rastr_win
        self.shablon = shablon
        self.rg_kod = int(rg_kod)
        self.switch_command_line = switch_command_line

    def load_shablon_automation(self):
        self.rastr_win.Load(2, '', self.shablon)
        if self.switch_command_line is not None:
            print(f'Добавлена структура рабочей области по шаблону: "{path.basename(self.shablon)}".')

    def load(self, file_path):
        self.rastr_win.Load(self.rg_kod, file_path, self.shablon)
        if self.switch_command_line is not None:
            print(f'Загружен файл: "{path.basename(file_path)}", по шаблону: "{path.basename(self.shablon)}".\n'
                  f'\t\t - cуществующие данные не изменились!')

    def loadNewFile(self):
        self.rastr_win.NewFile(self.shablon)
        if self.switch_command_line is not None:
            print(f'Очищена рабочая область по шаблону: "{path.basename(self.shablon)}".')


if __name__ == '__main__':
    import win32com.client
    from R_modules.load_and_save_file.shablons_dir import shablon_file_dynamic

    RastrWin = win32com.client.Dispatch("Astra.Rastr")
    # load_file(rastr_win=RastrWin,
    #           rg_kod=1,
    #           file_path='C:\\Users\\Ohrimenko_AG\\Documents\\RastrWin3\\test-rastr\\RUSTab\\test9.rst',
    #           shablon=shablon_file_dynamic,
    #           switch_command_line=True)

    load_file = LoadRUSTab(rastr_win=RastrWin,
                           shablon=shablon_file_dynamic,
                           switch_command_line=True)
    load_file.load(file_path='C:\\Users\\Ohrimenko_AG\\Documents\\RastrWin3\\test-rastr\\RUSTab\\test9.rst')

    load_file.loadNewFile()
    load_file.load_shablon_automation()
