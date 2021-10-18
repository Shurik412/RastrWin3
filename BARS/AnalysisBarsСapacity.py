# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.ActionsObject.Get import GettingParameter
from RastrWinLib.Tables.area.area import Area
from RastrWinLib.Tables.Vetv.vetv import Vetv
from RastrWinLib.Load import load_file
from csv import reader, writer
from os import mkdir
import os
import pandas
from icecream import ic
from RastrWinLib.UploadResults.chart import Plot

dict_name_area_pdg = [['Московская ЭС', 9], ['Тверская ЭС', 15], ['Костромская ЭС', 14],
                      ['Ярославская ЭС', 13], ['Владимирская ЭС', 12], ['Ивановская ЭC', 11],
                      ['Вологодская ЭС', 24], ['Смоленская область', 518], ['Тульская область', 511],
                      ['Брянская область', 519], ['Орловская область', 521], ['Курская область', 523],
                      ['Липецкая область', 524], ['Воронежская область', 526], ['Белгородская область', 527],
                      ['Тамбовская область', 528], ['Рязанская область', 531], ['Калужская область', 532], ]


def create_table_area(list_, na: int, name: str, pn: float, pg: float) -> None:
    dict_ = {
        Area.na: na,
        Area.name: name,
        Area.pn: pn,
        Area.pg: pg
    }
    list_.append(dict_)


PATH_NAME_FILE_PDG = r'U:\ODU_DIR\СЭР\Анализ МДП\171021\171021-17.mpt'
PATH_NAME_FILE_SMZU = '171021-17.mpt'

# load_file(path_file=PATH_NAME_FILE_PDG, shabl='мегаточка')


def create_csv():
    get = GettingParameter()
    for point in range(25, 49):
        RASTR.ReadPnt(point)
        list_ = []
        count = RASTR.Tables(Area.table).Count - 1
        for index in range(1, count):
            na = get.get_cell_row(table=Area.table, column=Area.na, row_id=index)
            name = get.get_cell_row(table=Area.table, column=Area.name, row_id=index)
            pn = get.get_cell_row(table=Area.table, column=Area.pn, row_id=index)
            pg = get.get_cell_row(table=Area.table, column=Area.pg, row_id=index)
            create_table_area(list_, na, name, pn, pg)

        data = pandas.DataFrame(list_)
        try:
            mkdir("file_bars_mdp_sech_csv")
        except FileExistsError:
            print("Каталог уже существует!")
        except PermissionError:
            print("Отсутствуют права на доступ к каталогу!")

        data.to_csv(path_or_buf=rf'{os.path.abspath(PATH_FILE_PDG)}\file_bars_csv\area_{point}.csv', sep=';')
        list_.clear()


# create_csv()

data2 = pandas.read_csv(filepath_or_buffer=rf'{os.path.dirname(PATH_NAME_FILE_PDG)}\PDG\area_1.csv', sep=';')
print(data2[data2.name == 'Москва      '])
