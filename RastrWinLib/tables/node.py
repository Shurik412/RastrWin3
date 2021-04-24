# -*- coding: utf-8 -*-
table: str = 'node'

sel: str = 'sel'  # отметка узла
sta: str = 'sta'  # состояние узла
tip: str = 'tip'  # тип узла
ny: str = 'ny'  # номер узла
name: str = 'name'  # название
nsx: str = 'nsx'  # номер СХН
na: str = 'na'  # район
npa: str = 'npa'  # территрория

# Проводимость
bsh: str = 'bsh'  # проводимость шунта
bshr: str = 'bshr'  # B_расч, Суммарная проводимость шунта

# Напряжение
vzd: str = 'vzd'  # V_зд, заданный модуль напряжения
uhom: str = 'uhom'  # Uном,номинальное напряжение
vras: str = 'vras'  # U, расчетный модуль напряжения
delta: str = 'delta'  # расчетный угол напряжения
umax: str = 'umax'  # максимальное заданое напряжение
umin: str = 'umin'  # минимальное заданое напряжение

# Q реактивная мощность
qn: str = 'qn'  # мощность нагрузки Q
qn_max: str = 'qn_max'  # Qнагр максимальное
qn_min: str = 'qn_min'  # Qнагр минимальное
nebal_q: str = 'nebal_q'  # небаланс
qg: str = 'qg'  # мощность генерации Q
qmin: str = 'qmin'  # минимальная генерация Q
qmax: str = 'qmax'  # максимальная генерация Q

# P активная мощность
pn: str = 'pn'  # мощность нагрузки Р
pn_max: str = 'pn_max'  # максимум нагрузки
pn_min: str = 'pn_min'  # минимум нагрузки
pg_max: str = 'pg_max'  # максимальная мощность Pg
pg_min: str = 'pg_min'  # минимальная мощность Pg
pg_nom: str = 'pg_nom'  # номинальная мощность Pg
nebal: str = 'nebal'  # небаланс Р
pg: str = 'pg'  # мощность генерации Р
