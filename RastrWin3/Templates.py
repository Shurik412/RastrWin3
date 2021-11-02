# -*- coding: utf-8 -*-
# from pathology.Path import script_dir
import pathlib
from os import path


class NameShablon:
    russian_names = {
        'режим': 'режим.rg2',
        'динамика': 'динамика.rst',
        'траектория утяжеления': 'траектория утяжеления.ut2',
        'сценарий': 'сценарий.scn',
        'автоматика': 'автоматика.dfw',
        'сечения': 'сечения.sch',
        'мегаточка': 'мегаточка.mpt',
    }


class ROOT_DIR_SHABLON:
    """ключи для выбора локации используемых файлов для загрузки шаблона"""
    LOCATION_SCRIPT = 'location_script'
    LOCATION_FOLDER_DOCUMENTS = 'location_folder_documents'
    LOCATION_ROOT_FOLDER_RASTR = 'location_root_folder_rastr'

    DOCUMENTS = path.expanduser('~\\Documents\\RastrWin3\\SHABLON')
    LOCAL = f'{pathlib.Path(__file__).parent.resolve()}\\Tools\\SHABLON'
    RASTR_WIN = r'C:\Program Files\RastrWin3\RastrWin3\SHABLON'


def directory_shabl(rus_name_shabl: str, location_of_files: str = ROOT_DIR_SHABLON.LOCATION_FOLDER_DOCUMENTS) -> str:
    """

    :param rus_name_shabl:
    :param location_of_files:
    :return: директорию к файлу Шаблона.
    """
    key_ = rus_name_shabl.lower()
    if key_ == '' or key_ == ' ' or key_ == " " or key_ == "":
        full_dir = ''
        return full_dir
    else:
        try:
            if location_of_files == ROOT_DIR_SHABLON.LOCATION_SCRIPT:
                full_dir = f'{ROOT_DIR_SHABLON.LOCAL}\\{NameShablon.russian_names[key_]}'
            elif location_of_files == ROOT_DIR_SHABLON.LOCATION_FOLDER_DOCUMENTS:
                full_dir = f'{ROOT_DIR_SHABLON.DOCUMENTS}\\{NameShablon.russian_names[key_]}'
            elif location_of_files == ROOT_DIR_SHABLON.LOCATION_ROOT_FOLDER_RASTR:
                full_dir = f'{ROOT_DIR_SHABLON.RASTR_WIN}\\{NameShablon.russian_names[key_]}'
            else:
                full_dir = f'{ROOT_DIR_SHABLON.LOCAL}\\{NameShablon.russian_names[key_]}'
        except KeyError:
            name_shabl_list = [key for key in NameShablon.russian_names.keys()]
            input_load_without_shabl = input(f'Введите:\n'
                                             f' - "Y" или "y" если хотите загрузить файл без шаблона.\n '
                                             f' - одно из названий шаблона:\n'
                                             f' {name_shabl_list}\n'
                                             f'=>  ')
            if input_load_without_shabl == "Y" or input_load_without_shabl == "y":
                full_dir = ''
                return full_dir
            elif input_load_without_shabl in name_shabl_list:
                if location_of_files == ROOT_DIR_SHABLON.LOCATION_SCRIPT:
                    full_dir = f'{ROOT_DIR_SHABLON.LOCAL}\\{NameShablon.russian_names[key_]}'
                    return full_dir
                elif location_of_files == ROOT_DIR_SHABLON.LOCATION_FOLDER_DOCUMENTS:
                    full_dir = f'{ROOT_DIR_SHABLON.DOCUMENTS}\\{NameShablon.russian_names[key_]}'
                    return full_dir
                elif location_of_files == ROOT_DIR_SHABLON.LOCATION_ROOT_FOLDER_RASTR:
                    full_dir = f'{ROOT_DIR_SHABLON.RASTR_WIN}\\{NameShablon.russian_names[key_]}'
                    return full_dir
        else:
            return full_dir
