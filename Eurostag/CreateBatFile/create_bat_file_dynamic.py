# -*- coding: utf-8 -*-

ROOT_DIR_SAVE_FILE: str = r'C:\01_ZAGAES_ZimaMax'
DIR_EUROSTAG: str = r'C:\Eurostag44\Eurostag'
DIR_HOME_BAT: str = r'C:\01_ZAGAES_ZimaMax'
NAME_SEZON: str = 'ZimaMax'  # ((1) ZimaMax - Зима макс, (2) ZimaMin - Зима мин, (3) LetoMax - Лето макс, (4) LetoMax - Лето мин.
KEY_Y_N: str = 'N'  # Y - с PSS, N - без PSS
U_NOM = '500'  # номинальное напряжение в точке КЗ
NAME_DTA_FILE: str = '1'  # название dta файла
COUNT_REGIME: int = 4

if NAME_SEZON == 'ZimaMax':
    file = open(fr"{ROOT_DIR_SAVE_FILE}\Dyn_ZimaMax_dta_{NAME_DTA_FILE}_{KEY_Y_N}.bat", "w")
    file.write(f'set EUROSTAG={DIR_EUROSTAG}\nset EDITOR=%windir%\\system32\\notepad.exe\nset HOME={DIR_HOME_BAT}\n\n')
    for i in range(1, COUNT_REGIME+1):
        file.write(f'eustag_cpt -s 1_{i}_{KEY_Y_N}_{U_NOM}kV.seq {NAME_DTA_FILE}.dta 1_{i}.sav\n')
    file.write('pause')
    file.close()

elif NAME_SEZON == 'ZimaMin':
    file = open(fr"{ROOT_DIR_SAVE_FILE}\Dyn_ZimaMin_dta_{NAME_DTA_FILE}_{KEY_Y_N}.bat", "w")
    file.write(f'set EUROSTAG={DIR_EUROSTAG}\nset EDITOR=%windir%\\system32\\notepad.exe\nset HOME={DIR_HOME_BAT}\n')
    for i in range(1, COUNT_REGIME+1):
        file.write(f'eustag_cpt -s 2_{i}_{KEY_Y_N}_{U_NOM}kV.seq {NAME_DTA_FILE}.dta 2_{i}.sav\n')
    file.write('pause')
    file.close()

elif NAME_SEZON == 'LetoMax':
    file = open(fr"{ROOT_DIR_SAVE_FILE}\Dyn_LetoMax_dta_{NAME_DTA_FILE}_{KEY_Y_N}.bat", "w")
    file.write(f'set EUROSTAG={DIR_EUROSTAG}\nset EDITOR=%windir%\\system32\\notepad.exe\nset HOME={DIR_HOME_BAT}\n')
    for i in range(1, COUNT_REGIME+1):
        file.write(f'eustag_cpt -s 3_{i}_{KEY_Y_N}_{U_NOM}kV.seq {NAME_DTA_FILE}.dta 3_{i}.sav\n')
    file.write('pause')
    file.close()

elif NAME_SEZON == 'LetoMin':
    file = open(fr"{ROOT_DIR_SAVE_FILE}\Dyn_LetoMin_dta_{NAME_DTA_FILE}_{KEY_Y_N}.bat", "w")
    file.write(f'set EUROSTAG={DIR_EUROSTAG}\nset EDITOR=%windir%\\system32\\notepad.exe\nset HOME={DIR_HOME_BAT}\n')
    for i in range(1, COUNT_REGIME+1):
        file.write(f'eustag_cpt -s 4_{i}_{KEY_Y_N}_{U_NOM}kV.seq {NAME_DTA_FILE}.dta 4_{i}.sav\n')
    file.write('pause')
    file.close()

print('The End')
