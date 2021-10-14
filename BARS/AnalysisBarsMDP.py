# -*- coding: utf-8 -*-
import csv
from os import mkdir

import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv


# ROOT_PATH = os.getcwd()


def create_csv(path_read, path_save='ogrsech_new.csv'):
    list_one = []
    list_three = []
    with open(path_read, newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            list_one.append(row[0].split(sep=';'))
    for num in list_one:
        list_two = [num[0], num[1], num[2]]
        list_three.append(list_two)
    list_three.insert(0, ['sech', 'time', 'P'])

    with open(path_save, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for row in list_three:
            list_ = [row[0], row[1], row[2]]
            writer.writerow(list_)
    try:
        mkdir("file_bars_mdp_sech_csv")
    except FileExistsError:
        print("Каталог уже существует!")
    except PermissionError:
        print("Отсутствуют права на доступ к каталогу!")

    data = read_csv(path_save)
    data_sech_2 = data[data.sech == 2]
    data_sech_18 = data[data.sech == 18]
    data_sech_10 = data[data.sech == 10]
    data_sech_19 = data[data.sech == 19]

    update_sech_2 = data_sech_2.drop([data_sech_2.index[23]])
    update_sech_18 = data_sech_18.drop([data_sech_18.index[23]])
    update_sech_10 = data_sech_10.drop([data_sech_10.index[23]])
    update_sech_19 = data_sech_19.drop([data_sech_19.index[23]])

    update_sech_2.to_csv("file_bars_mdp_sech_csv/date_sech_2.csv")
    update_sech_18.to_csv("file_bars_mdp_sech_csv/date_sech_18.csv")
    update_sech_10.to_csv("file_bars_mdp_sech_csv/date_sech_10.csv")
    update_sech_19.to_csv("file_bars_mdp_sech_csv/date_sech_19.csv")


def plot():
    FILE_CSV = [
        "file_bars_mdp_sech_csv/date_sech_2.csv",
        "file_bars_mdp_sech_csv/date_sech_18.csv",
        "file_bars_mdp_sech_csv/date_sech_10.csv",
        "file_bars_mdp_sech_csv/date_sech_19.csv"
    ]

    dict_sech = {
        '2': "Воронежское-2 на Север",
        '18': "Воронежское-2 на Север (Статика)",
        '10': "Донское",
        '19': "Донское (Статика)",
    }

    data_sech_2 = read_csv(FILE_CSV[0])
    data_sech_18 = read_csv(FILE_CSV[1])
    data_sech_10 = read_csv(FILE_CSV[2])
    data_sech_19 = read_csv(FILE_CSV[3])

    data_sech_2_list_time = data_sech_2.time.to_list()
    data_sech_2_list_P = data_sech_2.P.to_list()

    data_sech_18_list_time = data_sech_18.time.to_list()
    data_sech_18_list_P = data_sech_18.P.to_list()

    data_sech_10_list_time = data_sech_10.time.to_list()
    data_sech_10_list_P = data_sech_10.P.to_list()

    data_sech_19_list_time = data_sech_19.time.to_list()
    data_sech_19_list_P = data_sech_19.P.to_list()

    sech_1_min = min([data_sech_2.P.min(), data_sech_18.P.min()])
    sech_2_min = min([data_sech_10.P.min(), data_sech_19.P.min()])
    ##############################
    fig, ax_1 = plt.subplots()
    fig, ax_4 = plt.subplots()

    ax_1.grid()
    ax_4.grid()

    ax_1.set_xlabel('Точка (час)')
    ax_1.set_ylabel('МДП (МВт)')

    ax_4.set_xlabel('Точка (час)')
    ax_4.set_ylabel('МДП (МВт)')

    ax_1.plot(data_sech_2.time,
              data_sech_2.P,
              linewidth=3,
              color='r',
              label=dict_sech[str(2)])

    ax_4.step(data_sech_2_list_time,
              data_sech_2_list_P,
              color="r",
              linewidth=3,
              where='post',
              label=dict_sech[str(2)])

    ax_1.plot(data_sech_18.time,
              data_sech_18.P,
              linewidth=1.5,
              color='b',
              label=dict_sech[str(18)])

    ax_4.step(data_sech_18_list_time,
              data_sech_18_list_P,
              color="b",
              linewidth=1.5,
              where='post',
              label=dict_sech[str(18)])

    ax_1.set_xlim([25, 48])
    ax_1.legend()
    ax_1.set_title(f'Анализ МДП => {sech_1_min} МВт')

    ax_4.set_xlim([25, 48])
    ax_4.legend()
    ax_4.set_title(f'Анализ МДП => {sech_1_min} МВт')

    plt.xticks(np.arange(25, 48, 1))
    ##############################
    fid, ax_2 = plt.subplots()
    fid, ax_3 = plt.subplots()

    ax_2.grid()
    ax_3.grid()

    ax_2.set_xlabel('Точка (час)')
    ax_2.set_ylabel('МДП (МВт)')

    ax_3.set_xlabel('Точка (час)')
    ax_3.set_ylabel('МДП (МВт)')

    ax_2.plot(data_sech_10.time, data_sech_10.P,
              linewidth=3,
              color="r",
              label=dict_sech[str(10)])

    ax_3.step(data_sech_10_list_time,
              data_sech_10_list_P,
              color="r",
              linewidth=3,
              where='post',
              label=dict_sech[str(10)])

    ax_2.plot(data_sech_19.time,
              data_sech_19.P,
              linewidth=1.5,
              color="b",
              label=dict_sech[str(19)])

    ax_3.step(data_sech_19_list_time,
              data_sech_19_list_P,
              linewidth=1.5,
              color="b",
              where='post',
              label=dict_sech[str(19)])

    ax_3.set_xlim([25, 48])
    ax_2.set_xlim([25, 48])

    ax_3.legend()
    ax_2.legend()

    ax_3.set_title(f"Анализ МДП => {sech_2_min} МВт")
    ax_2.set_title(f"Анализ МДП => {sech_2_min} МВт")
    ##############################
    plt.xticks(np.arange(25, 48, 1))
    plt.show()


create_csv(path_read='ogrsech.csv')
plot()
