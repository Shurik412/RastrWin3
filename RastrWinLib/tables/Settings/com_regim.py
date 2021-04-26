# -*- coding: utf-8 -*-
# Модуль переменных таблицы параметров "Режим" RastrWin3

table = 'com_regim'

neb_p: str = 'neb_p'  # Точность расчета (dP)
it_max: str = 'it_max'  # Максимальное число итераций (It)
start: str = 'start'  # Стартовый алгоритм (Start)
flot: str = 'flot'  # Плоский старт (Пл.старт)
dv_min: str = 'dv_min'  # Мин. допустимое снижение V (dV-)
dv_max: str = 'dv_max'  # Макс. допустимое превышение V (dV+)
dd_max: str = 'dd_max'  # Макс. допустимый угол по связи (dDelta)
status: str = 'status'  # Состояние расчета режима (Статус)
rr: str = 'rr'  # Учет частоты: (W)
wt: str = 'wt'  # Отклонение частоты (dF)
gen_p: str = 'gen_p'  # Пересчитывать P/Q узла по P ген (Ген->P)
method: str = 'method'  # Метод Расчета (Метод)
method_ogr: str = 'method_ogr'  # Метод учета ограничений Q (Метод учета ограничений Q)
print_mode: str = 'print_mode'  # Уровень печати (Печать)
qmax: str = 'qmax'  # Точный метод расчета Qmax (Qmax)
min_x: str = 'min_x'  # Сопротивление выключателя (ое на 10-6) (Min_X)
calc_tr: str = 'calc_tr'  # Пересчет АТ/3х обм. трансформаторов (Транс.)
nag_p: str = 'nag_p'  # Пересчитывать (P/Q) нагрузки узла по ВРДО (Наг->P)
rem_breaker: str = 'rem_breaker'  # Удаление выключателей из схемы: (Выкл)
gram: str = 'gram'  # Пересчет мощности генератора по ГРАМ: (Грам)
ctrl_baza: str = 'ctrl_baza'  # Автоматическое создание БУ (БУ)
itz: str = 'itz'  # Стартовый метод: число итераций (Z_it)
itz_ogr_max: str = 'itz_ogr_max'  # Стартовый метод: Учет Qmax с итерации (Z_it_max)
itz_ogr_min: str = 'itz_ogr_min'  # Стартовый метод: Учет Qmin с итерации (Z_it_min)
min_nodes_in_island: str = 'min_nodes_in_island'  # Минимальное число узлов в острове (Min_nodes)

com_regim_table = 'com_regim'
com_regim_attributes_list = ['neb_p', 'it_max', 'start', 'flot', 'dv_min', 'dv_max', 'dd_max', 'status', 'rr', 'wt',
                             'gen_p', 'method', 'method_ogr', 'print_mode', 'qmax', 'min_x', 'calc_tr', 'nag_p',
                             'rem_breaker', 'gram', 'ctrl_baza', 'itz', 'itz_ogr_max', 'itz_ogr_min',
                             'min_nodes_in_island', ]
com_regim_attributes = {
    'neb_p': 'Точность расчета (dP)',
    'it_max': 'Максимальное число итераций (It)',
    'start': 'Стартовый алгоритм (Start)',
    'flot': 'Плоский старт (Пл.старт)',
    'dv_min': 'Мин. допустимое снижение V (dV-)',
    'dv_max': 'Макс. допустимое превышение V (dV+)',
    'dd_max': 'Макс. допустимый угол по связи (dDelta)',
    'status': 'Состояние расчета режима (Статус)',
    'rr': 'Учет частоты: (W)',
    'wt': 'Отклонение частоты (dF)',
    'gen_p': 'Пересчитывать P/Q узла по P ген (Ген->P)',
    'method': 'Метод Расчета (Метод)',
    'method_ogr': 'Метод учета ограничений Q (Метод учета ограничений Q)',
    'print_mode': 'Уровень печати (Печать)',
    'qmax': 'Точный метод расчета Qmax (Qmax)',
    'min_x': 'Сопротивление выключателя (ое на 10-6) (Min_X)',
    'calc_tr': 'Пересчет АТ/3х обм. трансформаторов (Транс.)',
    'nag_p': 'Пересчитывать (P/Q) нагрузки узла по ВРДО (Наг->P)',
    'rem_breaker': 'Удаление выключателей из схемы: (Выкл)',
    'gram': 'Пересчет мощности генератора по ГРАМ: (Грам)',
    'ctrl_baza': 'Автоматическое создание БУ (БУ)',
    'itz': 'Стартовый метод: число итераций (Z_it)',
    'itz_ogr_max': 'Стартовый метод: Учет Qmax с итерации (Z_it_max)',
    'itz_ogr_min': 'Стартовый метод: Учет Qmin с итерации (Z_it_min)',
    'min_nodes_in_island': 'Минимальное число узлов в острове (Min_nodes)'
}
