# -*- coding: utf-8 -*-
import pythoncom
import pywintypes

from RastrWin3.AstraRastr import RASTR
from RastrWin3.Templates import directory_shabl
from RastrWin3.Tools.tools import TableOutput


def load_file(rastr_win=RASTR,
              rg_kod: int = 1,
              path_file: str = None,
              shabl: str = None,
              location_of_shabl_files: str = 'location_folder_documents',
              switch_command_line: bool = False) -> None:
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

    :param location_of_shabl_files: location_script - в корневой папку пакета;
                                    location_folder_documents - в корневой директории Мои документы (OS Windows);
                                    location_root_folder_rastr - в корневой директории RastrWin3;
                                    если параметр не задан то используется директория Мои документа;

    :param path_file: абсолютный путь с именем файла (пример:C:\\Folder\\ДРМ.rst);

    :param switch_command_line: True/False - выводит сообщения в протокол;

    :return: Noting
    """

    def load_(kod_rg: int = 1, pathFile: str = '', shablon=directory_shabl(rus_name_shabl='автоматика',
                                                                           location_of_files=location_of_shabl_files)):
        try:
            rastr_win.Load(kod_rg, pathFile, shablon)
        except pywintypes.com_error as er:
            hr, msg, exc, arg = er.args
            table_output = TableOutput(fieldName=['Сообщение'])
            table_output.row_add(message=[exc[2]])
            table_output.show(title_table=f'Ошибка при запуске функции: "{load_file.__name__}"')
            return False
        except pythoncom.com_error as error:
            hr, msg, exc, arg = error.args
            table_output = TableOutput(fieldName=['Сообщение'])
            table_output.row_add(message=[exc[2]])
            table_output.show(title_table=f'Ошибка при запуске функции: "{load_file.__name__}"')
            return False
        except ValueError as error:
            table_output = TableOutput(fieldName=['Сообщение'])
            table_output.row_add(message=[f'Тип аргумента "rg_kod" должен быть int а не "";\n {error}'])
            table_output.show(title_table=f'Ошибка при запуске функции: "{load_file.__name__}"')
            return False
        else:
            return True

    if shabl is None or shabl == '' or shabl == ' ':
        load = load_(kod_rg=rg_kod, pathFile=path_file, shablon='')
        if load:
            shabl = 'без шаблона'
            shabl_automation = directory_shabl(rus_name_shabl='автоматика',
                                               location_of_files=location_of_shabl_files)
            load_(kod_rg=1, pathFile='', shablon=shabl_automation)
            if switch_command_line:
                pt = TableOutput(fieldName=['Файл', 'Шаблон'])
                if path_file == '' or path_file == "" or path_file == ' ':
                    pt.add_row(["загружен только шаблон", shabl])
                else:
                    pt.add_row([path_file, shabl])
                pt.add_row(["загружен только шаблон", shabl_automation])
                pt.show(title_table='Загружаен файл данных в рабочую область RastrWin3')
    else:
        shabl_path_file = directory_shabl(rus_name_shabl=shabl,
                                          location_of_files=location_of_shabl_files)
        load = load_(kod_rg=rg_kod, pathFile=path_file, shablon=shabl_path_file)
        if load:
            shabl_automation = directory_shabl(rus_name_shabl='автоматика',
                                               location_of_files=location_of_shabl_files)
            load_(kod_rg=1, pathFile='', shablon=shabl_automation)
            if switch_command_line:
                pt = TableOutput(fieldName=['Файл', 'Шаблон'])
                if shabl_path_file == '':
                    shabl_path_file = 'без шаблона'
                if path_file == '' or path_file == "" or path_file == ' ':
                    pt.add_row(["загружен только шаблон", shabl_path_file])
                else:
                    pt.add_row([path_file, shabl_path_file])
                pt.add_row(["загружен только шаблон", shabl_automation])
                pt.show(title_table='Загружаен файл данных в рабочую область RastrWin3')
