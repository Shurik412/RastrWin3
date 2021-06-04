# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "ОМВ" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tables.Dynamic.DFW421UEL import DFW421UEL, DFW421UEL_Description
from RastrWinLib.variables.variable_parametrs import Variable


def filling_DFW421UEL(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        CustomModel: str = None,
        Dependency_F1: int = None,
        Output: str = None,
        K1: float = None,
        K2: float = None,
        Kul: float = None,
        Kui: float = None,
        Kuf: float = None,
        Kur: float = None,
        Kuc: float = None,
        Kl: float = None,
        Tu1: float = None,
        Tu2: float = None,
        Tu3: float = None,
        Tu4: float = None,
        Tuf: float = None,
        TuV: float = None,
        TuP: float = None,
        TuQ: float = None,
        Vurmax: float = None,
        Vucmax: float = None,
        Vulmax: float = None,
        Vulmin: float = None,
        Vuimin: float = None,
        Vuimax: float = None,
        switch_command_line: bool = False
):
    """

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице: возвращается функцией FindNexSel;
    :param sel: Отметка [O];
    :param sta: Состояние ОМВ [S];
    :param Id: Номер ОМВ [N ОМВ];
    :param Name: Название ОМВ [Название];
    :param ModelType: Модель ОМВ [Модель];
    :param Brand: Марка ОМВ [Марка];
    :param CustomModel: Модель в конструкторе [Конструктор];
    :param Dependency_F1: Номер зависимости Q(P) (UEL-2) [Q(P)];
    :param Output: Режим выхода [Выход];
    :param K1: Показатель степени F1 (UEL-2) [K1];
    :param K2: Показатель степени F2 (UEL-2) [K2];
    :param Kul: Пропорциональный коэффициент регулятора [Kul];
    :param Kui: Интегральный коэффициент регулятора [Kui];
    :param Kuf: Коэффициент обратной связи по току возбуждения [Kuf];
    :param Kur: Коэффициент радиуса (UEL-1) [Kur];
    :param Kuc: Коэффициент центра (UEL-1) [Kuc];
    :param Kl: Коэффициент усиления в режиме прямого выхода [Kl];
    :param Tu1: Постоянная времени регулятора [Tu1];
    :param Tu2: Постоянная времени регулятора [Tu2];
    :param Tu3: Постоянная времени регулятора [Tu3];
    :param Tu4: Постоянная времени регулятора [Tu4];
    :param Tuf: Коэффициент обратной связи по току возбуждения [Tuf];
    :param TuV: Постоянная времени фильтра напряжения (UEL-2) [TuV];
    :param TuP: Постоянная времени фильтра активной мощности (UEL-2) [TuP];
    :param TuQ: Постоянная времени фильтра реактивной мощности (UEL-2) [TuQ];
    :param Vurmax: Ограничение радиуса (UEL-1) [Vurmax];
    :param Vucmax: Ограничение центра (UEL-1) [Vucmax];
    :param Vulmax: Максимальное ограничение ОМВ [Vulmax];
    :param Vulmin: Минимальное ограничение ОМВ [Vulmin];
    :param Vuimin: Минимальное ограничение регулятора [Vuimin];
    :param Vuimax: Максимальное ограничение регулятора [Vuimax];
    :param switch_command_line:
    :return:
    """

    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.sel,
                                       row_id=row_id,
                                       value=sel)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.sta,
                                       row_id=row_id,
                                       value=sta)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Id,
                                       row_id=row_id,
                                       value=Id)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Name,
                                       row_id=row_id,
                                       value=Name)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.ModelType,
                                       row_id=row_id,
                                       value=ModelType)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Brand,
                                       row_id=row_id,
                                       value=Brand)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.CustomModel,
                                       row_id=row_id,
                                       value=CustomModel)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Dependency_F1,
                                       row_id=row_id,
                                       value=Dependency_F1)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Output,
                                       row_id=row_id,
                                       value=Output)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.K1,
                                       row_id=row_id,
                                       value=K1)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.K2,
                                       row_id=row_id,
                                       value=K2)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Kul,
                                       row_id=row_id,
                                       value=Kul)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Kui,
                                       row_id=row_id,
                                       value=Kui)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Kuf,
                                       row_id=row_id,
                                       value=Kuf)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Kur,
                                       row_id=row_id,
                                       value=Kur)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Kuc,
                                       row_id=row_id,
                                       value=Kuc)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Kl,
                                       row_id=row_id,
                                       value=Kl)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Tu1,
                                       row_id=row_id,
                                       value=Tu1)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Tu2,
                                       row_id=row_id,
                                       value=Tu2)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Tu3,
                                       row_id=row_id,
                                       value=Tu3)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Tu4,
                                       row_id=row_id,
                                       value=Tu4)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Tuf,
                                       row_id=row_id,
                                       value=Tuf)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.TuV,
                                       row_id=row_id,
                                       value=TuV)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.TuP,
                                       row_id=row_id,
                                       value=TuP)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.TuQ,
                                       row_id=row_id,
                                       value=TuQ)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Vurmax,
                                       row_id=row_id,
                                       value=Vurmax)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Vucmax,
                                       row_id=row_id,
                                       value=Vucmax)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Vulmax,
                                       row_id=row_id,
                                       value=Vulmax)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Vulmin,
                                       row_id=row_id,
                                       value=Vulmin)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Vuimin,
                                       row_id=row_id,
                                       value=Vuimin)

    variable_.make_changes_filling_row(table=DFW421UEL.table,
                                       column=DFW421UEL.Vuimax,
                                       row_id=row_id,
                                       value=Vuimax)


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.tables.Dynamic.DFW421UEL import DFW421UEL
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.save import save_file
    from RastrWinLib.loading.shablon import Shabl

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test.rst',
              shabl=Shabl.shablon_file_dynamic)

    load_file(rastr_win=RASTR,
              file_path='',
              shabl=Shabl.shablon_file_automation)

    table_ = RASTR.Tables(DFW421UEL.table)

    for i in range(0, 1000):
        table_.AddRow()
        filling_DFW421UEL(
            rastr_win=RASTR,
            row_id=i,
            sel=None,
            sta=None,
            Id=123456789,
            Name=f'Генератор {i}',
            ModelType=None,
            Brand=None,
            CustomModel=None,
            Dependency_F1=12345679,
            Output=None,
            K1=0.123456,
            K2=0.123456,
            Kul=0.123456,
            Kui=0.123456,
            Kuf=0.123456,
            Kur=0.123456,
            Kuc=0.123456,
            Kl=0.123456,
            Tu1=0.123456,
            Tu2=0.123456,
            Tu3=0.123456,
            Tu4=0.123456,
            Tuf=0.123456,
            TuV=0.123456,
            TuP=0.123456,
            TuQ=0.123456,
            Vurmax=0.123456,
            Vucmax=0.123456,
            Vulmax=0.123456,
            Vulmin=0.123456,
            Vuimin=0.123456,
            Vuimax=0.123456,
            switch_command_line=False)

    save_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test_DFW421UEL.rst',
              shabl=Shabl.shablon_file_dynamic)
