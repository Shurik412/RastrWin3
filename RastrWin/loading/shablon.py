# -*- coding: utf-8 -*-
from os import path

shablon_regime = 'режим.rg2'
shablon_dynamic = 'динамика.rst'
shablon_scenario = 'сценарий.scn'
shablon_automation = 'автоматика.dfw'
directory_file_shablon = path.expanduser('~\\Documents\\RastrWin\\SHABLON')
directory_file_test = path.expanduser('~\\Documents\\RastrWin\\test-rastr')

shablon_file_dynamic = f'{directory_file_shablon}\\{shablon_dynamic}'
shablon_file_scenario = f'{directory_file_shablon}\\{shablon_scenario}'
shablon_file_automation = f'{directory_file_shablon}\\{shablon_automation}'
shablon_file_regime = f'{directory_file_shablon}\\{shablon_regime}'

test_195_rg = f'{directory_file_test}\\cx195.rg2'
