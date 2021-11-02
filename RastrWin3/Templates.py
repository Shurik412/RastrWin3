# -*- coding: utf-8 -*-
# from pathology.Path import script_dir
import pathlib
from os import path


class Key_to_select_location:
    """Ключи для выбора локации"""
    LOCATION_SCRIPT = 'location_script'
    LOCATION_FOLDER_DOCUMENTS = 'location_folder_documents'
    LOCATION_ROOT_FOLDER_RASTR = 'location_root_folder_rastr'
    DOCUMENTS = path.expanduser('~\\Documents\\RastrWin3\\SHABLON')
    LOCAL = f'{pathlib.Path(__file__).parent.resolve()}\\Tools\\SHABLON'
    RASTR_WIN = r'C:\Program Files\RastrWin3\RastrWin3\SHABLON'
    dict_russian_names = {
        'режим': 'режим.rg2',
        'динамика': 'динамика.rst',
        'траектория утяжеления': 'траектория утяжеления.ut2',
        'сценарий': 'сценарий.scn',
        'автоматика': 'автоматика.dfw',
        'сечения': 'сечения.sch',
        'мегаточка': 'мегаточка.mpt',
    }


class ROOT_DIR_SHABLON(Key_to_select_location):
    """Ключи для выбора локации используемых файлов для загрузки шаблона"""

    def __init__(self):
        super().__init__()

    def directory_shabl(self,
                        russian_name_shabl: str,
                        location_of_files: str = Key_to_select_location.LOCATION_FOLDER_DOCUMENTS) -> str:
        """

        :param russian_name_shabl:
        :param location_of_files:
        :return:
        """
        russian_name_shabl_ = self.russian_names_shabl(name=russian_name_shabl)
        if russian_name_shabl_ != '':
            if location_of_files == Key_to_select_location.LOCATION_SCRIPT:
                full_dir = f'{Key_to_select_location.LOCAL}\\{russian_name_shabl_}'
            elif location_of_files == Key_to_select_location.LOCATION_FOLDER_DOCUMENTS:
                full_dir = f'{Key_to_select_location.DOCUMENTS}\\{russian_name_shabl_}'
            elif location_of_files == Key_to_select_location.LOCATION_ROOT_FOLDER_RASTR:
                full_dir = f'{Key_to_select_location.RASTR_WIN}\\{russian_name_shabl_}'
            else:
                full_dir = f'{Key_to_select_location.LOCAL}\\{russian_name_shabl_}'
            return full_dir
        else:
            full_dir = russian_name_shabl_
            return full_dir

    @staticmethod
    def russian_names_shabl(name):
        """

        :param name:
        :return:
        """

        key_ = name.lower()
        try:
            russian_name = Key_to_select_location.dict_russian_names[key_]
        except KeyError:
            names_shabl_list = [key for key in Key_to_select_location.dict_russian_names.keys()]
            input_load_without_shabl = input(f'Введите:\n'
                                             f' - "Y" или "y" если хотите загрузить файл без шаблона.\n '
                                             f' - одно из названий шаблона:\n'
                                             f' {names_shabl_list}\n'
                                             f'=>  ')
            if input_load_without_shabl == "Y" or input_load_without_shabl == "y":
                russian_name = ''
                return russian_name
            elif input_load_without_shabl in names_shabl_list:
                russian_name = Key_to_select_location.dict_russian_names[input_load_without_shabl]
                return russian_name
            else:
                russian_name = ''
                return russian_name
        else:
            return russian_name
