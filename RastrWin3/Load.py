# -*- coding: utf-8 -*-
import pythoncom
import pywintypes

from RastrWin3.AstraRastr import RASTR
from RastrWin3.Templates import ROOT_DIR_SHABLON
from RastrWin3.Tools.tools import TableOutput


class LoadFile(TableOutput, ROOT_DIR_SHABLON):
    """Загружает файл данных в рабочую область в соответствии с шаблоном"""

    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line: bool = False):
        """
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param switch_command_line: True/False - выводит сообщения в протокол;
        """
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line
        self.field_name = ['Файл', 'Шаблон']
        super().__init__(fieldName=self.field_name)

    def __bool__(self):
        return self.switch_command_line

    def load(self,
             kod_rg: int = 1,
             path_file: str = '',
             name_shabl_russian: str = 'автоматика',
             location_of_files: str = ROOT_DIR_SHABLON.LOCATION_FOLDER_DOCUMENTS) -> None:
        """
        Загружает файл данных path_file в рабочую область в соответствии с шаблоном типа name_shabl_russian.
        Если поле name_shabl_russian пусто, то загружается name без шаблона, если пусто поле name, то загружается только шаблон.

        :param kod_rg: числовое значение, определяет режим загрузки при наличии таблицы в рабочей области и может быть одним из следующих:

            Константа   Значение           Описание

            RG_ADD          0       Таблица добавляется к имеющейся в рабочей области, совпадение ключевых полей не
                                     контролируются (соответствует режиму «Присоединить» в меню);
            RG_REPL         1       Таблица в рабочей области замещается (соответствует режиму «Загрузить» в меню);
            RG_KEY          2       Данные в таблице, имеющие одинаковые ключевые поля, заменяются. Если ключ не
                                     найден, то данные игнорируются (соответствует режиму «Обновить» в меню);
            RG_ADDKEY       3       Данные в таблице, имеющие одинаковые ключевые поля, заменяются.
                                    Если ключ не найден, то данные вставляются (соответствует режиму «Объединить»);

        :param path_file: абсолютный путь с именем файла (пример:C:\\Folder\\ДРМ.rst);

        :param name_shabl_russian: шаблон RastrWin3 для загрузки пример: "режим", "динамика", "сценарий";

        :param location_of_files: location_script - в корневой папку пакета;
                                  location_folder_documents - в корневой директории Мои документы (OS Windows);
                                  location_root_folder_rastr - в корневой директории RastrWin3;
                                  если параметр не задан то используется директория Мои документа;
        :return: Noting;
        """
        directory_shabl = self.directory_shabl(russian_name_shabl=name_shabl_russian,
                                               location_of_files=location_of_files)
        try:
            if name_shabl_russian == 'динамика':
                self.rastr_win.Load(kod_rg, path_file, directory_shabl)

                directory_shabl_auto = self.directory_shabl(russian_name_shabl='автоматика',
                                                            location_of_files=location_of_files)
                self.rastr_win.Load(kod_rg, '', directory_shabl_auto)
                self.information_output(shabl_path_file=directory_shabl_auto,
                                        path_file='')
            else:
                self.rastr_win.Load(kod_rg, path_file, directory_shabl)
        except pywintypes.com_error as er:
            hr, msg, exc, arg = er.args
            table_output_error = TableOutput(fieldName=['Сообщение'])
            table_output_error.row_add(message=[exc[2]])
            table_output_error.show(title_table=f'Ошибка при запуске функции: "{load.__name__}"')

        except pythoncom.com_error as error:
            hr, msg, exc, arg = error.args
            table_output_error = TableOutput(fieldName=['Сообщение'])
            table_output_error.row_add(message=[exc[2]])
            table_output_error.show(title_table=f'Ошибка при запуске функции: "{load.__name__}"')

        except ValueError as error:
            table_output_error = TableOutput(fieldName=['Сообщение'])
            table_output_error.row_add(message=[f'Тип аргумента "rg_kod" должен быть int а не "";\n {error}'])
            table_output_error.show(title_table=f'Ошибка при запуске функции: "{load.__name__}"')

        else:
            if self.switch_command_line:
                self.information_output(shabl_path_file=directory_shabl,
                                        path_file=path_file)

    def information_output(self, shabl_path_file: str, path_file: str) -> None:
        pt = TableOutput(fieldName=self.field_name)
        if shabl_path_file == '':
            shabl_path_file = 'без шаблона'
        if path_file == '' or path_file == "" or path_file == ' ':
            pt.add_row(["загружен только шаблон", shabl_path_file])
        else:
            pt.add_row([path_file, shabl_path_file])
        pt.show(title_table='Загружаен файл данных в рабочую область RastrWin3')
