# -*- coding: utf-8 -*-
import pandas as pd
import time
from win32com.client import Dispatch, WithEvents
from icecream import ic

def changing_number_of_semicolons(number, digits=0):
    try:
        return f"{number:.{digits}f}"
    except TypeError:
        return number


# dt_dyn = pd.read_excel("Дин_набор ДРМ х64 (08.11.21).xlsm", sheet_name='Дин Набор')
# df_dyn = pd.DataFrame(dt_dyn, columns=["Станция",
#                                        "Модель генератора",
#                                        "Pном  (генер-а),  МВт",
#                                        "Uг ном, кВ (для модели)",
#                                        "CosF",
#                                        "K демпф.",
#                                        "Tj агрегата (приведенная к S), [МВт*с/МВА]",
#                                        "X`d",
#                                        "Xd"])


# print(type(df[df["Станция"] == i]["Tj агрегата (приведенная к S), [МВт*с/МВА]"].to_list()[0]))


def search_value(data_frame, col_search_name: str, search_name: str, column_name: str):
    return data_frame[data_frame[col_search_name] == search_name][column_name].to_list()[0]


list_ = ["Криворожская ТЭС - Г-1", "Криворожская ТЭС - Г-10", "Криворожская ТЭС - Г-2", "Криворожская ТЭС - Г-3",
         "Криворожская ТЭС - Г-4", "Криворожская ТЭС - Г-5", "Криворожская ТЭС - Г-6", "Криворожская ТЭС - Г-7",
         "Криворожская ТЭС - Г-8", "Криворожская ТЭС - Г-9"]

list_cols = ["Модель генератора",
             "Pном  (генер-а),  МВт",
             "Uг ном, кВ (для модели)",
             "CosF",
             "K демпф.",
             "Tj агрегата (приведенная к S), [МВт*с/МВА]",
             "X`d",
             "Xd"]


# print(df_dyn.columns)
# start = time.time()
# for i in list_:
#     for j in list_cols:
#         print(search_value(data_frame=df_dyn, col_search_name="Станция", search_name=i, column_name=j))
# end = time.time()
# print(f'Время работы: {changing_number_of_semicolons(number=(end - start), digits=8)} сек.')


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


# RASTR_1 = Dispatch('Astra.Rastr')
# WithEvents(RASTR_1, RastrEvents)
#
# SHABLON_RG2 = r'C:\Program Files\RastrWin3\RastrWin3\SHABLON\режим.rg2'
# RASTR_1.Load(1, 'БРМ лето 2021 МАКСИМУМ_7.rg2', SHABLON_RG2)
# RASTR_1.Tables("vetv").WriteCSV(1, "vetv.csv", "tip,name,r,x,b,dname", ";")


dt_csv = pd.read_csv("vetv.csv", encoding="windows-1251", header=None, sep='\n')
#
# df = pd.DataFrame(dt_csv)
dt_csv = dt_csv[0].str.split(';', expand=True)

df = pd.DataFrame(dt_csv)
# df.to_excel(excel_writer='vetv.xlsx')
# ic(df)
df.columns = ["tip", "name", "r", "x", "b", "dname", "id"]
ic(df)
# df.to_excel(excel_writer='vetv.xlsx')
# ic(df.tip[df.tip == 'ЛЭП'].column('name'))

df_filter = df['dname'].isin(['ПС 220 кВ Правобережная АТ-3  ', 'ПС 220 кВ Правобережная АТ-3  РПН '])
ic(df[df_filter]['dname'])
