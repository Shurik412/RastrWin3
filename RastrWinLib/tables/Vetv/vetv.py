# -*- coding: utf-8 -*-
# Модуль переменных таблицы ветвей RastrWin3


class Vetv:
    table: str = 'vetv'  # название таблицы
    table_name: str = 'Ветви'  # название таблицы

    sel: str = 'sel'  # Отмеченная
    sta: str = 'sta'  # S, Cостояние ветви
    tip: str = 'tip'  # Тип, тип ветви
    name: str = 'name'  # Название
    ip: str = 'iq'  # N_нач, номер начала
    iq: str = 'iq'  # N_кон, номер конца
    np: str = 'np'  # N_п, номер параллельной
    groupid: str = 'groupid'  # ID Группы, принадлежность к группе одной линии
    na: str = 'na'  # Nа, Номер района по потерм
    Tc: str = 'Tc'  # Tc, Температура

    # R, X, B, k_tr параметры ветви
    r: str = 'r'  #
    x: str = 'x'  #
    b: str = 'b'  #
    g: str = 'g'  #
    z: str = 'z'  #
    ktr: str = 'ktr'  #
    n_anc: str = 'n_anc'  #
    bd: str = 'bd'  #

    # P активная мощность
    pl_ip: str = 'pl_ip'  # P_нач, Поток P начале ветви
    pl_iq: str = 'pl_iq'  # P_кон, Поток P в конце ветви
    plmax: str = 'plmax'  # максимальная мощность ветви
    dp: str = 'dp'  # dP, Потери P (продольные)
    dq: str = 'dq'  # dQ, Потери Q (продольные)

    # Q реактивная мощность
    ql_ip: str = 'ql_ip'  # Q_нач, Поток Q в начале ветви
    ql_iq: str = 'ql_iq'  # Q_кон, Поток Q в конце ветви

    # S полная мощность

    # I ток
    i_max: str = 'i_max'  # I max, Максимальный ток по элементу
    i_zag: str = 'i_zag'  # I загр., Загрузка элемента по току

    # U напряжение
    v_ip: str = 'v_ip'  # Vнач, Напряжение в начале ветви
    v_iq: str = 'v_iq'  # Vкон, Напряжение в конце ветви
