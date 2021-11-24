# -*- coding: utf-8 -*-
# Модуль переменных таблицы "Генераторы" RastrWin3

class Generator:
    """

    """
    table = 'Generator'
    table_name: str = '"Генераторы(ИД)"'
    sel: str = 'sel'  #
    sta: str = 'sta'  #
    sta0: str = 'sta0'  #
    Num: str = 'Num'  #
    Name: str = 'Name'  #
    Node: str = 'Node'  #
    ModelType: str = 'ModelType'  #
    Brand: str = 'Brand'  #
    NumBrand: str = 'NumBrand'  #
    ExciterId: str = 'ExciterId'  #
    ARSId: str = 'ARSId'  #
    IVActuatorId: str = 'IVActuatorId'  #
    NumPQ: str = 'NumPQ'  #
    NumSat: str = 'NumSat'  #
    NumXop: str = 'NumXop'  #
    NodeId: str = 'NodeId'  #
    CustomModel: str = 'CustomModel'  #
    Type: str = 'Type'  #
    TypeSat: str = 'TypeSat'  #
    Id: str = 'Id'  #
    disp_num: str = 'disp_num'  #
    ngou: str = 'ngou'  #
    tgA: str = 'tgA'  #
    Vgain: str = 'Vgain'  #
    Tarif: str = 'Tarif'  #
    S: str = 'S'  #
    _adjpq: str = '_adjpq'  #
    Bmin: str = 'Bmin'  #

    # U - напряжение
    modV: str = 'modV'  #
    Eq: str = 'Eq'  #
    Eqnom: str = 'Eqnom'  #
    Eq1: str = 'Eq1'  #
    Eq2: str = 'Eq2'  #
    Vdrop: str = 'Vdrop'  #
    E: str = 'E'  #
    Ed1: str = 'Ed1'  #
    Ed2: str = 'Ed2'  #

    urE: str = 'urE'  #

    urDelta: str = 'urDelta'  #
    Delta: str = 'Delta'  #

    # Р - активная мощность
    P: str = 'P'  #
    Pgconst: str = 'Pgconst'  #
    Pmax: str = 'Pmax'  #
    Pmin: str = 'Pmin'  #
    Pnom: str = 'Pnom'  #
    Pdem: str = 'Pdem'  #

    # Q - реактивная мощность
    Q: str = 'Q'  #
    Qmax: str = 'Qmax'  #
    Qmin: str = 'Qmin'  #

    Ugnom: str = 'Ugnom'  #
    cosFi: str = 'cosFi'  #
    Demp: str = 'Demp'  #
    Mj: str = 'Mj'  #

    # сопротивление
    r: str = 'r'  #
    x: str = 'x'  #
    r0: str = 'r0'  #
    r2: str = 'r2'  #

    # сопротивления оси - d
    xd: str = 'xd'  #
    xd1: str = 'xd1'  #
    xd2: str = 'xd2'  #

    # сопротивления оси - q
    xq: str = 'xq'  #
    xq1: str = 'xq1'  #
    xq2: str = 'xq2'  #

    xl: str = 'xl'  #
    x0: str = 'x0'  #
    x2: str = 'x2'  #

    # I - ток
    Inom: str = 'Inom'  #
    modI: str = 'modI'  #
    i0: str = 'i0'  #
    di0: str = 'di0'  #
    i1: str = 'i1'  #
    di1: str = 'di1'  #
    i2: str = 'i2'  #
    di2: str = 'di2'  #
    ia: str = 'ia'  #
    dia: str = 'dia'  #
    ib: str = 'ib'  #
    dib: str = 'dib'  #
    ic: str = 'ic'  #
    dic: str = 'dic'  #
    ki: str = 'ki'  #
    ke: str = 'ke'  #

    td01: str = 'td01'  # T'd0 Переходная постоянная времени по продольной оси при разомкнутой обмотке статора
    td02: str = 'td02'  # T"d0 Сверхпереходная постоянная времени по продольной оси при разомкнутой обмотке статора

    tq01: str = 'tq01'  # T'q0 Переходная постоянная времени по поперечной оси при разомкнутой обмотке статора
    tq02: str = 'tq02'  # T"q0 Сверхпереходная постоянная времени по поперечной оси при разомкнутой обмотке статора


class GeneratorsDescription:
    """

    """
    gen = Generator()

    name_table: str = 'Таблица: Генераторы(ИД)'
    row_id: str = f'Порядковый номер в таблице Генераторы(ИД): возвращается функцией FindNexSel'
    sta: str = f'Состояние генератора [S]-[{gen.sta}]'
    Num: str = f'Номер генератора [N]-[{gen.Num}]'
    Name: str = f'Название генератора [Название]-[{gen.Name}]'
    Node: str = f'Номер узла [N узла]-[{gen.Node}]'
    ModelType: str = f'Модель генератора [Модель]-[{gen.ModelType}]'
    Brand: str = f'Марка генератора [Марка]-[{gen.Brand}]'
    NumBrand: str = f'Число генераторов одного типа [K_ген]-[{gen.NumBrand}]'
    ExciterId: str = f'N_возбудителя [N_взб]-[{gen.ExciterId}]'
    ARSId: str = f'N турб [N турб]-[{gen.ARSId}]'
    Pnom: str = f'Номинальная мощность генератора [P_ном]-[{gen.Pnom}]'
    Ugnom: str = f'Номинальное напряжение генератора [Uг_ном]-[{gen.Ugnom}]'
    cosFi: str = f'Номинальный коэффициент мощности [COS(Ф)_ном]-[{gen.cosFi}]'
    Demp: str = f'Коэффициент демпфирования [К_демп]-[{gen.Demp}]'
    Mj: str = f'Механическая постоянная инерции генератора вместе с турбиной [Mj]-[{gen.Mj}]'
    xd1: str = f"Переходное реактивное сопротивление по продольной оси [X'd]-[{gen.xd1}]"
    xd: str = f'Синхронное реактивное сопротивление по продольной оси [Xd]-[{gen.xd}]'
    xq: str = f'Синхронное реактивное сопротивление по поперечной оси [Xq]-[{gen.xq}]'
    xd2: str = f'Сверхпереходное реактивное сопротивление по продольной оси [X"d]-[{gen.xd2}]'
    xq2: str = f'Сверхпереходное реактивное сопротивление по поперечной оси [X"q]-[{gen.xq2}]'
    td01: str = f"Переходная постоянная времени по продольной оси при разомкнутой обмотке статора [T'd0]-[{gen.td01}]"
    td02: str = f'Сверхпереходная постоянная времени по продольной оси при разомкнутой обмотке статора [T"d0]-[{gen.td02}]'
    tq02: str = f'Сверхпереходная постоянная времени по поперечной оси при разомкнутой обмотке статора [T"q0]-[{gen.tq02}]'
    xq1: str = f"Переходное реактивное сопротивление по поперечной оси [X'q]-[{gen.xq1}]"
    xl: str = f'Реактивное сопротивление рассеивания [X_l]-[{gen.xl}]'
    x2: str = f'Реактивное сопротивление сопротивление обратной последовательности [X2]-[{gen.x2}]'
    x0: str = f'Реактивное сопротивление сопротивление нулевой последовательности [X0]-[{gen.x0}]'
    tq01: str = f"Переходная постоянная времени по поперечной оси при разомкнутой обмотке статора [T'q0]-[{gen.tq01}]"


param_gen = [Generator.Num, Generator.Name, Generator.ModelType, Generator.Pnom, Generator.Ugnom, Generator.cosFi,
             Generator.Demp, Generator.Mj, 'Tj=Mj/Pnom', Generator.xd1, Generator.xd, Generator.xq, Generator.xd2, Generator.xq2,
             Generator.td01, Generator.td02, Generator.tq02, Generator.xq1, Generator.xl]

par_gen_x = [Generator.xd1, Generator.xd, Generator.xq, Generator.xd2, Generator.xq2,
             Generator.td01, Generator.td02, Generator.tq02, Generator.xq1, Generator.xl]