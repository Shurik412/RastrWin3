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


def directory_shabl(rus_name_shabl: str):
    key_ = rus_name_shabl.lower()
    if key_ == '' or key_ == ' ' or key_ == " ":
        full_dir = ''
    else:
        full_dir = f'{ROOT_DIR_RASTR_WIN_SHABLON}\\{dict_shablon_name[key_]}'
    return full_dir

