# -*- coding: utf-8 -*-
# Модуль заполнения таблицы  "Возбудители Thyne 1-4" RastrWin3

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Tables.Dynamic.DFWTHYNE14 import DFWTHYNE14, DFWTHYNE14_Description
from RastrWinLib.Variables.variable_parametrs import Variable


def filling_DFWTHYNE14(
        rastr_win=RASTR,
        row_id: int = None,
        sel: bool = None,
        sta: bool = None,
        Id: int = None,
        Name: str = None,
        ModelType: str = None,
        Brand: str = None,
        UELId: int = None,
        PSSId: int = None,
        Aex: float = None,
        Bex: float = None,
        Alpha: float = None,
        Beta: float = None,
        IfdMin: float = None,
        Kc: float = None,
        Kd1: float = None,
        Kd2: float = None,
        Ke: float = None,
        Ketb: float = None,
        Kh: float = None,
        Kp1: float = None,
        Kp2: float = None,
        Kp3: float = None,
        Td1: float = None,
        Te1: float = None,
        Te2: float = None,
        Ti1: float = None,
        Ti2: float = None,
        Ti3: float = None,
        Tr1: float = None,
        Tr2: float = None,
        Tr3: float = None,
        Tr4: float = None,
        VO1Max: float = None,
        VO1Min: float = None,
        VO2Max: float = None,
        VO2Min: float = None,
        VO3Max: float = None,
        VO3Min: float = None,
        VD1Max: float = None,
        VD1Min: float = None,
        VI1Max: float = None,
        VI1Min: float = None,
        VI2Max: float = None,
        VI2Min: float = None,
        VI3Max: float = None,
        VI3Min: float = None,
        VP1Max: float = None,
        VP1Min: float = None,
        VP2Max: float = None,
        VP2Min: float = None,
        VP3Max: float = None,
        VP3Min: float = None,
        VrMax: float = None,
        VrMin: float = None,
        Xp: float = None,
        switch_command_line: bool = False
):
    """
    Функция filling_DFWTHYNE14 - вносит изменения в таблицу "Возбудители Thyne 1-4".

    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param row_id: Порядковый номер в таблице: возвращается функцией FindNexSel;
    :param sel: Отметка [O];
    :param sta: Состояние возбудителя [S];
    :param Id: Номер возбудителя [N взб];
    :param Name: Название возбудителя [Название];
    :param ModelType: Модель возбудителя [Модель];
    :param Brand: Марка возбудителя [Марка];
    :param UELId: Номер ОМВ [N ОМВ];
    :param PSSId: Номер системного стабилизатора [N стаб];
    :param Aex: Коэффициент насыщения возбудителя [Aex];
    :param Bex: Коэффициент насыщения возбудителя [Bex];
    :param Alpha: Статизм по активной мощности [Alpha];
    :param Beta: Статизм по реактивной мощности [Beta];
    :param IfdMin: Уставка минимального тока ротора [IfdMin];
    :param Kc: Коэффициент усиления [Kc];
    :param Kd1: Коэффициент усиления [Kd1];
    :param Kd2: Коэффициент усиления [Kd2];
    :param Ke: Коэффициент усиления [Ke];
    :param Ketb: Коэффициент усиления тиристорного моста [Ketb];
    :param Kh: Коэффициент усиления [Kh];
    :param Kp1: Коэффициент усиления регулятора напряжения [Kp1];
    :param Kp2: Коэффициент усиления регулятора тока ротора [Kp2];
    :param Kp3: Коэффициент усиления минимального токового реле [Kp3];
    :param Td1: Постоянная времени дифференциального канала регулятора напряжения [Td1];
    :param Te1: Постоянная времени тиристорного моста [Te1];
    :param Te2: Постоянная времени возбудителя [Te2];
    :param Ti1: Постоянная времени регулятора напряжения [Ti1];
    :param Ti2: Постоянная времени регулятора тока [Ti2];
    :param Ti3: Постоянная времени минимального токового реле [Ti3];
    :param Tr1: Постоянная времени входного фильтра [Tr1];
    :param Tr2: Постоянная времени входного фильтра [Tr2];
    :param Tr3: Постоянная времени входного фильтра [Tr3];
    :param Tr4: Постоянная времени входного фильтра [Tr4];
    :param VO1Max: Максимальное ограничение канала регулятора напряжения [VO1Max];
    :param VO1Min: Минимальное ограничение канала регулятора напряжения [VO1Min];
    :param VO2Max: Максимальное ограничение канала регулятора тока ротора [VO2Max];
    :param VO2Min: Минимальное ограничение канала регулятора тока ротора [VO2Min];
    :param VO3Max: Максимальное ограничение минимального токового реле [VO3Max];
    :param VO3Min: Минимальное ограничение минимального токового реле [VO3Min];
    :param VD1Max: Максимальное ограничение дифференциального канала [VD1Max];
    :param VD1Min: Минимальное ограничение дифференциального канала [VD1Min];
    :param VI1Max: Максимальное ограничение интегрального канала регулятора напряжения [VI1Max];
    :param VI1Min: Минимальное ограничение интегрального канала регулятора напряжения [VI1Min];
    :param VI2Max: Максимальное ограничение интегрального канала регулятора тока ротора [VI2Max];
    :param VI2Min: Минимальное ограничение интегрального канала регулятора тока ротора [VI2Min];
    :param VI3Max: Максимальное ограничение интегрального канала минимального токового реле [VI3Max];
    :param VI3Min: Минимальное ограничение интегрального канала  минимального токового реле [VI3Min];
    :param VP1Max: Максимальное ограничение пропорционального канала регулятора напряжения [VP1Max];
    :param VP1Min: Минимальное ограничение пропорционального канала регулятора напряжения [VP1Min];
    :param VP2Max: Максимальное ограничение пропорционального канала регулятора тока ротора [VP2Max];
    :param VP2Min: Минимальное ограничение пропорционального канала регулятора тока ротора [VP2Min];
    :param VP3Max: Максимальное ограничение пропорционального канала минимального токового реле [VP3Max];
    :param VP3Min: Минимальное ограничение пропорционального канала минимального токового реле [VP3Min];
    :param VrMax: Максимальное ограничение тиристорного моста [VrMax];
    :param VrMin: Минимальное ограничение тиристорного моста [VrMin];
    :param Xp: Коэффициент обратной связи [Xp];
    :param switch_command_line: True/False - вывод сообщений в протокол;
    :return: Noting return.
    """

    variable_ = Variable(rastr_win=rastr_win)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.sel,
                                       row_id=row_id,
                                       value=sel)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.sta,
                                       row_id=row_id,
                                       value=sta)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Id,
                                       row_id=row_id,
                                       value=Id)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Name,
                                       row_id=row_id,
                                       value=Name)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.ModelType,
                                       row_id=row_id,
                                       value=ModelType)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Brand,
                                       row_id=row_id,
                                       value=Brand)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.UELId,
                                       row_id=row_id,
                                       value=UELId)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.PSSId,
                                       row_id=row_id,
                                       value=PSSId)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Aex,
                                       row_id=row_id,
                                       value=Aex)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Bex,
                                       row_id=row_id,
                                       value=Bex)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Alpha,
                                       row_id=row_id,
                                       value=Alpha)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Beta,
                                       row_id=row_id,
                                       value=Beta)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.IfdMin,
                                       row_id=row_id,
                                       value=IfdMin)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Kc,
                                       row_id=row_id,
                                       value=Kc)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Kd1,
                                       row_id=row_id,
                                       value=Kd1)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Kd2,
                                       row_id=row_id,
                                       value=Kd2)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Ke,
                                       row_id=row_id,
                                       value=Ke)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Ketb,
                                       row_id=row_id,
                                       value=Ketb)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Kh,
                                       row_id=row_id,
                                       value=Kh)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Kp1,
                                       row_id=row_id,
                                       value=Kp1)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Kp2,
                                       row_id=row_id,
                                       value=Kp2)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Kp3,
                                       row_id=row_id,
                                       value=Kp3)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Td1,
                                       row_id=row_id,
                                       value=Td1)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Te1,
                                       row_id=row_id,
                                       value=Te1)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Te2,
                                       row_id=row_id,
                                       value=Te2)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Ti1,
                                       row_id=row_id,
                                       value=Ti1)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Ti2,
                                       row_id=row_id,
                                       value=Ti2)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Ti3,
                                       row_id=row_id,
                                       value=Ti3)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Tr1,
                                       row_id=row_id,
                                       value=Tr1)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Tr2,
                                       row_id=row_id,
                                       value=Tr2)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Tr3,
                                       row_id=row_id,
                                       value=Tr3)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Tr4,
                                       row_id=row_id,
                                       value=Tr4)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VO1Max,
                                       row_id=row_id,
                                       value=VO1Max)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VO1Min,
                                       row_id=row_id,
                                       value=VO1Min)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VO1Min,
                                       row_id=row_id,
                                       value=VO1Min)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VO2Max,
                                       row_id=row_id,
                                       value=VO2Max)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VO2Min,
                                       row_id=row_id,
                                       value=VO2Min)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VO3Max,
                                       row_id=row_id,
                                       value=VO3Max)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VO3Min,
                                       row_id=row_id,
                                       value=VO3Min)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VD1Max,
                                       row_id=row_id,
                                       value=VD1Max)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VD1Min,
                                       row_id=row_id,
                                       value=VD1Min)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VI1Max,
                                       row_id=row_id,
                                       value=VI1Max)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VI1Min,
                                       row_id=row_id,
                                       value=VI1Min)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VI2Max,
                                       row_id=row_id,
                                       value=VI2Max)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VI2Min,
                                       row_id=row_id,
                                       value=VI2Min)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VI3Max,
                                       row_id=row_id,
                                       value=VI3Max)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VI3Min,
                                       row_id=row_id,
                                       value=VI3Min)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VP1Max,
                                       row_id=row_id,
                                       value=VP1Max)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VP1Min,
                                       row_id=row_id,
                                       value=VP1Min)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VP2Max,
                                       row_id=row_id,
                                       value=VP2Max)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VP2Min,
                                       row_id=row_id,
                                       value=VP2Min)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VP3Max,
                                       row_id=row_id,
                                       value=VP3Max)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VP3Min,
                                       row_id=row_id,
                                       value=VP3Min)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VrMax,
                                       row_id=row_id,
                                       value=VrMax)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.VrMin,
                                       row_id=row_id,
                                       value=VrMin)

    variable_.make_changes_filling_row(table=DFWTHYNE14.table,
                                       column=DFWTHYNE14.Xp,
                                       row_id=row_id,
                                       value=Xp)


if __name__ == '__main__':
    from RastrWinLib.AstraRastr import RASTR
    from RastrWinLib.loading.load import load_file
    from RastrWinLib.loading.save import save_file
    from RastrWinLib.loading.shablon import Shabl
    from RastrWinLib.Tables.Dynamic.DFWTHYNE14 import DFWTHYNE14

    load_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test.rst',
              shabl=Shabl.shablon_file_dynamic)

    table_ = RASTR.Tables(DFWTHYNE14.table)

    for i in range(0, 100):
        table_.AddRow()

        filling_DFWTHYNE14(
            rastr_win=RASTR,
            row_id=i,
            sel=None,
            sta=None,
            Id=123456789,
            Name=f'Генератор {i}',
            ModelType=None,
            Brand=None,
            UELId=123456789,
            PSSId=123456789,
            Aex=0.123456,
            Bex=0.123456,
            Alpha=0.123456,
            Beta=0.123456,
            IfdMin=0.123456,
            Kc=0.123456,
            Kd1=0.123456,
            Kd2=0.123456,
            Ke=0.123456,
            Ketb=0.123456,
            Kh=0.123456,
            Kp1=0.123456,
            Kp2=0.123456,
            Kp3=0.123456,
            Td1=0.123456,
            Te1=0.123456,
            Te2=0.123456,
            Ti1=0.123456,
            Ti2=0.123456,
            Ti3=0.123456,
            Tr1=0.123456,
            Tr2=0.123456,
            Tr3=0.123456,
            Tr4=0.123456,
            VO1Max=0.123456,
            VO1Min=0.123456,
            VO2Max=0.123456,
            VO2Min=0.123456,
            VO3Max=0.123456,
            VO3Min=0.123456,
            VD1Max=0.123456,
            VD1Min=0.123456,
            VI1Max=0.123456,
            VI1Min=0.123456,
            VI2Max=0.123456,
            VI2Min=0.123456,
            VI3Max=0.123456,
            VI3Min=0.123456,
            VP1Max=0.123456,
            VP1Min=0.123456,
            VP2Max=0.123456,
            VP2Min=0.123456,
            VP3Max=0.123456,
            VP3Min=0.123456,
            VrMax=0.123456,
            VrMin=0.123456,
            Xp=0.123456,
            switch_command_line=False)

    save_file(rastr_win=RASTR,
              file_path=r'C:\Users\Ohrimenko_AG\Desktop\test_filling\test_DFWTHYNE14.rst',
              shabl=Shabl.shablon_file_dynamic)
