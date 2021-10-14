# -*- coding: utf-8 -*-
import csv
from os import getcwd, mkdir
import numpy as np
import matplotlib.pyplot as plt
import pandas

ROOT_PATH = getcwd()


def create_csv(path_read, path_save='ogersech_new.csv'):
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

    data = pandas.read_csv(path_save)
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
        '2': "Воронежское-2 на Север (Ток)",
        '18': "Воронежское-2 на Север (Статика)",
        '10': "Донское (Ток)",
        '19': "Донское (Статика)",
    }

    data_sech_2 = pandas.read_csv(FILE_CSV[0])
    data_sech_18 = pandas.read_csv(FILE_CSV[1])
    data_sech_10 = pandas.read_csv(FILE_CSV[2])
    data_sech_19 = pandas.read_csv(FILE_CSV[3])

    print(f'Вор_2_2 = {data_sech_2.P.max()}')
    print(f'Вор_2_2 = {data_sech_2.P.min()}')
    print(f'Вор_2_18 = {data_sech_18.P.max()}')
    print(f'Вор_2_18 = {data_sech_18.P.min()}')

    class Plot:
        def __init__(self, sech_1, sech_2, num_sech_1, num_sech_2):
            super().__init__()
            self.sech_1 = sech_1
            self.sech_2 = sech_2
            self.num_sech_1 = num_sech_1
            self.num_sech_2 = num_sech_2
            self.ax = subplots()
            # self.ax.grid()

        def plot_graf(self):
            self.ax.set_xlabel('Точка (час)')
            self.ax.set_ylabel('МДП (МВт)')
            self.ax.plot(self.sech_1.time, self.sech_1.P,
                         linewidth=3,
                         color='r',
                         label=dict_sech[str(self.num_sech_1)])

            self.ax.plot(self.sech_2.time, self.sech_2.P,
                         linewidth=1.5,
                         color='b',
                         label=dict_sech[str(self.num_sech_2)])

            self.ax.legend()
            self.ax.set_title('Анализ МДП')
            plt.show()

    ##############################
    fig, ax_1 = plt.subplots()
    ax_1.grid()
    ax_1.set_xlabel('Точка (час)')
    ax_1.set_ylabel('МДП (МВт)')
    ax_1.plot(data_sech_2.time, data_sech_2.P,
              linewidth=3,
              color='r',
              label=dict_sech[str(2)])

    ax_1.plot(data_sech_18.time, data_sech_18.P,
              linewidth=1.5,
              color='b',
              label=dict_sech[str(18)])

    ax_1.set_xlim([25, 48])
    ax_1.legend()
    ax_1.set_title('Анализ МДП')
    plt.xticks(np.arange(25, 48, 1))
    ##############################
    fid, ax_2 = plt.subplots()
    ax_2.grid()
    ax_2.set_xlabel('Точка (час)')
    ax_2.set_ylabel('МДП (МВт)')
    ax_2.plot(data_sech_10.time, data_sech_10.P,
              linewidth=3,
              color='r',
              label=dict_sech[str(10)])

    ax_2.plot(data_sech_19.time, data_sech_19.P,
              linewidth=1.5,
              color='b',
              label=dict_sech[str(19)])

    ax_2.set_xlim([25, 48])
    # ax_2.xticks([25,26,27,28,29,30, 48])
    ax_2.legend()
    ax_2.set_title('Анализ МДП')

    ##############################
    plt.xticks(np.arange(25, 48, 1))
    plt.show()


create_csv(path_read='ogrsech123.csv')
plot()
