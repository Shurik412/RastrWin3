# -*- coding: utf-8 -*-
from os import path

dict_shablon_name = {
    'режим': 'режим.rg2',
    'динамика': 'динамика.rst',
    'траектория утяжеления': 'траектория утяжеления.ut2',
    'сценарий': 'сценарий.scn',
    'автоматика': 'автоматика.dfw',
    'сечения': 'сечения.sch',
    'мегаточка': 'мегаточка.mpt',
}

ROOT_DIR_RASTR_WIN_SHABLON = path.expanduser('~\\Documents\\RastrWin3\\SHABLON')


def directory_shabl(rus_name_shabl: str) -> str:
    key_ = rus_name_shabl.lower()
    if key_ == '' or key_ == ' ' or key_ == " " or key_ == "":
        full_dir = ''
        return full_dir
    else:
        try:
            full_dir = f'{ROOT_DIR_RASTR_WIN_SHABLON}\\{dict_shablon_name[key_]}'
        except KeyError:
            name_shabl_list = [key for key in dict_shablon_name.keys()]
            input_load_without_shabl = input(f'Введите:\n'
                                             f' - "Y" если хотите загрузить файл без шаблона.\n '
                                             f' - одно из названий шаблона:\n'
                                             f' {name_shabl_list}\n')

            if input_load_without_shabl == "Y":
                full_dir = ''
                return full_dir
            elif input_load_without_shabl in name_shabl_list:
                full_dir = f'{ROOT_DIR_RASTR_WIN_SHABLON}\\{dict_shablon_name[input_load_without_shabl]}'
                return full_dir
        else:
            return full_dir
