# -*- coding: utf-8 -*-
import os
import shutil


def File_SEQ(dir_file_1, dir_file_2, number_regime, regime, Unom, PSS):
    dir_file_1 = dir_file_1 + '/' + 'SEQ.seq'
    for num in range(1, int(number_regime) + 1):
        file_2 = dir_file_2 + '/' + str(regime) + '_' + str(num) + '_' + str(PSS) + '_' + str(Unom) + 'kV' + '.seq'
        shutil.copyfile(dir_file_1, file_2)


def copy_file(dir_files_copy, name_file_one):
    folder = f'{dir_files_copy}\\New_BARS_SMZU'
    try:
        os.makedirs(folder)
    except OSError:
        print("Creation of the directory %s failed" % folder)
    else:
        print ("Successfully created the directory %s" % folder)

    for i in range(0, 24):
        if i < 10:
            file_two = f'{folder}\\0{i}_00_00.7z'
            print(file_two)
            shutil.copyfile(src=f'{dir_files_copy}\\{name_file_one}', dst=file_two)
        elif i > 9:
            file_two = f'{folder}\\{i}_00_00.7z'
            print(file_two)
            shutil.copyfile(src=f'{dir_files_copy}\\{name_file_one}', dst=file_two)


copy_file(dir_files_copy=r'C:\Users\Ohrimenko_AG\Desktop\СМЗУ - БАРС', name_file_one='08_30_32.7z')
