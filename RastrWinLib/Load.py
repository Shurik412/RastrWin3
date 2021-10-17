# -*- coding: utf-8 -*-
from prettytable import PrettyTable

from RastrWinLib.AstraRastr import RASTR, WithEvents
from RastrWinLib.Templates import directory_shabl


def load_file(rastr_win=RASTR,
              rg_kod: int = 1,
              path_file: str = None,
              shabl: str = None,
              switch_command_line: bool = False):
    """
    Загружает файл данных name в рабочую область в соответствии с шаблоном типа shabl.
    Если поле shabl пусто, то загружается name без шаблона, если пусто поле name, то загружается только шаблон.

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

    :param shabl: шаблон RastrWin3 для загрузки;
    :param path_file: абсолютный путь с именем файла (пример:C:\\Folder\\ДРМ.rst);
    :param switch_command_line: True/False - выводит сообщения в протокол;
    :return: True
    """
    rastr_win.Load(rg_kod, path_file, directory_shabl(rus_name_shabl=shabl))
    rastr_win.Load(1, '', directory_shabl(rus_name_shabl='автоматика'))

    if switch_command_line:
        pt = PrettyTable()
        pt.title = 'Загружаен файл данных в рабочую область RastrWin3'
        pt.field_names = ['Файл', 'Шаблон']
        pt.add_row([path_file, shabl])
        print(pt)


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR, WithEvents

    load_file(rastr_win=RASTR, path_file='', shabl='режим')
    load_file(rastr_win=RASTR, path_file='', shabl='динамика')
