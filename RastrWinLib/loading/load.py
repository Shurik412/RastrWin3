# -*- coding: utf-8 -*-
from os import path

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.loading.shablon import shablon_file_automation
from RastrWinLib.log_tools.tools import separator_grid


def load_file(rastr_win=RASTR,
              rg_kod=1,
              file_path='',
              shablon=shablon_file_automation,
              switch_command_line=False):
    """
   :param rastr_win: COM - объект Rastr.Astra (win32com);
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
    :param shablon: шаблон RastrWin3 для загрузки;
    :param file_path: абсолютный путь с именем файла (пример:C:\\Folder\\ДРМ.rst);
    :param switch_command_line: True/False - выводит сообщения в протокол.
    :return: True
    """

    rg_kod = rg_kod
    rastr_win = rastr_win
    rastr_win.Load(rg_kod, file_path, shablon)

    if switch_command_line is not False:
        print(f'{separator_grid}\n'
              f'Загружен файл: "{path.basename(file_path)}", по шаблону: "{path.basename(shablon)}".\n'
              f'{separator_grid}\n')


class LoadRUSTab:

    def __init__(self, rastr_win=RASTR, shablon=shablon_file_automation, rg_kod=1, switch_command_line=False):
        """

        :param rastr_win: com - объект Rastr.Astra
        :param shablon: шаблон RastrWin3 для загрузки.
        :param rg_kod:
        :param switch_command_line: True/False - выводит сообщения в протокол.
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
            print(f'Добавлена структура рабочей области по шаблону: "{path.basename(self.shablon)}".')
        return True

    def load(self, file_path):
        """

        :param file_path:
        :return: True
        """
        self.rastr_win.Load(self.rg_kod, file_path, self.shablon)
        if self.switch_command_line is not None:
            print(f'Загружен файл: "{path.basename(file_path)}", по шаблону: "{path.basename(self.shablon)}".')
        return True

    def load_new_file(self):
        """

        :return: True
        """
        self.rastr_win.NewFile(self.shablon)
        if self.switch_command_line is not None:
            print(f'Очищена рабочая область по шаблону: "{path.basename(self.shablon)}".')
        return True
