# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Load import load_file
from RastrWinLib.Load.shablon import Shabl
from RastrWinLib.Tables.Vetv.vetv import Vetv
from RastrWinLib.operation.Get import GettingParameter
from RastrWinLib.Tools.timer import timethis


def percentage_of_coincidence_two_str(string_one, string_two, print_results=False):
    string_one = string_one.lower()
    string_two = string_two.lower()
    str_one = string_one.split(" ")
    str_two = string_two.split(" ")

    percent = 100
    percent_of_one_string = percent / len(str_one)
    for index, i in enumerate(str_one):
        if i in str_two:

            if print_results:
                print(f'{index + 1}.Percent = {round(percent)}')
        else:
            percent -= percent_of_one_string
            if print_results:
                print(f'{index + 1}.Percent = {round(percent)}')
    return round(percent)


@timethis
def filling_list_of_data(table, column, rastr_win):
    list_ = []
    getting_parameter_obj = GettingParameter(rastr_win=rastr_win)
    count = getting_parameter_obj.get_count_table(table)
    print(f'count={count}')
    print(f"Количество строк в таблице {table}: {count}")
    for i in range(count):
        char = getting_parameter_obj.get_cell_row(table=table,
                                                  column=column,
                                                  row_id=i)
        list_.append(char)
    return list_


# load - SMZU
load_file(rastr_win=RASTR,
          file_path=r'C:\Users\Ohrimenko_AG\Desktop\BARS\smzu_mega.mptsmz',
          shabl=Shabl.without_shabl,
          switch_command_line=True)

name_smzu = filling_list_of_data(table=Vetv.table,
                                 column=Vetv.name,
                                 rastr_win=RASTR)

str_1 = 'Трубино 500 кВ - Владимирская 500'

for s in name_smzu:
    x = percentage_of_coincidence_two_str(string_one=str_1, string_two=s, print_results=False)
    if x > 60:
        print(f'{x} -> {s}')
