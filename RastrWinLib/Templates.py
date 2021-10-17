# -*- coding: utf-8 -*-
from os import path

REGIME = 'режим.rg2'
DYNAMIC = 'динамика.rst'
UT_COMMON = 'траектория утяжеления.ut2'
SCENARIO = 'сценарий.scn'
AUTOMATION = 'автоматика.dfw'
SECHEN = 'сечения.sch'
MEGA_MPT = 'мегаточка.mpt'

dict_shablon_name = {
    'режим': REGIME,
    'динамика': DYNAMIC,
    'траектория утяжеления': UT_COMMON,
    'сценарий': SCENARIO,
    'автоматика': AUTOMATION,
    'сечения': SECHEN,
    'мегаточка': MEGA_MPT,
}

ROOT_DIR_RASTR_WIN_SHABLON = path.expanduser('~\\Documents\\RastrWin3\\SHABLON')


def directory_shabl(rus_name_shabl: str):
    key_ = rus_name_shabl.lower()
    full_dir = f'{ROOT_DIR_RASTR_WIN_SHABLON}\\{dict_shablon_name[key_]}'
    return full_dir


if __name__ == '__main__':
    print(directory_shabl(rus_name_shabl='рЕжИм'))
