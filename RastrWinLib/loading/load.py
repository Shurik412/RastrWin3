# -*- coding: utf-8 -*-
from os import path

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.loading.shablon import Shabl
from RastrWinLib.tools.tools import Tools


def load_file(rastr_win=RASTR,
              rg_kod=1,
              file_path='',
              shabl=Shabl.shablon_file_automation,
              switch_command_line=False):
    f"""
    Загружает файл данных name в рабочую область в соответствии с шаблоном типа shabl.
    Если поле shabl пусто, то загружается name без шаблона, если пусто поле name, то загружается только шаблон.

   :param rastr_win: {Tools.RastrDoc};
   :param rg_kod: числовое значение, определяет режим загрузки при наличии таблицы
            в рабочей области и может быть одним из следующих:
            Константа   Значение           Описание
            RG_ADD          0       Таблица добавляется к имеющейся в рабочей области, совпадение ключевых полей не
                                     контролируются (соответствует режиму «Присоединить» в меню).
            RG_REPL         1       Таблица в рабочей области замещается (соответствует режиму «Загрузить» в меню)
            RG_KEY          2       Данные в таблице, имеющие одинаковые ключевые поля, заменяются. Если ключ не
                                     найден, то данные игнорируются (соответствует режиму «Обновить» в меню)
            RG_ADDKEY       3       Данные в таблице, имеющие одинаковые ключевые поля, заменяются.
                                    Если ключ не найден, то данные вставляются (соответствует режиму «Объединить»)
    :param shabl: шаблон RastrWin3 для загрузки;
    :param file_path: абсолютный путь с именем файла (пример:C:\\Folder\\ДРМ.rst);
    :param switch_command_line: {Tools.switch_command_line_doc}
    :return: True
    """

    rg_kod = rg_kod
    rastr_win = rastr_win
    rastr_win.Load(rg_kod, file_path, shabl)

    if switch_command_line is not False:
        print(f'{Tools.separator_grid}\n'
              f'Загружен файл: "{path.basename(file_path)}", по шаблону: "{path.basename(shablon)}".\n'
              f'{Tools.separator_grid}\n')


class LoadRUSTab:

    def __init__(self,
                 rastr_win=RASTR,
                 shablon=ShablonsRastrWin.shablon_file_automation,
                 rg_kod=1,
                 switch_command_line=False):
        f"""

        :param rastr_win: {Tools.RastrDoc};
        :param shablon: шаблон RastrWin3 для загрузки.
        :param rg_kod:
        :param switch_command_line: {Tools.switch_command_line_doc};
        """
        self.rastr_win = rastr_win
        self.shablon = shablon
        self.rg_kod = int(rg_kod)
        self.switch_command_line = switch_command_line

    def load_shablon_automation(self):
        """

        :return:
        """
        self.rastr_win.Load(2, '', self.shablon)
        if self.switch_command_line is not None:
            print(f'{Tools.separator_grid}\n'
                  f'Добавлена структура рабочей области по шаблону: "{path.basename(self.shablon)}".\n'
                  f'{Tools.separator_grid}\n')
        return True

    def load(self, file_path):
        """

        :param file_path:
        :return: True
        """
        self.rastr_win.Load(self.rg_kod, file_path, self.shablon)
        if self.switch_command_line is not None:
            print(f'{Tools.separator_grid}\n'
                  f'Загружен файл: "{path.basename(file_path)}", по шаблону: "{path.basename(self.shablon)}".'
                  f'{Tools.separator_grid}\n')
        return True

    def load_new_file(self):
        """

        :return: True
        """
        self.rastr_win.NewFile(self.shablon)
        if self.switch_command_line is not None:
            print(f'{Tools.separator_grid}\n'
                  f'Очищена рабочая область по шаблону: "{path.basename(self.shablon)}".'
                  f'{Tools.separator_grid}\n')
        return True
