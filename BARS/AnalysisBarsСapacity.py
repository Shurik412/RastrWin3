# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.operation.get import GettingParameter
from RastrWinLib.Tables.area.area import Area
from RastrWinLib.Tables.Vetv.vetv import Vetv
from RastrWinLib.UploadResults.chart import Plot
from RastrWinLib.Load import load_file
from csv import reader, writer
from os import mkdir
from RastrWinLib.Tools.directory_rastrwin.defines_file_extensions import file_extensions
import os
from icecream import ic
import pandas
from os import listdir
from os.path import isfile, join
from icecream import ic
from RastrWinLib.UploadResults.chart import Plot

dict_name_area2_pdg = [['ЯРОСЛАВЛЬ', 999], ['ТУЛА', 998], ['ТВЕРЬ', 997],
                       ['ТАМБОВ (без учета 5980 ПС 220 кВ Давыдовская)', 996], ['СМОЛЕНСК', 995],
                       ['РЯЗАНЬ', 994], ['ОРЕЛ', 993], ['МОСКВА', 992], ['ЛИПЕЦК', 991],
                       ['КУРСК', 990], ['КОСТРОМА', 989], ['КАЛУГА (без учета 5742 ПС 220 кВ Метзавод)', 988],
                       ['ИВАНОВО', 987], ['ВОРОНЕЖ', 986], ['ВОЛОГДА', 985], ['ВЛАДИМИР', 984], ['БРЯНСК', 983],
                       ['БЕЛГОРОД', 982], ]

POINT_START = 25
POINT_END = 49
NAME_FOLDER_PDG = 'Файлы CSV Территории ПДГ'
NAME_FOLDER_SMZU = 'Файлы CSV Территории СМЗУ'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
input_file_name = input("Введите название файла: (пример -> 171021): ")

if input_file_name == '':
    file_name, file_extension = file_extensions(path_file=ROOT_PATH, extensions='.mpt')
    file_mpt = f'{ROOT_PATH}/{file_name}{file_extension}'
else:
    file_name = input_file_name + '.mpt'
    file_mpt = f'{ROOT_PATH}/{file_name}'


def create_table_area(list_, na: int, name: str, pn: float, pg: float) -> None:
    name_ = name.split()
    name_sj = ' '.join(name_)

    dict_ = {
        Area.na: na,
        Area.name: name_sj,
        Area.pn: pn,
        Area.pg: pg
    }
    list_.append(dict_)


def create_csv(name_file_csv: str, path: str, folder_name: str) -> None:
    print(f'Выбран файл: {path}')
    get = GettingParameter()
    for point in range(POINT_START, POINT_END):
        RASTR.ReadPnt(point)
        list_ = []
        count = RASTR.Tables("area2").Count
        for index in range(0, count - 1):
            na = get.get_cell_row(table="area2", column="npa", row_id=index)
            name = get.get_cell_row(table="area2", column="name", row_id=index)
            pn = get.get_cell_row(table="area2", column="pn", row_id=index)
            pg = get.get_cell_row(table="area2", column="pg", row_id=index)
            create_table_area(list_, na, name, pn, pg)
        data = pandas.DataFrame(list_)
        try:
            if not os.path.exists(folder_name):
                mkdir(folder_name)
        except FileExistsError:
            print("Каталог уже существует!")
        except PermissionError:
            print("Отсутствуют права на доступ к каталогу!")

        fullname = f'{path}/{folder_name}/{name_file_csv}_{point}.csv'
        # print(fullname)
        data.to_csv(fullname, sep=';')
        list_.clear()


def create_csv_PDG(name_file=ROOT_PATH, name_file_csv='Area2_PDG', folder_name=NAME_FOLDER_PDG):
    load_file(path_file=file_mpt, shabl='мегаточка')
    create_csv(name_file_csv=name_file_csv, path=name_file, folder_name=folder_name)
    load_file(path_file='', shabl='мегаточка')


def create_csv_SMZU(name_file=ROOT_PATH, name_file_csv='Area2_SMZU', folder_name=NAME_FOLDER_SMZU):
    load_file(path_file=f'{name_file}/smzu_mega_XML_UR_MDP.mptsmz', shabl='мегаточка')
    create_csv(name_file_csv=name_file_csv, path=name_file, folder_name=folder_name)
    load_file(path_file='', shabl='мегаточка')


def plot(title_chart: str, path: str, name_file_csv: str,
         folder_name_prg: str, folder_name_smzu: str) -> None:
    plt = Plot(title=title_chart,
               x_major_locator=1, x_minor_locator=1,
               enable_axis_x_fission_regulation=True,
               y_major_locator=5, y_minor_locator=5)
    list_prg_y = []
    list_prg_x = []
    list_smzu_x = []
    list_smzu_y = []
    for point in range(POINT_START, POINT_END):
        file = f'{path}/{folder_name_prg}/{name_file_csv}_{point}.csv'
        pd = pandas.read_csv(file, sep=';')
        data = pd.to_dict()
        list_prg_y.append(data["pn"][10])
        list_prg_x.append(point)

    plt.settings_plot(axis_y=list_prg_y,
                      axis_x=list_prg_x,
                      line_width=2,
                      line_color='red',
                      line_name_legend='ПРГ')

    for point in range(POINT_START, POINT_END):
        file_ = f'{path}/{folder_name_smzu}/{name_file_csv}_{point}.csv'
        pd = pandas.read_csv(file_, sep=';')
        data = pd.to_dict()
        list_smzu_y.append(data["pn"][10])
        list_smzu_x.append(point)

    plt.settings_plot(axis_y=list_smzu_y,
                      axis_x=list_smzu_x,
                      line_color='blue',
                      line_width=2,
                      line_name_legend='СМЗУ')
    plt.show_plot()

    list_y.clear()
    list_x.clear()


create_csv_PDG(name_file=ROOT_PATH,
               name_file_csv='Area2_PDG', folder_name='Файлы CSV Территории ПДГ')

create_csv_SMZU(name_file=ROOT_PATH,
                name_file_csv='Area2_SMZU', folder_name='Файлы CSV Территории СМЗУ')

plot(title_chart='График', path=ROOT_PATH,
     folder_name_prg='Файлы CSV Территории ПДГ',
     folder_name_smzu='Файлы CSV Территории СМЗУ',
     name_file_csv='Area2_PDG')
