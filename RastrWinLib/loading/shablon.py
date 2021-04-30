# -*- coding: utf-8 -*-
from os import path


class Shabl:
    """

    """
    shablon_regime = 'режим.rg2'
    shablon_dynamic = 'динамика.rst'
    shablon_ut_common = 'траектория утяжеления.ut2'
    shablon_scenario = 'сценарий.scn'
    shablon_automation = 'автоматика.dfw'
    directory_file_shablon = path.expanduser('~\\Documents\\RastrWin3\\SHABLON')
    directory_file_test = path.expanduser('~\\Documents\\RastrWin3\\test-rastr')

    shablon_file_dynamic = f'{directory_file_shablon}\\{shablon_dynamic}'
    shablon_file_scenario = f'{directory_file_shablon}\\{shablon_scenario}'
    shablon_file_automation = f'{directory_file_shablon}\\{shablon_automation}'
    shablon_file_regime = f'{directory_file_shablon}\\{shablon_regime}'
    shablon_file_ut_common = f'{directory_file_shablon}\\{shablon_ut_common}'

    test_195_rg = f'{directory_file_test}\\cx195.rg2'
    test_9_rst = f'{directory_file_test}\\RUSTab\\test9.rst'
