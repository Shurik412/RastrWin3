# -*- coding: utf-8 -*-
import pandas as pd
import time
from win32com.client import Dispatch, WithEvents
from icecream import ic
import os


class RastrEvents:
    """
    Метод Onprot - выводит сообщения написанные: rastr.Printp("Сообщение из Printp")\n
    Метод OnLog
    """

    def OnLog(self, code, level, id, name, index, description, formName):
        if code == 2:
            print('[Error]', description)
        elif code == 3:
            print('[Warning]', description)
        elif code == 4:
            print('[Lightbulb]', description)
        elif code == 5:
            print('[Info]', description)
        else:
            print([code, description])

    def Onprot(self, message):
        print(message)


RASTR = Dispatch('Astra.Rastr')
WithEvents(RASTR, RastrEvents)

SHABLON_RG2 = r'C:\Program Files\RastrWin3\RastrWin3\SHABLON\режим.rg2'
SHABLON_RST = r'C:\Program Files\RastrWin3\RastrWin3\SHABLON\динамика.rst'

FILE_PATH_RASTR = r'Зимний минимум 2027 минус 31.rst'


def dir_name(file: str):
    path_file = os.path.dirname(file)
    file_basename = os.path.basename(file)
    file_name, file_extension = os.path.splitext(file_basename)
    return path_file, file_name, file_extension


def corr_dname_vetv_model(FILE_PATH_RASTR: str, SHABLON: str):
    path_file, file_name, file_extension = dir_name(file=FILE_PATH_RASTR)
    RASTR.Load(1, FILE_PATH_RASTR, SHABLON)
    vetv = RASTR.Tables("vetv")
    for index_vetv in range(0, vetv.Count):
        dname_old = vetv.Cols("dname").Z(index_vetv)
        dname_old_split_ = dname_old.split()
        for index, i in enumerate(dname_old_split_):
            if "-" in i:
                i_ = i.split("-")
                _i = " - ".join(i_)
                dname_old_split_[index] = _i
                dname_new = " ".join(dname_old_split_)
        dname_new = " ".join(dname_old_split_)
        vetv.Cols("dname").SetZ(index_vetv, dname_new)
    # file_save = path_file + name_file + "" + file_extension
    file_save = FILE_PATH_RASTR
    RASTR.Save(rf'{file_save}', SHABLON)


def simile(dir_file_list: list, sh_list: list) -> None:
    RASTR1 = Dispatch('Astra.Rastr')
    WithEvents(RASTR1, RastrEvents)
    RASTR2 = Dispatch('Astra.Rastr')
    WithEvents(RASTR2, RastrEvents)
    RASTR1.Load(1, dir_file_list[0], sh_list[0])
    RASTR2.Load(1, dir_file_list[1], sh_list[1])
    vetv_1 = RASTR1.Tables("vetv")
    vetv_2 = RASTR2.Tables("vetv")
    counter = 0
    for i in range(0, vetv_1.Count):
        for j in range(0, vetv_2.Count):
            val1 = str(vetv_1.Cols('dname').Z(i))
            val2 = str(vetv_2.Cols('dname').Z(j))
            if val1 == val2:
                counter += 1
                print(f"{counter}.{val1} -> {val2}")
                break


def simile2(dir_file_list: list, sh_list: list):
    RASTR1 = Dispatch('Astra.Rastr')
    WithEvents(RASTR1, RastrEvents)
    RASTR2 = Dispatch('Astra.Rastr')
    WithEvents(RASTR2, RastrEvents)
    RASTR1.Load(1, dir_file_list[0], sh_list[0])
    RASTR2.Load(1, dir_file_list[1], sh_list[1])
    vetv_1 = RASTR1.Tables("vetv")
    vetv_2 = RASTR2.Tables("vetv")
    list1 = []
    list2 = []
    for i in range(0, vetv_1.Count):
        val1 = str(vetv_1.Cols('dname').Z(i))
        list1.append(val1)

    for j in range(0, vetv_2.Count):
        val2 = str(vetv_2.Cols('dname').Z(j))
        list2.append(val2)
    return list1, list2


dir_file_list = ['Зимний минимум 2027 минус 31.rst', 'БРМ лето 2021 МАКСИМУМ_7.rg2']
sh_list = [SHABLON_RST, SHABLON_RG2]

# for index, name_file in enumerate(dir_file_list):
#     corr_dname_vetv_model(name_file, sh_list[index])

# simile(dir_file_list, sh_list)
list_1, list_2 = simile2(dir_file_list, sh_list)

counter = 0
for i in list_1:
    if i != '' or i != '0':
        if i in list_2:
            counter += 1
            print(f'{counter}. {i} => {1}')